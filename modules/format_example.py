import re
from .regex_convert import *


def one_line_format_input(input: str) -> str:
    '''
    Format any of the lines which contain the string "Input"
    '''
    string = re.sub("<div class=\"title\">", "", input)
    string = re.sub("<div class=\"output\">", "", string)
    string = re.sub("</div>", "", string)
    string = re.sub("</?pre>", "\n", string)
    string = re.sub("<br\ ?/?>", "", string)
    return string + "```"


def one_liner(one_line: str) -> str:
    '''
    If the sample inputs are all on one line, do this and format them.
    What I do is pre-parse the line, doing some regular formatting stuff. 
    Then split the line based on \n and format the line containing ### Examples
    and format all of the input lines. This is because the input lines require the ```
    '''

    # Initial parsing of data
    string = one_line
    string = re.sub("<div class=\"sample-tests\">", "\n### ", string)
    string = re.sub("<div class=\"input\">", "\n```\n", string)
    string = re.sub("<div class=\"note\">", "\n### ", string)

    # now split by \n and format the input lines.
    lines = string.strip().split("\n")
    for i, line in enumerate(lines):
        if i == 0:  # the first line is the ### Examples one
            lines[i] = convert_tags(line)
            continue

        contains_input = re.search(".*Input.*", line)
        if contains_input:
            lines[i] = one_line_format_input(contains_input.group(0))
       
    return "\n".join(lines)


def multi_liner(lines: list[str]) -> str:
    lines_to_write = []
    # These should go at the start for formatting
    lines_to_write.append("### Examples")
    lines_to_write.append("```")
    lines_to_write.append("Input")
    
    r = re.search("Input</div>.*", lines[0])  # if there are some lines of input, on the same line then add those
    if r:
        r = clear_tags(r.group(0)[11:])
        lines_to_write.append(r)

    for i, line in enumerate(lines[1:]):
        if re.search("class=\"output\"", line):  # Format output inside ```
            lines_to_write.append("Output")
        elif re.search("class=\"input\"", line):  # Format input inside ```
            lines_to_write.append("```")
            lines_to_write.append("```")
            lines_to_write.append("Input")

            r = re.search("Input</div>.*", line)  # if there are some lines of input, on the same line then add those
            if r:
                r = clear_tags(r.group(0)[11:])
                lines_to_write.append(r)
        else:
            # if the line just contains tags and whitespace, ignore it. Otherwise:
            temp = clear_tags(line)
            if re.search("^\s*$", temp):  # if it contains only whitespace, don't add it
                continue
            # its just a plain input line
            lines_to_write.append(line)
    
    lines_to_write.append("```")   # add the final closing code block.
    return '\n'.join(lines_to_write)


def format_example(example:str) -> str:
    '''
    Format the examples.
    Split the lines by \n. If there is only one line, then parse it with that knowledge.
    Otherwise you have to do something different.
    '''
    lines = example.split("\n")
        
    if len(lines) == 1:
        lines_to_write = one_liner(lines[0])
    else:
        lines_to_write = multi_liner(lines)


    return lines_to_write


if __name__ == "__main__":
    format_example()
