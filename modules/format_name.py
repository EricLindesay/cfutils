import re


def format_name(unformatted:str) -> str:
    lines = unformatted.split("\n")

    difficulty = re.search("\d+", lines[0]).group(0)  # search for the digits
    name = lines[1][22:-6]
    print(f"{name} - {difficulty}")

    return f"# {name} - {difficulty}"
    

if __name__ == "__main__":
    format_name()
