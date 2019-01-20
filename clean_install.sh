rm -rf venv/
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py recreate-db && python manage.py seed-db