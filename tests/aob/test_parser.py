from aob.parser import parse_aob

def test_parser_a():
  data, mask = parse_aob("AA ? BB ?? C1 ?? DD EE FF 01")
  assert data == [0xAA, 0x00, 0xBB, 0x00, 0xC1, 0x00, 0xDD, 0xEE, 0xFF, 0x01]
  assert mask == [True, False, True, False, True, False, True, True, True, True]
