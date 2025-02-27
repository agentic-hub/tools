from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BaserowCredentials

class BaserowGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database_id: Optional[str] = Field(None, description="Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    row_id: Optional[str] = Field(None, description="ID of the row to return")
    operation: Optional[str] = Field(None, description="Operation")


class BaserowGetTool(BaseTool):
    name: str = "baserow_get"
    description: str = "Tool for baserow get operation - get operation"
    args_schema: type[BaseModel] | None = BaserowGetToolInput
    credentials: Optional[BaserowCredentials] = None
