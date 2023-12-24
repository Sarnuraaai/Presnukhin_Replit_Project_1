def to_snake_case(string):
  res = ""
  for x in string:
    res = res + '_' + x.lower() if x.isupper() else res + x
  return res


def to_camel_case(string):
  res = ''
  caps = False
  for x in string:
    if x == '_':
      caps = True
    else:
      if caps:
        res = res + x.upper()
        caps = False
      else:
        res = res + x
  return res
