from typing import List
from aob.parser import parse_aob
from aob.wildcards import get_mask, sanitize_wildcards

from iced_x86 import Register, Decoder, BlockEncoder

_REGISTERS = [Register.EAX, Register.EBX, Register.ECX, Register.EDX, Register.EBP, Register.EDI, Register.ESI] # ESP is weird to change

class AOB(object):

  def __init__(self, data: bytes, mask: List[bool] = None):
    self.data = data
    self.mask = mask

  def generate_permutation(self, start = 0):
    decoder = Decoder(32, self.data)
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

  @staticmethod
  def from_string(string: str):
    return AOB(*parse_aob(string))

  @staticmethod
  def from_bytes(data: bytes, mask: List[bool] = None):
    return AOB(data, mask if mask else [True] * len(data))