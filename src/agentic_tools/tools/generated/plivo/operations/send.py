from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PlivoCredentials

class PlivoSendToolInput(BaseModel):
    media_urls: Optional[str] = Field(None, description="Comma-separated list of media URLs of the files from your file server")
    to: Optional[str] = Field(None, description="Phone number to send the message to")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message to send")
    from: Optional[str] = Field(None, description="Plivo Number to send the SMS from")
    operation: Optional[str] = Field(None, description="Operation")


class PlivoSendTool(BaseTool):
    name: str = "plivo_send"
    description: str = "Tool for plivo send operation - send operation"
    args_schema: type[BaseModel] | None = PlivoSendToolInput
    credentials: Optional[PlivoCredentials] = None
