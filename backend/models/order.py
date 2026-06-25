from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean

from database import Base


class Order(Base):

    __tablename__ = "orders"

    order_id = Column(
        String,
        primary_key=True
    )

    customer_id = Column(String)

    category = Column(String)

    delivered_date = Column(String)

    opened = Column(Boolean)

    damaged = Column(Boolean)