from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BaserowCredentials

class BaserowDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database_id: Optional[str] = Field(None, description="Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    row_id: Optional[str] = Field(None, description="ID of the row to delete")
    operation: Optional[str] = Field(None, description="Operation")


class BaserowDeleteTool(BaseTool):
    name: str = "baserow_delete"
    connector_id: str = "nodes-base.baserow"
    description: str = "Tool for baserow delete operation - delete operation"
    args_schema: type[BaseModel] | None = BaserowDeleteToolInput
    credentials: Optional[BaserowCredentials] = None
