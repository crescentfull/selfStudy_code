from app import db

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    from app import create_app
    app = create_app()
    setup_database(app)