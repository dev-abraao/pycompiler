def parse(tokens, line_number):

  if len(tokens) == 0:
      return

  command = tokens[0][1]

  if command == "SET":
      if len(tokens) != 3:
        raise Exception(f"Erro sintático na linha {line_number}: SET precisa de 2 argumentos")

      if tokens[1][0] != "IDENTIFIER":
        raise Exception(f"Erro sintático na linha {line_number}: esperado IDENTIFIER")

      if tokens[2][0] != "NUMBER":
        raise Exception(f"Erro sintático na linha {line_number}: esperado NUMBER")

  elif command in ["ADD", "SUB", "MUL", "DIV"]:
      if len(tokens) != 3:
        raise Exception(f"Erro sintático na linha {line_number}: operação precisa de 2 operandos")

      if tokens[1][0] not in ["IDENTIFIER", "NUMBER"]:
        raise Exception(f"Erro sintático na linha {line_number}: operando inválido")

      if tokens[2][0] not in ["IDENTIFIER", "NUMBER"]:
        raise Exception(f"Erro sintático na linha {line_number}: operando inválido")

  elif command == "PRINT":
      if len(tokens) != 2:
        raise Exception(f"Erro sintático na linha {line_number}: PRINT precisa de 1 argumento")

      if tokens[1][0] != "IDENTIFIER":
        raise Exception(f"Erro sintático na linha {line_number}: PRINT aceita apenas variável")

  else:
    raise Exception(f"Erro sintático na linha {line_number}: comando desconhecido")