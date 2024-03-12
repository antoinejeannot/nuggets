import sys

from bs4 import BeautifulSoup


def add_analytics(html_doc: str, filename: str) -> str:
    # Parse the HTML
    soup = BeautifulSoup(html_doc, "html.parser")
    # Create the new <link> and <script> elements
    link = soup.new_tag(
        "link",
        rel="canonical",
        href=filename,
    )
    script = soup.new_tag(
        "script",
        **{
            "data-goatcounter": "https://ajeannot.goatcounter.com/count",
            "async": "",
            "src": "//gc.zgo.at/count.js",
        }
    )
    # Append the new elements to the <head> section
    soup.head.append(link)
    soup.head.append(script)
    return soup.prettify()


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        html_doc = file.read()
    with open(sys.argv[1], "w") as file:
        file.write(add_analytics(html_doc, sys.argv[2]))
