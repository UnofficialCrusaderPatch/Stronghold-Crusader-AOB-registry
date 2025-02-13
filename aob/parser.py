hexchars = '0123456789abcdef'
HEXCHARS = '0123456789ABCDEF'
wildcard = '?'
wildcards = '??'

import re
re_hex = re.compile('[A-Fa-f0-9]{2}')
re_wildcard = re.compile('[?]{1,2}')
re_both = re.compile('([A-Fa-f0-9]{2}|[?]{1,2})')

def parse_aob(string: str):
  data = []
  mask = []
  scanner = re_both.scanner(string)
  result = scanner.search()
  while result:
    needle = result.group(0)
    if re_hex.match(needle):
      data.append(bytes.fromhex(needle)[0])
    else:
      data.append(0x0)
    
    if re_wildcard.match(needle):
      mask.append(False)
    else:
      mask.append(True)
    
    result = scanner.search()

  return data, mask