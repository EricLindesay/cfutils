import re, regex_convert

def extract_note(html: str) -> str:
    default = "```\n### Note\n"
    r = re.search("<p>.*</p>", html)
    if r:
        string = r.group(0)
        string = regex_convert.convert_latex(string)
        string = regex_convert.convert_random_specials(string)
        string = regex_convert.convert_tags(string)
    else:
        string = html

    return default + string.rstrip()

def format_example(filename="examples.md"):
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()

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

    with open(filename, "w") as f:
        f.write(''.join(lines_to_write))


if __name__ == "__main__":
    format_example()
