#!/usr/bin/env python3

import urllib.request
import re


def get_problem_statement(line: str) -> None:
    problem_statement = re.search("<div>.*</div>", line)
    if problem_statement:
        statement = problem_statement.group(0)
        return statement
    else:
        raise Exception("Could not find problem statement")


def get_name(line: str) -> None:
    name = re.search("<div class=\"title\">.+?</div>", line)
    if name:
        return name.group(0)


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

        # Find the problem statement and name
        if state == PROBLEM:
            # see if the problem and input are both on this line.
            
            problem_line = re.search("class=\"problem-statement\"", line)
            if problem_line:
                url_info["problem"] = get_problem_statement(line)
                url_info["name"] += get_name(line)
                state = EXAMPLES
                continue

        # Find Examples and Notes
        if state == EXAMPLES:
            r = re.search("<script>", line)   
            if r:  # when it finds <script>, stop looking. We know we have found the examples and notes
                break
            url_info["examples"] += "\n"+line
    
    return url_info
            

if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/1/A"
    get_url_info(url)

