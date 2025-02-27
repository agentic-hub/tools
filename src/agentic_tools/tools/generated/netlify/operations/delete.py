from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import NetlifyCredentials

class NetlifyDeleteToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    site_id: Optional[str] = Field(None, description="Site ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class NetlifyDeleteTool(BaseTool):
    name: str = "netlify_delete"
    connector_id: str = "nodes-base.netlify"
    description: str = "Tool for netlify delete operation - delete operation"
    args_schema: type[BaseModel] | None = NetlifyDeleteToolInput
    credentials: Optional[NetlifyCredentials] = None
