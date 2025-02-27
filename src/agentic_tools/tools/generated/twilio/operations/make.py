from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwilioCredentials

class TwilioMakeToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    twiml: Optional[bool] = Field(None, description="Whether to use the <a href=\"https://www.twilio.com/docs/voice/twiml\">Twilio Markup Language</a> in the message")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class TwilioMakeTool(BaseTool):
    name: str = "twilio_make"
    description: str = "Tool for twilio make operation - make operation"
    args_schema: type[BaseModel] | None = TwilioMakeToolInput
    credentials: Optional[TwilioCredentials] = None
