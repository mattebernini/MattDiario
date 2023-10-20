from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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

# frontend

def get_diary_pages_json(diary_entries):
    diary_pages = []
    
    for entry in diary_entries:
        diary_pages.append({
            'title': entry.title,
            'category': entry.category,
            'date': entry.date,
            'content': entry.content
        })
    return diary_pages

@app.route('/')
def index():
    categories = db.session.query(DiaryEntry.category, func.count(DiaryEntry.id)).group_by(DiaryEntry.category).all()  
    year_month = db.session.query(
        func.strftime("%Y-%m", DiaryEntry.date).label("year_month"),
        func.count(DiaryEntry.id)
    ).group_by("year_month").all() 
    return render_template('index.html',
                           categories=categories,
                           year_month=year_month)

@app.route('/pagina/<quale>')
def pagina(quale):
    if quale == "ultima":
        diary_entries = DiaryEntry.query.all()
    else:
        tipo, val = quale.split("=")
        if tipo == "category":
            diary_entries = DiaryEntry.query.filter_by(category=val).all()
        elif tipo == "year_month":
            diary_entries = DiaryEntry.query.filter(DiaryEntry.date.like(f"{val}%")).all()

    return render_template('pagina.html', 
                           diary_pages=get_diary_pages_json(diary_entries))

@app.route('/delete_category', methods=['GET', 'POST'])
def delete_category():
    if request.method == 'POST':
        category_to_delete = request.form.get('category')
        DiaryEntry.query.filter_by(category=category_to_delete).delete()
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/db_grezzo')
def db_grezzo():
    diary_pages = DiaryEntry.query.all()
    return render_template('db_grezzo.html', diary_pages=diary_pages)

if __name__ == '__main__':
    app.run(debug=True)
