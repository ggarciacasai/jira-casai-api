# jira-casai-api

Manage VENV
`https://docs.python.org/3/tutorial/venv.html`

install venv
python3 -m venv .venv

activate 
source .venv/bin/activate

select venv in vscode

install dependencies from requeriments.txt
python -m pip install -r requirements.txt


freeze dependencies
pip freeze -l > requirements.txt 


serve app 
python manage.py runserver
