from lexer import tokenize_line
from parser import parse
from semantic import check_semantics
from translator import translate


def compile_file(input_file, output_file):

  python_lines = []

  with open(input_file, "r") as file:
    lines = file.readlines()

  line_number = 1

  for line in lines:

    if line.strip() == "":
      line_number += 1
      continue

    try:

      tokens = tokenize_line(line)

      parse(tokens, line_number)

      check_semantics(tokens, line_number)

      python_code = translate(tokens)

      python_lines.append(python_code)

    except Exception as error:

      print(error)
      return

    line_number += 1

  with open(output_file, "w") as f:

    for line in python_lines:
        f.write(line + "\n")

  print("Compilação finalizada. Arquivo gerado:", output_file)


if __name__ == "__main__":

  compile_file("entrada.calc", "saida.py")