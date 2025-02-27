from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KitemakerCredentials

class KitemakerUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    space_id: Optional[str] = Field(None, description="ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    work_item_id: Optional[str] = Field(None, description="ID of the work item to update")
    operation: Optional[str] = Field(None, description="Operation")


class KitemakerUpdateTool(BaseTool):
    name: str = "kitemaker_update"
    connector_id: str = "nodes-base.kitemaker"
    description: str = "Tool for kitemaker update operation - update operation"
    args_schema: type[BaseModel] | None = KitemakerUpdateToolInput
    credentials: Optional[KitemakerCredentials] = None
