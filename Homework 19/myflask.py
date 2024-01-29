from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Orders

app = Flask(__name__)

engine = create_engine("sqlite:///db/hw19.sqlite")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    orders = session.query(Orders).all()

    return render_template("orders.html", orders=orders)


if __name__ == "__main__":
    app.run()
