"""
@Acknowledgement: This script and the whole workflow are
inspired by the awesome work at https://github.com/tw93/tw93
"""
import requests
import re
from pathlib import Path


CODE_TIME = "https://gist.githubusercontent.com/rexwangcc/6a3a391c000e418240e4c512642aeac0/raw/"
root = Path(__file__).parent.resolve()
README = root / "README.md"


def replace_text(text, replacement, identifier) -> str:
    r = re.compile(
        fr"<!\-\- {identifier} starts \-\->.*<!\-\- {identifier} ends \-\->", re.DOTALL
    )
    replacement = f"<!-- {identifier} starts -->\n{replacement}\n<!-- {identifier} ends -->"
    return r.sub(replacement, text)


def fetch_code_time() -> requests.Response:
    return requests.get(CODE_TIME)


def main():
    # read in self
    md = README.open("r").read()

    # watch out for side effects
    code_time_text = f"\n```text\n{fetch_code_time().text}\n```\n"
    md = replace_text(md, code_time_text, "code_time")
    print(md)


    # write back the updated contents to self
    README.open("w").write(md)

if __name__ == "__main__":
    main()
