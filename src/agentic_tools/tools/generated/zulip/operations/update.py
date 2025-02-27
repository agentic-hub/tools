from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZulipCredentials

class ZulipUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the message")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    user_id: Optional[str] = Field(None, description="The ID of user to update")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    stream_id: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ZulipUpdateTool(BaseTool):
    name: str = "zulip_update"
    description: str = "Tool for zulip update operation - update operation"
    args_schema: type[BaseModel] | None = ZulipUpdateToolInput
    credentials: Optional[ZulipCredentials] = None
