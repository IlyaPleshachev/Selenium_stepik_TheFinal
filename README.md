pip install -r requirements.txt 

Run Chrome browser tests

pytest -v

pytest -v --tb=line

pytest -v -s --tb=line --language=en

pytest -v --tb=line --language=en -m need_review

Run Firefox browser tests

pytest -v -s --tb=line --browser_name=firefox --language=en
