import re


def format_name(filename="name.md"):
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()

    difficulty = re.search("\d+", lines[0]).group(0)  # search for the digits
    name = lines[1][22:-6]
    print(f"{name} - {difficulty}")
    with open(filename, "w") as f:
        f.write(f"# {name} - {difficulty}")


if __name__ == "__main__":
    format_name()
