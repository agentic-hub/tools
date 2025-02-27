from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SeatableCredentials

class SeatableCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    columns_ui: Optional[Dict[str, Any]] = Field(None, description="Add destination column with its value")
    fields_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    row_id: Optional[str] = Field(None, description="Row ID")
    operation: Optional[str] = Field(None, description="The operation being performed")
    table_name: Optional[str] = Field(None, description="The name of SeaTable table to access. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class SeatableCreateTool(BaseTool):
    name: str = "seatable_create"
    connector_id: str = "nodes-base.seaTable"
    description: str = "Tool for seaTable create operation - create operation"
    args_schema: type[BaseModel] | None = SeatableCreateToolInput
    credentials: Optional[SeatableCredentials] = None
