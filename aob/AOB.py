from aob.wildcards import get_mask, sanitize_wildcards

from iced_x86 import Register, Decoder

_REGISTERS = [Register.EAX, Register.EBX, Register.ECX, Register.EDX, Register.EBP, Register.EDI, Register.ESI] # ESP is weird to change

class AOB(object):

  def __init__(self, string: str):
    self.string = sanitize_wildcards(string)
    self.mask = get_mask(string)

  def generate_permutation(self, start = 0):
    decoder = Decoder(32, bytes.fromhex(self.string))
    instructions = []
    offset = -1
    for instruction in decoder:
      offset += 1
      instructions.append(instruction)
      if offset <= start:
        continue
      op_code = instruction.op_code()
      op_code_string = str(op_code)
      # Is permutable?
      if not "r/m32" in op_code_string and not "r32" in op_code_string:
        continue
      pass