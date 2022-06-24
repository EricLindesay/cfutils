import re

def convert_latex(latex: str) -> str:
    string = re.sub("\\\leq", "<=", latex)
    string = re.sub("\\\le", "<=", string)
    string = re.sub("\\\lt", "<", string)
    string = re.sub("\\\geq", ">=", string)
    string = re.sub("\\\ge", ">=", string)
    string = re.sub("\\\gt", ">", string)
    string = re.sub("\\\ldots", "...", string)
    string = re.sub("\\\dots", "...", string)
    return string

def convert_tags(tags: str) -> str:
    string = re.sub("<div.+?>", "", tags)
    string = re.sub("<p>", "", string)
    string = re.sub("</p>", "  \n\n", string)
    string = re.sub("</div>", "", string)
    string = re.sub("<.+?>", "`", string)  # if there is a random tag we haven't considered, just replace it with `
    return string

def convert_random_specials(string: str) -> str:
    string = re.sub("\$\$\$", "`", string)
    string = re.sub("\\\,", ",", string)
    return string

