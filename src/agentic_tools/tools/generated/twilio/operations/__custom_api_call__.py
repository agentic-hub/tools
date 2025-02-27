from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwilioCredentials

class Twilio__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send")
    operation: Optional[str] = Field(None, description="Operation")


class Twilio__custom_api_call__Tool(BaseTool):
    name: str = "twilio___custom_api_call__"
    description: str = "Tool for twilio __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Twilio__custom_api_call__ToolInput
    credentials: Optional[TwilioCredentials] = None
