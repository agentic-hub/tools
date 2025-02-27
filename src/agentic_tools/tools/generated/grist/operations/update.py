from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GristCredentials

class GristUpdateToolInput(BaseModel):
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    fields_to_send: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    row_id: Optional[str] = Field(None, description="ID of the row to update")
    operation: Optional[str] = Field(None, description="Operation")


class GristUpdateTool(BaseTool):
    name: str = "grist_update"
    description: str = "Tool for grist update operation - update operation"
    args_schema: type[BaseModel] | None = GristUpdateToolInput
    credentials: Optional[GristCredentials] = None
