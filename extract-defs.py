import re
from main import convert_pdf_to_string, convert_pdf_to_html

FILE_PATH = "./docs/contracts/groundfloor-sub.pdf"

def extract_definitions_from_text(text):
  definitions = {}

  new_text = text.replace('“', '"').replace("”", '"').replace("", "") # normalize all quotation marks to "

  for match in re.finditer(r"\"([^\"’]*)(\"|’)\s? means", new_text):
    term = match.groups()[0]
    def_start = match.span()[1]
    def_end = new_text.find("1.", def_start)
    definition = new_text[def_start:def_end].replace("\n", " ").replace("1.", "")
    definitions[term] = definition

  previous_section_at = 0
  last_section_num = 0
  sections = {}

  for i in range(1, 20):
    pattern = re.compile(f"{i}\. ")
    match = pattern.search(new_text, previous_section_at)
    if match:
      def_start = match.span()[0]
      previous_section_at = def_start
      def_end = new_text.find(".", def_start + 3)
      definition = new_text[def_start:def_end].replace("\n", " ")
      sections[i] = {"start": def_start, "name": definition, "subsections": []}
    else:
      last_section_num = i - 1
      break
  
  for i in range(1, last_section_num + 1):
    current_section = sections[i]
    next_section = {"start": len(new_text)}
    
    if i != last_section_num:
      next_section = sections[i + 1]

    subsections = []
  
    for j in range(97, 123):
      pattern = re.compile(f"\n\({chr(j)}\) ")
      match = pattern.search(new_text, current_section["start"], next_section["start"])
      
      if match:
        section_start = match.span()[0] + 1
        subsections.append(section_start)
      else:
        subsections.append(next_section["start"])
        break
    
    for idx, start in enumerate(subsections):
      if idx != len(subsections) - 1:
        section_end = subsections[idx + 1]
        sections[i]["subsections"].append(new_text[start:section_end][:20].replace("\n", ""))
  
  return (sections, definitions)

def main():
  text = convert_pdf_to_string(FILE_PATH)
  sections, definitions = extract_definitions_from_text(text)
  print(sections)
  print(definitions)
  html = convert_pdf_to_html(FILE_PATH, definitions)
  print(html)

if __name__ == '__main__':
  main()