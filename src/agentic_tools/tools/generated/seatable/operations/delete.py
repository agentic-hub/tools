from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SeatableCredentials

class SeatableDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="The operation being performed")
    table_name: Optional[str] = Field(None, description="The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class SeatableDeleteTool(BaseTool):
    name: str = "seatable_delete"
    connector_id: str = "nodes-base.seaTable"
    description: str = "Tool for seaTable delete operation - delete operation"
    args_schema: type[BaseModel] | None = SeatableDeleteToolInput
    credentials: Optional[SeatableCredentials] = None
