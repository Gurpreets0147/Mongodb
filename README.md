https://www.mongodb.com/docs/drivers/pymongo/
python -m pip install 'pymongo[srv]'

python -m venv .venv
set-executionpolicy remotesigned
pip install -r .\requirements.txt
pip freeze > requirements.txt
