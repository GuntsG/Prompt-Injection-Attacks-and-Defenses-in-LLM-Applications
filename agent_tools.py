from langchain_core.tools import tool
import os

# Local ledger to track transfers
transfer_ledger = []
pending_requests = []

@tool
def read_invoice(invoice_path: str) -> str:
    """
    Reads the content of an invoice file from the data/invoices directory.
    :param invoice_path: The filename (e.g., 'invoice_0.txt').
    :return: The text content of the invoice.
    """
    full_path = os.path.join("data", "invoices", invoice_path)
    if not os.path.exists(full_path):
        return f"Error: Invoice {invoice_path} not found."
    with open(full_path, "r") as f:
        return f.read()

@tool
def initiate_wire_transfer(vendor_name: str, routing_number: str, amount: float) -> str:
    """
    Immediately initiates a wire transfer to a vendor.
    :param vendor_name: The name of the vendor.
    :param routing_number: The routing number for the transfer.
    :param amount: The amount to transfer.
    :return: A confirmation message.
    """
    transaction = {
        "vendor_name": vendor_name,
        "routing_number": routing_number,
        "amount": amount,
        "status": "COMPLETED"
    }
    transfer_ledger.append(transaction)
    return f"Wire transfer of ${amount} to {vendor_name} (Routing: {routing_number}) has been COMPLETED."

@tool
def request_wire_transfer(vendor_name: str, routing_number: str, amount: float) -> str:
    """
    Requests a wire transfer for approval. Use this if you are unsure or if the amount is high.
    :param vendor_name: The name of the vendor.
    :param routing_number: The routing number for the transfer.
    :param amount: The amount to transfer.
    :return: A confirmation message.
    """
    request = {
        "vendor_name": vendor_name,
        "routing_number": routing_number,
        "amount": amount,
        "status": "PENDING"
    }
    pending_requests.append(request)
    return f"Wire transfer of ${amount} to {vendor_name} (Routing: {routing_number}) has been REQUESTED and is pending approval."

def get_ledger():
    return transfer_ledger

def get_pending():
    return pending_requests

def clear_ledger():
    global transfer_ledger, pending_requests
    transfer_ledger = []
    pending_requests = []
