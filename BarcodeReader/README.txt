'''
Create a run.sh file with the following lines
'''

py -3 -m venv barcodereader_venv
source barcodereader_venv/Scripts/activate
pip install -r requirements.txt

export FLASK_APP=app.py
flask run
