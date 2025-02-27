from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SeatableCredentials

class SeatableGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="The operation being performed")
    table_name: Optional[str] = Field(None, description="The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class SeatableGetallTool(BaseTool):
    name: str = "seatable_getall"
    description: str = "Tool for seaTable getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = SeatableGetallToolInput
    credentials: Optional[SeatableCredentials] = None
