from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import QuickbooksCredentials

class QuickbooksSendToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoice_id: Optional[str] = Field(None, description="The ID of the invoice to send")
    customer_ref: Optional[str] = Field(None, description="The ID of the customer who the estimate is for. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    customer_id: Optional[str] = Field(None, description="The ID of the customer to retrieve")
    employee_id: Optional[str] = Field(None, description="The ID of the employee to retrieve")
    display_name: Optional[str] = Field(None, description="The display name of the customer to create")
    payment_id: Optional[str] = Field(None, description="The ID of the payment to send")
    vendor_id: Optional[str] = Field(None, description="The ID of the vendor to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email of the recipient of the estimate")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    download: Optional[bool] = Field(None, description="Whether to download the estimate as a PDF file")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    bill_id: Optional[str] = Field(None, description="The ID of the bill to delete")
    line: Optional[List[Any]] = Field(None, description="Individual line item of a transaction")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    estimate_id: Optional[str] = Field(None, description="The ID of the estimate to send")
    file_name: Optional[str] = Field(None, description="Name of the file that will be downloaded")


class QuickbooksSendTool(BaseTool):
    name: str = "quickbooks_send"
    description: str = "Tool for quickbooks send operation - send operation"
    args_schema: type[BaseModel] | None = QuickbooksSendToolInput
    credentials: Optional[QuickbooksCredentials] = None
