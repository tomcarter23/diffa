import os
import argparse
from jinja2 import Template


import difflib


def generate_diff_html(file1_path, file2_path):
    # Read files
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    # Generate a unified diff between the files (whole lines only, no character-level diffs)
    diff = difflib.unified_diff(
        file1_lines, file2_lines, fromfile="File 1", tofile="File 2", lineterm=""
    )

    with open("diffa/templates/basic_template.html") as file_:
        template = Template(file_.read())

    template_data = {
        "file1_path": file1_path,
        "file2_path": file2_path,
    }

    diff_counter = tuple[str, str]
    diff_lines: list[tuple[str, str]] = []

    # Initialize HTML structure for diff tables
    for line in diff:
        if line.startswith("---") or line.startswith("+++"):
            continue  # Skip file header lines
        elif line.startswith("-"):
            diff_lines.append((line[1:], ""))
        elif line.startswith("+"):
            diff_lines.append(("", line[1:]))
        else:
            diff_counter = (line, line)

    template_data["diff_lines"] = diff_lines
    template_data["diff_counter"] = diff_counter

    return template.render(template_data)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a simple HTML diff of two files."
    )
    parser.add_argument("file1", help="Path to the first input file.")
    parser.add_argument("file2", help="Path to the second input file.")
    parser.add_argument("output", help="Path to save the output HTML file.")

    args = parser.parse_args()

    # Validate input files
    if not os.path.isfile(args.file1):
        print(f"Error: File '{args.file1}' does not exist.")
        return
    if not os.path.isfile(args.file2):
        print(f"Error: File '{args.file2}' does not exist.")
        return

    # Generate HTML diff
    diff_html = generate_diff_html(
        args.file1, args.file2
    )

    # Write to output HTML file
    with open(args.output, "w") as output_file:
        output_file.write(diff_html)
    print(f"Interactive diff saved to {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
