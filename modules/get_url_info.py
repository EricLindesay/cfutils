#!/usr/bin/env python3

from statistics import multimode
import urllib.request
import re


def copy_until(str1: str, end_pattern: str) -> str:
    pattern_limit = re.search(end_pattern, str1)
    if pattern_limit:
        end_ind = pattern_limit.span(0)[0]  # stop copying problem-statement when it gets to sample-tests part
    else:
        end_ind = len(str1)  # if sample-tests isn't on this line, just copy it all.
    return str1[:end_ind]        


def get_problem_statement(line: str) -> str:
    # start index = "standard output + 2 /divs"
    # end index = index of class=sample-tests
    
    problem_statement = re.search("standard output\ ?</div></div>.*", line)
    if problem_statement:
        statement = problem_statement.group(0)[27:]  #27 means you don't include the standard output div div section.
        return copy_until(statement, "<div class=\"sample-tests\"")
    else:
        raise Exception("Could not find problem statement")


def get_name(line: str) -> str:
    name = re.search("<div class=\"title\">.+?</div>", line)
    if name:
        return name.group(0)


def get_sample_tests(line: str) -> str:
    # does this line contain equal number of class="input" and class="output"?
    # YES then just copy the line
    # NO then we need to set the multiline flag thing saying how many you need left   
    multiline_input = line.count("class=\"input\"") - line.count("class=\"output\"")
    bool_return = bool(multiline_input)
    # we don't want to include the notes section if it exists. We are doing that elsewhere
    return copy_until(line, "<div class=\"note\">"), bool_return


def get_note(line: str) -> str:
    return line


def get_url_info(url) -> dict:
    url_info = {
        "problem": "",
        "examples": "",
        "name": "",
    }

    fp = urllib.request.urlopen(url)

    DIFF = 0
    NAME = 1
    PROBLEM = 2
    EXAMPLES = 3
    state = DIFF

    first_test = False
    multiline_input = False

    for line in fp.readlines():
        line = line.decode("utf8")

        # Find the difficulty tag
        if state == DIFF:
            difficulty = re.search("title=\"Difficulty\"", line)
            if difficulty:
                state = NAME  # the difficulty is on the next line
                continue

        if state == NAME:  # write the difficulty
            url_info["name"] = line

            state = PROBLEM
            continue


        # find problem-statement
        # find sample-test
        # find output
        # find note
        # create functions which get the required inputs
        # could just see if the line contains that class
        # if it does, call the function.
        # need to be able to tell in the function when it should end.


        # if state != NAME && state != DIFF

        # Find the problem statement
        problem_line = re.search("class=\"problem-statement\".*", line)
        if problem_line:
            # get the problem statement
            url_info["problem"] = get_problem_statement(problem_line.group(0))

            # The name is also on this line, so get that too
            url_info["name"] += get_name(line)
            # NOTE THERE IS NO CONTINUE

        # if you find an input, then until you find output, append everything. The input can be on multiple lines.

        # There can be multiple inputs and outputs. Even on the same line.
        sample_tests = re.search("<div class=\"sample-tests\".*", line)
        if sample_tests:
            # when we get to notes, we change this to false
            new_input, multiline_input = get_sample_tests(sample_tests.group(0))
            url_info["examples"] += new_input
            if multiline_input:
                continue
                # NOTE THERE IS A CONTINUE

        if multiline_input:
            # now we just want to copy all the lines of input until we see class="note"
            # if line contains note, add it to the examples and return.
            url_info["examples"] += line
            
            note_line = re.search("<div class=\"section-title\">Note", line)
            if note_line:  
                break  # we no longer need anything else
        else:
            note_line = re.search("<div class=\"note\">.*", line)
            if note_line:
                url_info["examples"] += get_note(note_line.group(0))

    return url_info
            

if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/110/A"
    get_url_info(url)
    

