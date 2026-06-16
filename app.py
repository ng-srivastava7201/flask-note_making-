from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Notes(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable=False)
  date_created = db.Column(db.DateTime, default=db.func.now())

  def __repr__():
    return '<Task %r>' %self.id

@app.route('/', methods=["GET", "POST"])
def index():
  if request.method=="POST":
    note_content = request.form['content']
    new_task = Notes(content=note_content)
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except:
      return 'there was some error'
  else:
    notes = Notes.query.order_by(date_created).all()
    return render_template('index.html', notes=notes)

with app.app_context():
  db.create_all()
  
if __name__ == '__main__':
  app.run(debug=True)
