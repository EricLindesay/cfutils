import re

def convert_latex(latex: str) -> str:
    '''
    Convert common latex expressions into expressions which
    can be interpreted by markdown.  
    '''
    string = re.sub(r"\\leq", "<=", latex)
    string = re.sub(r"\\le", "<=", string)
    string = re.sub(r"\\lt", "<", string)
    string = re.sub(r"\\geq", ">=", string)
    string = re.sub(r"\\ge", ">=", string)
    string = re.sub(r"\\gt", ">", string)
    string = re.sub(r"\\ldots", "...", string)
    string = re.sub(r"\\dots", "...", string)
    string = re.sub(r"\\cdots?", "*", string)
    string = re.sub(r"\\times", "*", string)
    return string

def convert_tags(tags: str) -> str:
    '''
    Convert common html tags into appropriate text which makes the file look nicer.
    '''
    string = re.sub("<div.+?>", "", tags)
    string = re.sub("<p>", "", string)
    string = re.sub("</p>", "  \n\n", string)
    string = re.sub("</div>", "", string)
    string = re.sub("<li>", "-", string)
    string = re.sub("</li>", "\n", string)
    string = re.sub("</?ul>", "", string)
    string = re.sub("</?ol>", "", string)
    string = re.sub("</?i>", "*", string)
    string = re.sub("<br.+?>", "\n", string)
    string = re.sub("<.+?>", "`", string)  # if there is a random tag we haven't considered, just replace it with `
    return string

def clear_tags(tags: str) -> str:
    '''
    Replace all html tags with an empty string.
    '''
    string = re.sub("<div.+?>", "", tags)
    string = re.sub("<p>", "", string)
    string = re.sub("</p>", "", string)
    string = re.sub("</div>", "", string)
    string = re.sub("<li>", "", string)
    string = re.sub("</li>", "", string)
    string = re.sub("</?ul>", "", string)
    string = re.sub("</?ol>", "", string)
    string = re.sub("</?i>", "", string)
    string = re.sub("<br.+?>", "", string)
    string = re.sub("<.+?>", "", string)
    return string

def convert_random_specials(string: str) -> str:
    '''
    Convert random special characters to the string representation.  
    '''
    string = re.sub("\$\$\$", "`", string)
    string = re.sub("\\\,", ",", string)
    string = re.sub("&quot;", "\"", string)
    return string

