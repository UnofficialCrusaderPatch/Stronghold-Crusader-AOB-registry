import re

_PATTERN = re.compile("[?]{1,2}")

def sanitize_wildcards(string: str):
  return _PATTERN.sub("00", string)

def get_mask(string: str):
  for match in _PATTERN.finditer(string):
    pass
  return _PATTERN.findall(string)