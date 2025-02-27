from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BaserowCredentials

class BaserowGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database_id: Optional[str] = Field(None, description="Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Options")
    row_id: Optional[str] = Field(None, description="ID of the row to return")
    operation: Optional[str] = Field(None, description="Operation")


class BaserowGetallTool(BaseTool):
    name: str = "baserow_getall"
    connector_id: str = "nodes-base.baserow"
    description: str = "Tool for baserow getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BaserowGetallToolInput
    credentials: Optional[BaserowCredentials] = None
