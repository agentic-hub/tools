from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NetlifyCredentials

class NetlifyCreateToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    site_id: Optional[str] = Field(None, description="Enter the Site ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class NetlifyCreateTool(BaseTool):
    name: str = "netlify_create"
    connector_id: str = "nodes-base.netlify"
    description: str = "Tool for netlify create operation - create operation"
    args_schema: type[BaseModel] | None = NetlifyCreateToolInput
    credentials: Optional[NetlifyCredentials] = None
