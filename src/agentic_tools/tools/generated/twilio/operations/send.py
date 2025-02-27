from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwilioCredentials

class TwilioSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    to_whatsapp: Optional[bool] = Field(None, description="Whether the message should be sent to WhatsApp")
    operation: Optional[str] = Field(None, description="Operation")


class TwilioSendTool(BaseTool):
    name: str = "twilio_send"
    description: str = "Tool for twilio send operation - send operation"
    args_schema: type[BaseModel] | None = TwilioSendToolInput
    credentials: Optional[TwilioCredentials] = None
