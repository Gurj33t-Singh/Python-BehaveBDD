# eGovDigit

## Execute behave using
`behave --no-capture /feature_file_path --tags=tag_name1,tag_name2 -f allure_behave.formatter:AllureFormatter -o ~/report_json_directory_path`

- `--no-capture` flag to print logs in console 
- `--no-capture-stderr` flag to print errors in console
- `-f allure_behave.formatter:AllureFormatter` flag to generate report in allure format class (creates report in JSON file)

https://github.com/allure-framework/allure2/releases Download allure2 to view reports in HTML

- `allure generate ~/path_to_JSON_report --clean -o ~/path_to_HTML_report` 
- `allure generate reports --clean -o reports_html` example 
- `allure open ./reports_html/` open reports locally from html files 

## For preparing payload:
following two are mandatory to declare in method:
- context.req_header={}
- context.req_param={}

when storing payload, use following variable names with 'context.' prefix 
- multipart_body
- payload_string

## PIP dependancy: 
|Package            |Version|
|-------------------|------|
|allure-behave         |2.13.2|
|allure-python-commons |2.13.2|
|attrs                 |23.2.0|
|behave             |1.2.6|
|certifi            |2024.2.2|
|charset-normalizer |3.3.2|
|idna               |3.6|
|parse              |1.20.1|
|parse-type         |0.6.2|
|pip                |23.3.1|
|requests           |2.31.0|
|requests-toolbelt  |1.0.0|
|setuptools         |68.2.2|
|six                |1.16.0|
|urllib3            |2.2.1|
|wheel              |0.41.2|

## Conda dependancy: 
install miniconda3 or anaconda environment manager
`conda env create --file=CondaEnv.yaml` to create conda environment from CondaEnv.yml of this project
`--name myEnv` add this flag to set your own environment name 
`conda activate egov` to activate this environment