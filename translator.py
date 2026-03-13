def translate(tokens):

    command = tokens[0][1]

    if command == "SET":

        var = tokens[1][1]
        value = tokens[2][1]

        return f"{var} = {value}"

    elif command == "ADD":

        op1 = tokens[1][1]
        op2 = tokens[2][1]

        return f"print({op1} + {op2})"

    elif command == "SUB":

        op1 = tokens[1][1]
        op2 = tokens[2][1]

        return f"print({op1} - {op2})"

    elif command == "MUL":

        op1 = tokens[1][1]
        op2 = tokens[2][1]

        return f"print({op1} * {op2})"

    elif command == "DIV":

        op1 = tokens[1][1]
        op2 = tokens[2][1]

        return f"print({op1} / {op2})"

    elif command == "PRINT":

        var = tokens[1][1]

        return f"print({var})"
