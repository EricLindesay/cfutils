from .get_html_data import get_html_data
from .format_problem import format_problem_statement
from .format_example import format_example
from .format_note import format_note
from .format_name import format_name, format_difficulty
import re



def gen_readme(url:str, filename="README.md"):
    url_info = get_html_data(url)
    url_info["name"] = format_name(url_info["name"])
    url_info["difficulty"] = format_difficulty(url_info["difficulty"])
    url_info["problem"] = format_problem_statement(url_info["problem"])
    url_info["examples"] = format_example(url_info["examples"])
    url_info["note"] = format_note(url_info["note"])
   
    with open(filename, "w") as f:
        f.write(f"# {url_info['name']} - {url_info['difficulty']}\n")
        f.write("- [Problem](#problem)\n")
        f.write("- [Solution](#solution)\n\n")
        
        f.write("## Problem\n")
        f.write(f"[Problem Link]({url})  \n\n")
        f.write(url_info["problem"]+"\n\n")
        f.write(url_info["examples"])
        f.write(url_info["note"])

        f.write("\n\n\n-----\n## Solution\n\n")



if __name__ == "__main__":
    url = "https://codeforces.com/problemset/problem/1694/A"
    gen_readme(url)
