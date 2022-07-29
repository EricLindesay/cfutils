import re


def format_name(unformatted: str) -> str:
    '''
    Format the name of the problem.  
    The name is always in the form:
        <div class="title">A. NAME</div>
    So, if we use regex we can find where the dot is and find where the </div> is and 
    then just copy the parts between.
    We then also have to strip the whitespace.  
    '''
    unformatted = unformatted.strip()
    formatted = re.search("(?<=\.).+?(?=</div>)", unformatted)
    return formatted.group(0).strip()


def format_difficulty(unformatted: str) -> str:
    '''
    Format the difficulty of the problem.
    The difficulty is always in the form of:
        \t*1200
    And we need to extract the numbers, so just search for the numbers in regex.
    '''
    difficulty = re.search("\d+", unformatted.strip()).group(0)  # search for the digits
    return f"{difficulty}"


def pascal_case(string: str) -> str:
    '''
    Convert a string into pascal case.
    '''
    capitalise_next = False
    new_string = ""
    for i, char in enumerate(string):
        if i == 0 or capitalise_next:
            new_string += char.upper()
            capitalise_next = False
        elif char == " ":
            new_string += " "
            capitalise_next = True
        else:
            new_string += char
    return new_string


def format_tags(unformatted: str) -> str:
    '''
    Format the tags into pascal case, seperated by a comma
    '''
    conversions = {
        "math": "maths",
        "sortings": "sorting",
        "dp": "dynamic programming",
    }
    formatted = ""
    for x in unformatted.split("\n"):
        if not x:
            continue
        
        x = x.strip()
        if x in conversions.keys():
            x = conversions[x]
        formatted += pascal_case(x.strip()) + ", "
    return formatted[:-2]

if __name__ == "__main__":
    print(format_tags("implementation\nmath\nbinary search"))
