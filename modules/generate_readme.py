#import getURLInfo as gui, formatProblemStatement as fps, formatExample as fe, formatName as fn
from .get_url_info import get_url_info
from .format_problem import format_problem_statement
from .format_example import format_example
from .format_name import format_name
import os

def gen_readme(url:str, filename="README.md"):
    problem_file = "problem.md"
    example_file = "examples.md"
    name_file = "name.md"
    
    get_url_info(url, problem_file, example_file, name_file)
    format_problem_statement(problem_file)
    format_example(example_file)
    format_name(name_file)

    problem = ""
    with open(problem_file, "r") as f:
        problem = f.read()

    examples = ""
    with open(example_file, "r") as f:
        examples = f.read()

    name = ""
    with open(name_file, "r") as f:
        name = f.read()

    with open(filename, "w") as f:
        f.write(name+"\n")
        f.write("- [Problem](#problem)\n")
        f.write("- [Solution](#solution)\n\n")        
        
        f.write("## Problem\n")
        f.write(f"[Problem Link]({url})  \n\n")
        f.write(problem+"\n\n")
        f.write(examples)

        f.write("\n\n\n## Solution\n\n")

    os.remove(problem_file)
    os.remove(example_file)
    os.remove(name_file)



if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/1694/A"
    gen_readme(url)
