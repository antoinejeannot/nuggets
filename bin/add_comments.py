import sys

from bs4 import BeautifulSoup


def add_comments(html_doc: str) -> str:
    # Parse the HTML
    soup = BeautifulSoup(html_doc, "html.parser")
    # Create the new <link> and <script> elements
    separator = soup.new_tag("hr")
    script = soup.new_tag(
        "script",
        **{
            "src": "https://giscus.app/client.js",
            "data-repo": "antoinejeannot/nuggets",
            "data-repo-id": "R_kgDOLObhkQ",
            "data-category": "Announcements",
            "data-category-id": "DIC_kwDOLObhkc4Cd6p8",
            "data-mapping": "title",
            "data-strict": "0",
            "data-reactions-enabled": "1",
            "data-emit-metadata": "0",
            "data-input-position": "top",
            "data-theme": "noborder_light",
            "data-lang": "en",
            "crossorigin": "anonymous",
            "async": "",
        }
    )

    # Append the new elements to the <body> section
    soup.body.append(separator)
    soup.body.append(script)
    return soup.prettify()


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        html_doc = file.read()
    with open(sys.argv[1], "w") as file:
        file.write(add_comments(html_doc))
