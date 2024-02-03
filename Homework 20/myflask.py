from flask import Flask, render_template, request, make_response, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import (
    Orders,
    create_client,
    get_clients,
    create_order,
    get_orders,
    delete_order,
)

app = Flask(__name__)

engine = create_engine("sqlite:///db/hw20.sqlite")
Session = sessionmaker(bind=engine)
session = Session()


@app.route("/")
def index():
    return render_template("nav.html")


@app.route("/clients", methods=["GET", "POST"])
def new_client():
    if request.method == "POST":
        client_name = request.form.get("name")
        if not client_name:
            return make_response("Name cannot be empty!", 400)
        create_client(client_name)
        return redirect("/clients")

    clients = get_clients()
    return render_template("clients.html", clients=clients)


@app.route("/orders", methods=["GET", "POST", "DELETE"])
def new_order():
    if request.method == "GET":
        spis_orders = get_orders()
        return render_template("orders.html", orders=spis_orders)
    if request.method == "POST":
        create_order(
            cost=request.form.get("cost"),
            name=request.form.get("name"),
            client_id=request.form.get("client_id"),
        )
        return redirect("/orders")


@app.route("/orders/<id>", methods=["DELETE"])
def delete_my_order(id):
    delete_order(int(id))
    return redirect("/orders")


@app.route("/updateorders/<id>", methods=["GET"])
def asd():
    order = get_orders(id)
    return render_template("updateorders.html", order=order)


if __name__ == "__main__":
    app.run()
