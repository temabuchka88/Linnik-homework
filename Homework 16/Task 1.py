from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, select, text
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20))
    orders = relationship("Orders", back_populates="client")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, autoincrement=True, primary_key=True)
    cost = Column(Integer)
    name = Column(String(20))
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Clients", back_populates="orders")

    def __init__(self, cost, name, client_id):
        self.cost = cost
        self.name = name
        self.client_id = client_id

    def __str__(self):
        return f"{self.name} {self.cost}"

    def __repr__(self):
        return f"{self.name} {self.cost}"


connection_string = "sqlite:///hw16.sqlite"
engine = create_engine(connection_string)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# artem = Clients("Artem")
# volodya = Clients("Volodya")
# egor = Clients("Egor")
# lesha = Clients("Lesha")
# session.add_all([artem, volodya, egor, lesha])
# session.commit()

# order_1 = Orders(7.99, "Chefwave Electric Milk Frother With Stand", 1)
# order_2 = Orders(9.99, "YEVIOR Clip on Strainer for Pots", 2)
# order_3 = Orders(5.99, "Joseph Jospeh Adjustable Measuring Spoon", 3)
# order_4 = Orders(7.99, "Olanly Memory Foam Bath Mat", 4)
# order_5 = Orders(9.95, "Jade Leaf Matcha Powder", 4)
# order_6 = Orders(5.99, "Urbana Exfoliating Gloves", 3)
# order_7 = Orders(9.22, "KitchenIQ 50009 Edge Grip 2-Stage Knife Sharpener", 2)
# order_8 = Orders(9.99, "Manhattan Toy Winkel Rattle & Sensory Teether Toy", 1)
# order_9 = Orders(9.95, "Quick & Clean Keurig Cleaning Pods", 3)
# order_10 = Orders(
#     6.95, "Hiware Window Blind Cleaner Duster Brush with 5 Microfiber Sleeves", 4
# )
# session.add_all(
#     [
#         order_1,
#         order_2,
#         order_3,
#         order_4,
#         order_5,
#         order_6,
#         order_7,
#         order_8,
#         order_9,
#         order_10,
#     ]
# )
# session.commit()

# clients = session.query(Clients).all()
# for client in clients:
#     print(f"Client ID: {client.id}, client name: {client.name}")
#     for order in client.orders:
#         print(f"Order name: {order.name} order prise: {order.cost}")

# session.close()

connection_string = "sqlite:///hw16.sqlite"
engine = create_engine(connection_string)
connection = engine.connect()

query_1 = connection.execute(
    text(
        "SELECT clients.name AS client_name, orders.name AS order_name, orders.cost AS order_cost FROM clients JOIN orders on clients.id = orders.client_id"
    )
)
for row in query_1.mappings():
    client_name = row["client_name"]
    order_name = row["order_name"]
    order_cost = row["order_cost"]
    print(
        f"Client Name: {client_name}\nOrder name: {order_name}\nOrder prise: {order_cost}"
    )

connection.close()
