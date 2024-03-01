import sys

from bs4 import BeautifulSoup


def collapse_details(html_doc: str) -> str:
    # Parse the HTML
    soup = BeautifulSoup(html_doc, "html.parser")

    # Use the function to find all <h4> tags with ids starting with "more-details"
    more_details_tags = soup.find_all(
        lambda tag: tag.name == "h4"
        and tag.has_attr("id")
        and tag["id"].startswith("more-details")
    )
    for h4_tag in more_details_tags:
        # Create a new <details> tag
        details_tag = soup.new_tag("details")

        # Create a new <summary> tag and add it inside <details>
        summary_tag = soup.new_tag("summary")
        summary_tag.string = h4_tag.text
        details_tag.append(summary_tag)

        # Move all tags that happen before the next <hr> into the <details> section
        next_sibling = h4_tag.find_next_sibling()
        while next_sibling and next_sibling.name != "hr":
            # Keep a reference to the next sibling because moving will change the current sibling
            current_sibling = next_sibling
            next_sibling = current_sibling.find_next_sibling()
            # Move the current sibling into <details>
            details_tag.append(current_sibling)
        # Replace the <h4> tag with <details>
        h4_tag.replace_with(details_tag)
    return soup.prettify()


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        html_doc = file.read()
    with open(sys.argv[1], "w") as file:
        file.write(collapse_details(html_doc))
