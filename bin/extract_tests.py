import glob
import os
import re


def generate_python_tests(filename, mk_doc):
    test_template = """
def test_{filename}():
{code_blocks}
""".strip()
    # Regex to find Python code blocks
    python_code_blocks = re.findall(r"```python\n(.*?)\n```", mk_doc, re.DOTALL)
    python_code_blocks = [
        block.strip() for block in python_code_blocks if "# skip test" not in block
    ]
    python_code = "\n\n".join(
        (
            "\n".join(f"\t{line}" for line in code_block.split("\n"))
            for code_block in python_code_blocks
        )
    )
    return test_template.format(filename=filename, code_blocks=python_code)


if __name__ == "__main__":
    for mkdoc_filepath in glob.glob("markdown/*.md"):
        filename, _ = os.path.splitext(os.path.basename(mkdoc_filepath))
        with open(mkdoc_filepath, "r") as f:
            mk_doc = f.read()
        tests = generate_python_tests(filename, mk_doc)
        os.makedirs("tests", exist_ok=True)
        with open(os.path.join("tests", f"test_{filename}.py"), "w") as f:
            f.write(tests)
