Create a virtual environment and install behave and selenium to execute.

pip install behave
pip install selenium
pip install selenium-wire
pip install allure-behave

Finally, Execute this with following command:

$  behave -f allure_behave.formatter:AllureFormatter -o reportTest features

$ allure serve reportTest

report will be generated to C:\Users\shail\AppData\Local\Temp\3609749911560213999\allure-report

pip install -r requirement.txt