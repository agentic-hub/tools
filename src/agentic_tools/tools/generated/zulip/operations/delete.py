from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZulipCredentials

class ZulipDeleteToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    user_id: Optional[str] = Field(None, description="The ID of user to get")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    stream_id: Optional[str] = Field(None, description="ID of stream to delete")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ZulipDeleteTool(BaseTool):
    name: str = "zulip_delete"
    description: str = "Tool for zulip delete operation - delete operation"
    args_schema: type[BaseModel] | None = ZulipDeleteToolInput
    credentials: Optional[ZulipCredentials] = None
