Installation
Use the package manager pip to install dependencies
pip install -r requirements.txt 
Downloading and installing Allure commandline application suitable for your environment
Usage
Run Chrome browser tests

pytest -v
pytest -v --tb=line
pytest -v -s --tb=line --language=en
pytest -v --tb=line --language=en -m need_review
Run Firefox browser tests

pytest -v -s --tb=line --browser_name=firefox --language=en
Run tests with execution reports Allure

pytest --alluredir name_dir_allure_result name_test
allure serve name_dir_allure_result # result of test  
