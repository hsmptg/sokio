sokio (Flask-SocketIO test)
===========================

Installation of requirements
----------------------------

    pip install -r requirements.txt

Creation of the sqlite database
----------------------------

    python manage.py shell

    from app import db
    db.drop_all()
    db.create_all()
    exit()

Running the application
-----------------------

    python manage.py run
