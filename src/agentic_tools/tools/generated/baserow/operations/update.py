from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BaserowCredentials

class BaserowUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database_id: Optional[str] = Field(None, description="Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    row_id: Optional[str] = Field(None, description="ID of the row to update")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class BaserowUpdateTool(BaseTool):
    name: str = "baserow_update"
    description: str = "Tool for baserow update operation - update operation"
    args_schema: type[BaseModel] | None = BaserowUpdateToolInput
    credentials: Optional[BaserowCredentials] = None
