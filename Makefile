all: run

run:
	pipenv run python ./convertXMLtoCSV.py

shell:
	pipenv run python