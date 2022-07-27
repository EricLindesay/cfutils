from .regex_convert import *

def format_note(unformatted: str) -> str:
    '''
    Format the note.
    The note can be empty.

    We just want to set the Note header and convert all the tags as you
    would for the problem statement.
    All of the useful data is within the <p></p> tags
    '''
    if not unformatted:
        return ""
        
    header = "\n\n### Note\n"
    r = re.search("<p>.*</p>", unformatted)
    if r:
        formatted_string = r.group(0)
        formatted_string = convert_latex(formatted_string)
        formatted_string = convert_random_specials(formatted_string)
        formatted_string = convert_tags(formatted_string)
    else:
        # If we can't find the <p> tags, then something went wrong so
        # just add the unformatted text to the readme instead. So you can do
        # it manually.
        formatted_string = unformatted

    return header + formatted_string.rstrip()

