from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date = db.Column(db.String(255))
    category = db.Column(db.String(255))
    content = db.Column(db.Text)

with app.app_context():
    db.create_all()


@app.route('/api/send', methods=['POST'])
def receive_page():
    data = request.get_json()
    print(data)
    entry = DiaryEntry(
        title=data['title'],
        date=data['date'],
        category=data['category'],
        content=data['content']
    )

    db.session.add(entry)
    db.session.commit()

    return jsonify(success=True)

@app.route('/')
def index():
    diary_pages = DiaryEntry.query.all()
    return render_template('db_data.html', diary_pages=diary_pages)

if __name__ == '__main__':
    app.run(debug=True)
