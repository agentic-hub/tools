from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import InvoiceninjaCredentials

class InvoiceninjaDeleteToolInput(BaseModel):
    invoice_id: Optional[str] = Field(None, description="Invoice ID")
    invoice_items_ui: Optional[Dict[str, Any]] = Field(None, description="Invoice Items")
    expense_id: Optional[str] = Field(None, description="Expense ID")
    quote_id: Optional[str] = Field(None, description="Quote ID")
    payment_id: Optional[str] = Field(None, description="Payment ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    api_version: Optional[str] = Field(None, description="API Version")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class InvoiceninjaDeleteTool(BaseTool):
    name: str = "invoiceninja_delete"
    connector_id: str = "nodes-base.invoiceNinja"
    description: str = "Tool for invoiceNinja delete operation - delete operation"
    args_schema: type[BaseModel] | None = InvoiceninjaDeleteToolInput
    credentials: Optional[InvoiceninjaCredentials] = None
