from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql+psycopg://postgres:postgres@db:5432/postgres'
)
db = SQLAlchemy(app)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/')
def home():
    return "Hello from my DevOps project! Running in Docker."

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/visits')
def visits():
    with app.app_context():
        record = Visit.query.first()
        if record is None:
            record = Visit(count=1)
            db.session.add(record)
        else:
            record.count += 1
        db.session.commit()
        return {"total_visits": record.count}

@app.route('/init-db')
def init_db():
    with app.app_context():
        db.create_all()
    return {"status": "database initialized"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
