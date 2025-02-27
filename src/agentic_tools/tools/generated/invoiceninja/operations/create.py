from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import InvoiceninjaCredentials

class InvoiceninjaCreateToolInput(BaseModel):
    invoice_id: Optional[str] = Field(None, description="Invoice ID")
    invoice_items_ui: Optional[Dict[str, Any]] = Field(None, description="Invoice Items")
    contacts_ui: Optional[Dict[str, Any]] = Field(None, description="Contacts")
    time_logs_ui: Optional[Dict[str, Any]] = Field(None, description="Time Logs")
    expense_id: Optional[str] = Field(None, description="Expense ID")
    quote_id: Optional[str] = Field(None, description="Quote ID")
    payment_id: Optional[str] = Field(None, description="Payment ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    billing_address_ui: Optional[Dict[str, Any]] = Field(None, description="Billing Address")
    shipping_address_ui: Optional[Dict[str, Any]] = Field(None, description="Shipping Address")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    invoice: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    api_version: Optional[str] = Field(None, description="API Version")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    amount: Optional[float] = Field(None, description="Amount")


class InvoiceninjaCreateTool(BaseTool):
    name: str = "invoiceninja_create"
    description: str = "Tool for invoiceNinja create operation - create operation"
    args_schema: type[BaseModel] | None = InvoiceninjaCreateToolInput
    credentials: Optional[InvoiceninjaCredentials] = None
