from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import XeroCredentials

class XeroGetallToolInput(BaseModel):
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


class XeroGetallTool(BaseTool):
    name: str = "xero_getall"
    description: str = "Tool for xero getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = XeroGetallToolInput
    credentials: Optional[XeroCredentials] = None
