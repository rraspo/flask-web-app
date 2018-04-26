# flask-web-app
Repository for a Flask CRUD web application

## Non-functional requirements
This project uses MySQL database engine, so make sure to have it installed or within a docker container to be able to run this project fully.

## Installing 

First clone the repository, cd into it, create a virtual environment, activate it and install the requirements.

```bash
git clone https://github.com/rraspo/flask-web-app
cd flask-web-app
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, you will need to udpate `instance/config.py` with your credentials. There's an `instance.example` folder, rename it to `instance` and copy your database connection string into `config.py`. 

You can replace the following script with your credentials to properly create a MySQL connection string for SQLAlchemy. 

```bash
mv instance.example instance
DB_USER="my_db_user"
DB_PASS="my_db_password"
DB_HOST="my_db_host"
DB_NAME="my_db_name"
CONN_STRING="mysql://$DB_USER:$DB_PASS@$DB_HOST/$DB_NAME"
echo "SQLALCHEMY_DATABASE_URI = '$CONN_STRING'" > instance/config.py
```

## Running migrations

Now, we need to run our migrations, make sure that the user has privileges for the database you chose for this project.

```bash
export FLASK_APP=run.py
export FLASK_CONFIG=development
flask db init
flask db migrate
flask db upgrade
```

## You're all set
Application should work now, go ahead and run it.
```bash
flask run
```

## Running tests
To run the tests included in this project, use the following command.
```bash
python tests.py
```
