from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZammadCredentials

class ZammadGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Group to update. Specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Group Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZammadGetallTool(BaseTool):
    name: str = "zammad_getall"
    connector_id: str = "nodes-base.zammad"
    description: str = "Tool for zammad getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ZammadGetallToolInput
    credentials: Optional[ZammadCredentials] = None
