from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MessagebirdCredentials

class MessagebirdSendToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    message: Optional[str] = Field(None, description="The message to be send")
    recipients: Optional[str] = Field(None, description="All recipients separated by commas")
    originator: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class MessagebirdSendTool(BaseTool):
    name: str = "messagebird_send"
    description: str = "Tool for messageBird send operation - send operation"
    args_schema: type[BaseModel] | None = MessagebirdSendToolInput
    credentials: Optional[MessagebirdCredentials] = None
