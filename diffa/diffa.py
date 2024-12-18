import os

import difflib
import argparse


def generate_diff_html(file1_path, file2_path, side_by_side=False):
    # Read files
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    # Generate a unified diff between the files (whole lines only, no character-level diffs)
    diff = difflib.unified_diff(
        file1_lines, file2_lines, fromfile="File 1", tofile="File 2", lineterm=""
    )

    # Initialize HTML structure for diff tables
    if side_by_side:
        # Side-by-side layout
        diff_table = '<table class="diff" style="width: 100%;">'
        diff_table += f"<tr><th>{file1_path}</th><th>{file2_path}</th></tr>"
        for line in diff:
            if line.startswith("---") or line.startswith("+++"):
                continue  # Skip file header lines
            elif line.startswith("-"):
                diff_table += f'<tr><td class="diff_sub">{line[1:]}</td><td></td></tr>'  # Lines only in file 1
            elif line.startswith("+"):
                diff_table += f'<tr><td></td><td class="diff_add">{line[1:]}</td></tr>'  # Lines only in file 2
            else:
                diff_table += f'<tr><td class="diff_next">{line}</td><td class="diff_next">{line}</td></tr>'  # Matching lines
        diff_table += "</table>"
    else:
        # One-column layout
        diff_table = '<table class="diff">'
        for line in diff:
            if line.startswith("---") or line.startswith("+++"):
                continue  # Skip file header lines
            elif line.startswith("-"):
                diff_table += f'<tr><td class="diff_sub">{line[1:]}</td></tr>'  # Lines only in file 1
            elif line.startswith("+"):
                diff_table += f'<tr><td class="diff_add">{line[1:]}</td></tr>'  # Lines only in file 2
            else:
                diff_table += (
                    f'<tr><td class="diff_next">{line}</td></tr>'  # Matching lines
                )
        diff_table += "</table>"

    # Add custom JS/CSS for interaction (simple hover highlight)
    custom_html = f"""
    <html>
    <head>
        <title>Interactive Diff</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table.diff {{ width: 100%; border-collapse: collapse; }}
            .diff_header {{ background-color: #f0f0f0; font-weight: bold; }}
            .diff_next {{ background-color: #f9f9f9; }}
            .highlight {{ background-color: #ffff99 !important; }}
            .diff_add {{ background-color: #d4fcbc; }}
            .diff_chg {{ background-color: #fff5b1; }}
            .diff_sub {{ background-color: #fbb6c2; }}
            .diff td {{ padding: 4px; white-space: pre-wrap; }}
            /* Side-by-side view styling */
            .side-by-side td {{
                width: 50%;
                vertical-align: top;
                padding: 8px;
            }}
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', () => {{
                let rows = document.querySelectorAll('.diff tbody tr');
                rows.forEach(row => {{
                    row.addEventListener('mouseover', () => {{
                        row.classList.add('highlight');
                    }});
                    row.addEventListener('mouseout', () => {{
                        row.classList.remove('highlight');
                    }});
                }});
            }});
        </script>
    </head>
    <body>
        <h1>Side-by-Side Diff</h1>
        <div class="side-by-side">
            {diff_table}
        </div>
    </body>
    </html>
    """

    return custom_html


def main():
    parser = argparse.ArgumentParser(
        description="Generate a simple HTML diff of two files."
    )
    parser.add_argument("file1", help="Path to the first input file.")
    parser.add_argument("file2", help="Path to the second input file.")
    parser.add_argument("output", help="Path to save the output HTML file.")
    parser.add_argument(
        "--side-by-side",
        action="store_true",
        help="Display diff in a side-by-side view.",
    )

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
        args.file1, args.file2, side_by_side=args.side_by_side
    )

    # Write to output HTML file
    with open(args.output, "w") as output_file:
        output_file.write(diff_html)
    print(f"Interactive diff saved to {os.path.abspath(args.output)}")


if __name__ == "__main__":
    main()
