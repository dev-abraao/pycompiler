OPERATORS = ['SET' ,'ADD', 'SUB', 'MUL', 'DIV', 'PRINT']

def tokenize_line(line):
  tokens = []
  current = ""

  for char in line:
    if char == " " or char == "\n":
      if current != "":
        tokens.append(classify(current))
        current = ""
    else:
      current += char

  if current != "":
    tokens.append(classify(current))

  return tokens

def classify(word):
  if word in OPERATORS:
    return ("COMMAND", word)

  elif word.isalpha():
    return ("IDENTIFIER", word)

  elif word.isnumeric():
    return ("NUMBER", int(word))

  else:
    raise Exception(f"Token inválido: {word}")
