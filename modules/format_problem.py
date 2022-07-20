import re
from .regex_convert import convert_latex, convert_random_specials, convert_tags

def format_problem_statement(statement: str) -> str:
    '''
    Format the problem statement.
    The problem statement is just a bunch of text with a bunch of html tags.
    So remove the html tags and put in the headers correctly.
    '''
    statement = convert_latex(statement)
    statement = convert_tags(statement)
    statement = convert_random_specials(statement)
    statement = re.sub("ExampleInput", "", statement)
    statement = re.sub("ExamplesInput", "", statement)
    statement = re.sub("\nOutput", "  \n### Output\n", statement)
    statement = re.sub("\nInput", "  \n### Input\n", statement)

    return statement.rstrip()


if __name__ == "__main__":
    format_problem_statement()
