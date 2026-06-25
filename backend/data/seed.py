from database import Base
from database import engine
from database import SessionLocal

from models.customer import Customer
from models.order import Order

Base.metadata.create_all(bind=engine)

db = SessionLocal()

customers = [

    Customer(
        customer_id="C001",
        name="John Doe",
        refund_count=1
    ),

    Customer(
        customer_id="C002",
        name="Sarah Kim",
        refund_count=4
    ),

    Customer(
        customer_id="C003",
        name="Alex Brown",
        refund_count=0
    )

]

orders = [

    Order(
        order_id="ORD1001",
        customer_id="C001",
        category="Electronics",
        delivered_date="2026-06-01",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1002",
        customer_id="C002",
        category="Clothing",
        delivered_date="2026-06-10",
        opened=False,
        damaged=False
    ),

    Order(
        order_id="ORD1003",
        customer_id="C003",
        category="Electronics",
        delivered_date="2026-06-12",
        opened=False,
        damaged=True
    )

]

db.add_all(customers)
db.add_all(orders)

db.commit()

db.close()

print("Seed Complete")