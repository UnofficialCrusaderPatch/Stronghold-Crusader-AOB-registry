import aob.AOB

def test_aob_init():
  a = aob.AOB.AOB.from_string("AA ? BB ?? C1 ?? DD EE FF 01")
  b = aob.AOB.AOB.from_bytes(b"\xe8\x66\xcb\xe9\xff")