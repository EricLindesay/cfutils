import re, regex_convert

def format_problem_statement(filename="problem.md"):
    statement = ""
    with open(filename, "r") as f:
        statement = f.read()

    statement = regex_convert.convert_latex(statement)
    statement = regex_convert.convert_tags(statement)
    statement = regex_convert.convert_random_specials(statement)
    statement = re.sub("ExampleInput", "", statement)
    statement = re.sub("ExamplesInput", "", statement)
    statement = re.sub("\nOutput", "  \n### Output\n", statement)
    statement = re.sub("\nInput", "  \n### Input\n", statement)

    with open(filename, "w") as f:
        f.write(statement.rstrip())


if __name__ == "__main__":
    format_problem_statement()
