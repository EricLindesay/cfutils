import urllib.request
import re


def copy_between(string: str, start: str, end: str, single_line=False) -> str:
    '''
    Copies all data in a string between two values (or a newline, if single_line=False)
    '''
    include_newline = "" if single_line else "|\n"
    r = re.search(f"(?<={start}).+?(?=({end}{include_newline}))", string)
    if r:
        return r.group(0)
    return None


def get_problem_statement(line: str) -> str:
    '''
    Given a string, get the problem statement section out of it.
    The problem statement data always follows "standard output</div></div>" and ends with "<div class="sample-tests"
    So if we use those as our regex lookaheads, we can just get the data we want.
    '''
    problem_statement = copy_between(line+"\n", "standard output</div></div>", "<div class=\"sample-tests\"")
    if problem_statement:
        return problem_statement
    else:
        raise Exception("Could not find problem statement")


def get_name(line: str) -> str:
    '''
    Extract the name from a string.
    The name is always between the following two tags "<div class="title">" and "</div>"
    '''
    name = re.search("<div class=\"title\">.+?</div>", line)
    if name:
        return name.group(0)
    else:
        raise Exception("Could not find name")


def is_multiline_input(line: str) -> bool:
    '''
    See whether the input/output test data is on one line or on multiple.
    Count how many "class="input""s there are and count how many "class="output""s there are.
    Each input has a matching output. If there are an equal number of inputs and outputs
    then we know that all of the test data is contained on this line. Otherwise it isn't.
    '''
    multiline_input = line.count("class=\"input\"") - line.count("class=\"output\"")
    return bool(multiline_input)
    

def get_sample_input(line: str) -> str:
    '''
    Copy all of the sample input on this line. This line could end in \n if its multiline input 
    Or in <div class="note"> if it is a single line input
    '''
    test = copy_between(line+"\n", "", "<div class=\"note\">")
    if test:
        return test   
    raise Exception("Sample input not found")
    

def get_html_data(url) -> dict:
    '''
    Go through the html line by line.
    Then extract the following:
    - The difficulty
    - The name
    - The problem statement
    - The examples
    - The notes

    The examples can be on one line or on multiple so we have to 
    account for that.

    Note: In the for loop, the if must be ifs because there can be examples and
    the problem statement on the same line.
    '''

    url_info = {
        "difficulty": "",
        "name": "",
        "problem": "",
        "examples": "",
        "note": "",
    }

    # Get the html data from the url.
    fp = urllib.request.urlopen(url)

    START = 0  # while we are still looping through garbage data
    DIFFICULTY = 1  # while we are looking for the difficulty
    PROBLEM = 2  # while we are looking for the problem statement
    EXAMPLE = 3  # while we are looking for the example class
    NOTE = 4  # while we are looking for the note or for multiline input.

    state = START
    multiline_input = False

    # Loop through each line in the html
    for line in fp.readlines():
        line = line.decode("utf8")

        # Find the difficulty of the problem
        if state == START:
            difficulty = re.search("title=\"Difficulty\"", line)
            if difficulty:
                # The difficulty always follows the line containing "title="Difficulty""
                # So set the state to DIFFICULTY
                state = DIFFICULTY
                continue

        if state == DIFFICULTY:  # write the difficulty
            url_info["difficulty"] = line
            state = PROBLEM
            continue

        if state == PROBLEM:
            # Find the problem statement and name
            problem_line = re.search("class=\"problem-statement\".*", line)
            if problem_line:
                # get the problem statement
                url_info["problem"] = get_problem_statement(problem_line.group(0))

                # The name is also on this line, so get that too
                url_info["name"] = get_name(line)
                
                state = EXAMPLE

        if state == EXAMPLE:
            # Find the examples. This can be on one line or can be on multiple
            # so we also need to determine that.
            sample_input = re.search("<div class=\"sample-tests\".*", line)
            if sample_input:
                multiline_input = is_multiline_input(sample_input.group(0))
                first_input = get_sample_input(sample_input.group(0))
                url_info["examples"] = first_input
                state = NOTE
                if multiline_input:
                    continue

        if state == NOTE:
            # Now we are doing two things. If there are multiple lines of input, we want to write all of them
            # into examples.
            # We also want to get nay notes which may be there.
            
            if multiline_input:               
                # If we see the note or a <script> tag, we need to stop looping.

                # Is the note on this line?
                note_line = re.search("<div class=\"section-title\">Note.*", line)
                if note_line:  
                    url_info["note"] = note_line.group(0)
                    break 
                
                # Is the <script> tag on this line?
                script_line = re.search("<script>", line)
                if script_line:
                    break

                # Otherwise it is sample test data, so add it onto the examples.
                url_info["examples"] += line
                
            else:
                # We know that for a single line input, the note is on the same line, so just add
                # it on (if it exists).
                note_line = re.search("<div class=\"note\">.*", line)
                if note_line:
                    url_info["note"] = note_line.group(0)
                break

    return url_info
            

if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/110/A"
    dict = get_html_data(url)
    print(dict["name"])
