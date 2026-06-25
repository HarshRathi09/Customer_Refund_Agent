from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

from database import Base


class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(
        String,
        primary_key=True
    )

    name = Column(String)

    refund_count = Column(Integer)