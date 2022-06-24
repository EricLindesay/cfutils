#!/usr/bin/env python3

import urllib.request
import re

def write_problem_statement(line: str, problem_statement_file: str) -> None:
    problem_statement = re.search("<div>.*</div>", line)
    if problem_statement:
        statement = problem_statement.group(0)
        with open(problem_statement_file, "w") as f:
            f.write(statement)
    else:
        raise Exception("Could not find problem statement")


def write_name(line: str, name_file: str) -> None:
    name = re.search("<div class=\"title\">.+?</div>", line)
    if name:
        with open(name_file, "a") as f:
            f.write(name.group(0))


def get_url_info(url, problem_statement_file="problem.md", examples_file="examples.md", name_file="name.md"):
    fp = urllib.request.urlopen(url)

    with open(examples_file, "w") as f:  # clear the examples file
        f.write("")

    #with open("test.md", "w") as f:
    #    f.write(fp.read().decode("utf8"))

    found_problem_statement = False
    found_difficulty_tag = False
    for line in fp.readlines():
        line = line.decode("utf8")

        # Find the difficulty tag
        difficulty = re.search("title=\"Difficulty\"", line)
        if difficulty:
            found_difficulty_tag = True  # the next line will be the difficulty
            continue

        if found_difficulty_tag:
            found_difficulty_tag = False
            with open(name_file, "w") as f:
                f.write(line)

        # Find the problem statement and name
        if not found_problem_statement:
            problem_line = re.search("class=\"problem-statement\"", line)
            if problem_line:
                write_problem_statement(line, problem_statement_file)
                write_name(line, name_file)
                found_problem_statement = True
                continue

        # Find Examples and Notes
        if found_problem_statement:
            r = re.search("<script>", line)   
            if r:  # when it finds <script>, stop looking. We know we have found the examples and notes
                break
            with open(examples_file, "a") as f:
                f.write(line)
        

if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/1694/B"
    get_url_info(url)

