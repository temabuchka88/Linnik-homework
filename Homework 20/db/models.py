from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    create_engine,
    select,
    text,
    update,
)
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


connection_string = "sqlite:///db/hw20.sqlite"
engine = create_engine(connection_string)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def get_orders():
    session = Session()
    stmt = session.execute(select(Orders))
    all_orders = stmt.scalars().all()
    session.close()
    return all_orders


def create_client(name):
    session = Session()
    new_client = Clients(name)
    session.add(new_client)
    session.commit()
    session.close()
    return new_client


def get_clients():
    session = Session()
    stmt = session.execute(select(Clients))
    all_clients = stmt.scalars().all()
    session.close()
    return all_clients


def create_order(cost, name, client_id):
    session = Session()
    new_order = Orders(cost, name, client_id)
    session.add(new_order)
    session.commit()
    session.close()
    return new_order


def delete_order(id):
    session = Session()
    for order in session.query(Orders):
        if id == order.id:
            session.delete(order)
    session.commit()
    session.close()


def update_order(id, cost, name, client_id):
    session = Session()
    get_id_order = session.get(Orders, id)
    get_id_order.cost = cost
    get_id_order.name = name
    get_id_order.client_id = client_id
    session.commit()
    session.close()
