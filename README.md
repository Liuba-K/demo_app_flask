1. Create new virtual env
python3 -m venv ./venv
2. copy example.env to .env and set SECRET_KEY
3. activate virtual env
source venv/bin/activate
4. install dependencies
pip install -r requirements.txt
5. Run command for init db and create user
flask db upgrade
flask create-init-user
flask create-init-tags
6. Run flask application
flask run

