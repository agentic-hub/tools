from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GristCredentials

class GristCreateToolInput(BaseModel):
    doc_id: Optional[str] = Field(None, description="In your document, click your profile icon, then Document Settings, then copy the value under \"This document's ID\"")
    table_id: Optional[str] = Field(None, description="ID of table to operate on. If unsure, look at the Code View.")
    fields_to_send: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    row_id: Optional[str] = Field(None, description="ID of the row to delete, or comma-separated list of row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GristCreateTool(BaseTool):
    name: str = "grist_create"
    connector_id: str = "nodes-base.grist"
    description: str = "Tool for grist create operation - create operation"
    args_schema: type[BaseModel] | None = GristCreateToolInput
    credentials: Optional[GristCredentials] = None
