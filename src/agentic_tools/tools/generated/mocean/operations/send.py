from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MoceanCredentials

class MoceanSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="Number from which to send the message")
    language: Optional[str] = Field(None, description="Language")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message to send")
    from: Optional[str] = Field(None, description="Number to which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class MoceanSendTool(BaseTool):
    name: str = "mocean_send"
    description: str = "Tool for mocean send operation - send operation"
    args_schema: type[BaseModel] | None = MoceanSendToolInput
    credentials: Optional[MoceanCredentials] = None
