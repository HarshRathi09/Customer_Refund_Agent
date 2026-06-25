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

        Customer(
        customer_id="C004",
        name="Richard Morris",
        refund_count=1
    ),

    Customer(
        customer_id="C005",
        name="Priya Sharma",
        refund_count=4
    ),

    Customer(
        customer_id="C006",
        name="Kim Jong",
        refund_count=0
    ),

     Customer(
        customer_id="C007",
        name="Alex Hales",
        refund_count=3
    ),

    Customer(
        customer_id="C008",
        name="Harry Cooper",
        refund_count=2
    ),

    Customer(
        customer_id="C009",
        name="M.Leornard",
        refund_count=0
    )

        Customer(
        customer_id="C0010",
        name="Rahul Desai",
        refund_count=1
    ),

    Customer(
        customer_id="C0011",
        name="Priya Sharma",
        refund_count=5
    ),

    Customer(
        customer_id="C0012",
        name="Ali",
        refund_count=2
    ), 
    Customer(
        customer_id="C0013",
        name="George Russel",
        refund_count=3
    ),

    Customer(
        customer_id="C0014",
        name=" Chris Lewis",
        refund_count=0
    ),

    Customer(
        customer_id="C0015",
        name="Rohith Verma",
        refund_count=0
    ),
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
    ),

        Order(
        order_id="ORD1004",
        customer_id="C004",
        category="Electronics",
        delivered_date="2026-06-30",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1005",
        customer_id="C005",
        category="Clothing",
        delivered_date="2026-06-15",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1006",
        customer_id="C006",
        category="Electronics",
        delivered_date="2026-06-18",
        opened=False,
        damaged=True
    ),
        Order(
        order_id="ORD1007",
        customer_id="C007",
        category="Furniture",
        delivered_date="2026-06-09",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1008",
        customer_id="C002",
        category="Clothing",
        delivered_date="2026-06-06",
        opened=True,
        damaged=True
    ),

    Order(
        order_id="ORD1009",
        customer_id="C009",
        category="Electronics",
        delivered_date="2026-06-14",
        opened=False,
        damaged=False
    ),

        Order(
        order_id="ORD10",
        customer_id="C010",
        category="Electronics",
        delivered_date="2026-06-24",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1010",
        customer_id="C002",
        category="Clothing",
        delivered_date="2026-09-02",
        opened=False,
        damaged=True
    ),

    Order(
        order_id="ORD1011",
        customer_id="C003",
        category="Clothing",
        delivered_date="2026-02-11",
        opened=False,
        damaged=True
    ),

        Order(
        order_id="ORD12",
        customer_id="C001",
        category="Electronics",
        delivered_date="2026-05-01",
        opened=True,
        damaged=False
    ),

    Order(
        order_id="ORD1013",
        customer_id="C002",
        category="Clothing",
        delivered_date="2026-06-10",
        opened=False,
        damaged=False
    ),

    Order(
        order_id="ORD1014",
        customer_id="C003",
        category="Electronics",
        delivered_date="2026-06-12",
        opened=True,
        damaged=True
    ),

     Order(
        order_id="ORD1015",
        customer_id="C003",
        category="Furniture",
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
