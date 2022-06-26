#import getURLInfo as gui, formatProblemStatement as fps, formatExample as fe, formatName as fn
from .get_url_info import get_url_info
from .format_problem import format_problem_statement
from .format_example import format_example
from .format_name import format_name
import os

def gen_readme(url:str, filename="README.md"):
    url_info = get_url_info(url)
    url_info["name"] = format_name(url_info["name"])
    url_info["problem"] = format_problem_statement(url_info["problem"])
    url_info["examples"] = format_example(url_info["examples"])
   
    with open(filename, "w") as f:
        f.write(url_info["name"]+"\n")
        f.write("- [Problem](#problem)\n")
        f.write("- [Solution](#solution)\n\n")        
        
        f.write("## Problem\n")
        f.write(f"[Problem Link]({url})  \n\n")
        f.write(url_info["problem"]+"\n\n")
        f.write(url_info["examples"])

        f.write("\n\n\n## Solution\n\n")



if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/1694/A"
    gen_readme(url)
