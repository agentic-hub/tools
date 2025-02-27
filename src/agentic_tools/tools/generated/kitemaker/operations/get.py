from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KitemakerCredentials

class KitemakerGetToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    space_id: Optional[str] = Field(None, description="ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    work_item_id: Optional[str] = Field(None, description="ID of the work item to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class KitemakerGetTool(BaseTool):
    name: str = "kitemaker_get"
    connector_id: str = "nodes-base.kitemaker"
    description: str = "Tool for kitemaker get operation - get operation"
    args_schema: type[BaseModel] | None = KitemakerGetToolInput
    credentials: Optional[KitemakerCredentials] = None
