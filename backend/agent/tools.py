from langchain_core.tools import tool
from sqlalchemy.orm import Session
from database import SessionLocal
from models.customer import Customer
from models.order import Order
from rag.vector_store import load_vectorstore

@tool
def get_customer(customer_id: str):
    """
    Retrieve customer profile.
    """

    db: Session = SessionLocal()

    customer = (
        db.query(Customer)
        .filter(
            Customer.customer_id == customer_id
        )
        .first()
    )

    db.close()

    if not customer:
        return "Customer not found"

    return {
        "customer_id": customer.customer_id,
        "name": customer.name,
        "refund_count": customer.refund_count
    }


@tool
def get_order(order_id: str):
    """
    Retrieve order details.
    """

    db: Session = SessionLocal()

    order = (
        db.query(Order)
        .filter(
            Order.order_id == order_id
        )
        .first()
    )

    db.close()

    if not order:
        return "Order not found"

    return {
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "category": order.category,
        "delivered_date": order.delivered_date,
        "opened": order.opened,
        "damaged": order.damaged
    }


@tool
def retrieve_policy(query: str):
    """
    Search refund policy.
    """

    vectorstore = load_vectorstore()

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


@tool
def process_refund(order_id: str):
    """
    Process refund.
    """

    return (
        f"Refund initiated for "
        f"{order_id}"
    )