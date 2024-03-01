.PHONY: install html pdf tests

install:
	pip install -r requirements.txt

html:
	@ sh bin/build_html.sh

pdf:
	@ sh bin/build_pdf.sh

tests:
	@ python bin/extract_tests.py
	@ pytest
