symbol_table = {}


def check_semantics(tokens, line_number):

  command = tokens[0][1]

  if command == "SET":

    var = tokens[1][1]
    value = tokens[2][1]

    symbol_table[var] = value

  elif command in ["ADD", "SUB", "MUL", "DIV"]:

    for token in tokens[1:]:

      if token[0] == "IDENTIFIER":

        if token[1] not in symbol_table:
          raise Exception(
            f"Erro semântico na linha {line_number}: variável '{token[1]}' não declarada"
          )

  elif command == "PRINT":

    var = tokens[1][1]

    if var not in symbol_table:
      raise Exception(
        f"Erro semântico na linha {line_number}: variável '{var}' não declarada"
      )
