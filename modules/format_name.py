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


if __name__ == "__main__":
    format_name()
