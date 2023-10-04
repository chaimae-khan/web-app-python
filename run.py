from app import create_app, db  # app/__init__ (ROOT PACKAGE)
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        #if not User.query.filter_by(first__name='harry').first():
        #    User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    flask_app.run(host='0.0.0.0',debug=True)


