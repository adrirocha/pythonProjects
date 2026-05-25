from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)

class Book(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form["book_name"]
        book_author = request.form["book_author"]
        book_rating = request.form["book_rating"]
        
        with app.app_context():
            book = Book(
                title = book_name,
                author = book_author,
                rating = book_rating
            )
            db.session.add(book)
            db.session.commit()
        
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    book = db.get_or_404(Book, id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", book=book)

@app.route("/delete/<id>")
def delete(id):
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
