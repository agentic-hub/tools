from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import XeroCredentials

class Xero__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    invoice_id: Optional[str] = Field(None, description="Invoice ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organization_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    operation: Optional[str] = Field(None, description="Operation")


class Xero__custom_api_call__Tool(BaseTool):
    name: str = "xero___custom_api_call__"
    description: str = "Tool for xero __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Xero__custom_api_call__ToolInput
    credentials: Optional[XeroCredentials] = None
