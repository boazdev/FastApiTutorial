activate the virtual environment with:
venv/Scripts/activate
#update pip version in the venv
<--
python -m pip install --upgrade pip
start the uvicorn server that runs the fastApi app:
uvicorn main:app --reload
fix import not showing :ctrl shift P
select python interpreter from scripts: python.exe