from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RocketchatCredentials

class RocketchatPostmessageToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    attachments_json: Optional[str] = Field(None, description="Attachments")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    channel: Optional[str] = Field(None, description="The channel name with the prefix in front of it")
    operation: Optional[str] = Field(None, description="Operation")
    text: Optional[str] = Field(None, description="The text of the message to send, is optional because of attachments")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachments: Optional[List[Any]] = Field(None, description="Attachments")


class RocketchatPostmessageTool(BaseTool):
    name: str = "rocketchat_postmessage"
    connector_id: str = "nodes-base.rocketchat"
    description: str = "Tool for rocketchat postMessage operation - postMessage operation"
    args_schema: type[BaseModel] | None = RocketchatPostmessageToolInput
    credentials: Optional[RocketchatCredentials] = None
