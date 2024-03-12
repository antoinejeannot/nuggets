.PHONY: install html pdf tests index

install:
	pip install -r requirements.txt

html:
	@ sh bin/build_html.sh

index:
	@ sh bin/build_index.sh

pdf:
	@ sh bin/build_pdf.sh

tests:
	@ python bin/extract_tests.py
	@ pytest
