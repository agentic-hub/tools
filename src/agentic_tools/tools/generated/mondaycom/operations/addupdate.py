from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MondaycomCredentials

class MondaycomAddupdateToolInput(BaseModel):
    item_id: Optional[str] = Field(None, description="The unique identifier of the item to add update to")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The update text to add")
    column_id: Optional[str] = Field(None, description="The column's unique identifier. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The board's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    board_id: Optional[str] = Field(None, description="Board unique identifiers. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    group_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class MondaycomAddupdateTool(BaseTool):
    name: str = "mondaycom_addupdate"
    connector_id: str = "nodes-base.mondayCom"
    description: str = "Tool for mondayCom addUpdate operation - addUpdate operation"
    args_schema: type[BaseModel] | None = MondaycomAddupdateToolInput
    credentials: Optional[MondaycomCredentials] = None
