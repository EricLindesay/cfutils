from operator import contains
import re

from numpy import extract
from .regex_convert import convert_tags, convert_random_specials, convert_latex
from modules import regex_convert


def extract_note(html: str, triple=True) -> str:
    default = "\n```\n" if triple else ""
    default += "\n### Note\n"
    r = re.search("<p>.*</p>", html)
    if r:
        string = r.group(0)
        string = convert_latex(string)
        string = convert_random_specials(string)
        string = convert_tags(string)
    else:
        string = html

    return default + string.rstrip()


def format_input(input: str) -> str:
    string = re.sub("<div class=\"title\">", "", input)
    string = re.sub("<div class=\"output\">", "", string)
    string = re.sub("</div>", "", string)
    string = re.sub("</?pre>", "\n", string)
    string = re.sub("<br\ ?/?>", "", string)
    return string + "```"


def one_liner(one_line: str) -> str:
    string = one_line
    string = re.sub("<div class=\"sample-tests\">", "\n### ", string)
    string = re.sub("<div class=\"input\">", "\n```\n", string)
    string = re.sub("<div class=\"note\">", "\n### ", string)

    # now split by \n and fix everything
    lines = string.strip().split("\n")
    print(lines)
    for i, line in enumerate(lines):
        if i == 0:  # the first line is the ### Examples one
            lines[i] = regex_convert.convert_tags(line)
            continue

        contains_input = re.search(".*Input.*", line)
        if contains_input:
            lines[i] = format_input(contains_input.group(0))
        
        contains_note = re.search(".*Note.*", line)
        if contains_note:
            lines[i] = extract_note(contains_note.group(0), False)

    return "\n".join(lines)


def format_example(example:str) -> str:
    lines = example.split("\n")
        
    lines_to_write = []
    if len(lines) > 1:
        # These should go at the start for formatting
        lines.insert(0, "### Examples\n")

        for i, line in enumerate(lines):
            if re.search("class=\"output\"", line):  # Format output inside ```
                lines[i] = "\nOutput"
            elif re.search("class=\"input\"", line):  # Format input inside ```
                lines[i] = "```\nInput\n"   # + any lines of input with \n

                r = re.search("Input</div>.*", line)  # if there are some lines of input, on the same line then add those
                if r:
                    r = regex_convert.clear_tags(r.group(0)[11:])
                    lines[i] += r
            elif re.search("class=\"note\"", line):  # Format note
                # extract and format the note
                lines[i] = extract_note(line)
                lines_to_write = lines[:i+1]  # after the notes, we don't want to include any of the final <div>s or newlines
                break
            else:
                # its just a plain input line
                lines[i] = "\n" + lines[i]
    
    if len(lines) == 1:
        lines_to_write = one_liner(lines[0])


    return ''.join(lines_to_write)


if __name__ == "__main__":
    format_example()
