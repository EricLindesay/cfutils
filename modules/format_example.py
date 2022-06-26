import re
from .regex_convert import convert_tags, convert_random_specials, convert_latex

def extract_note(html: str) -> str:
    default = "```\n### Note\n"
    r = re.search("<p>.*</p>", html)
    if r:
        string = r.group(0)
        string = convert_latex(string)
        string = convert_random_specials(string)
        string = convert_tags(string)
    else:
        string = html

    return default + string.rstrip()

def format_example(example:str) -> str:
    lines = example.split("\n")
    
    # These should go at the start for formatting
    lines.insert(0, "### Examples\n```\nInput\n")

    lines_to_write = []

    for i, line in enumerate(lines):
        if re.search("class=\"output\"", line):  # Format output inside ```
            lines[i] = "Output\n"
        elif re.search("class=\"input\"", line):  # Format input inside ```
            lines[i] = "```\n```\nInput\n"
        elif re.search("class=\"note\"", line):  # Format note
            # extract and format the note
            lines[i] = extract_note(line)
            lines_to_write = lines[:i+1]  # after the notes, we don't want to include any of the final <div>s or newlines
            break

    return ''.join(lines_to_write)


if __name__ == "__main__":
    format_example()
