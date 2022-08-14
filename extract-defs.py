import re

FILE_PATH = "./docs/contracts/groundfloor-sub.txt"

with open(FILE_PATH, 'r') as f:
  new_text = f.read().replace('“', '"').replace("”", '"') # normalize all quotation marks to "

  for match in re.finditer(r"\"([^\"’]*)(\"|’) means", new_text):
    term = match.groups()[0]
    def_start = match.span()[1]
    def_end = new_text.find("\n\n", def_start)
    definition = new_text[def_start:def_end].replace("\n", " ")
    print(f"Definition of {term}:")
    print(f"- {definition}")
    print()
    