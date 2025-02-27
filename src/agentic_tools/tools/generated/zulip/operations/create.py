from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZulipCredentials

class ZulipCreateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message")
    full_name: Optional[str] = Field(None, description="The full name of the new user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    short_name: Optional[str] = Field(None, description="The short name of the new user. Not user-visible.")
    user_id: Optional[str] = Field(None, description="The ID of user to get")
    email: Optional[str] = Field(None, description="The email address of the new user")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    password: Optional[str] = Field(None, description="The password of the new user")
    stream_id: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    subscriptions: Optional[Dict[str, Any]] = Field(None, description="A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created.")


class ZulipCreateTool(BaseTool):
    name: str = "zulip_create"
    description: str = "Tool for zulip create operation - create operation"
    args_schema: type[BaseModel] | None = ZulipCreateToolInput
    credentials: Optional[ZulipCredentials] = None
