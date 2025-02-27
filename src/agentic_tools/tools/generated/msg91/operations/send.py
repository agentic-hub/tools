from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Msg91Credentials

class Msg91SendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number, with coutry code, to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class Msg91SendTool(BaseTool):
    name: str = "msg91_send"
    description: str = "Tool for msg91 send operation - send operation"
    args_schema: type[BaseModel] | None = Msg91SendToolInput
    credentials: Optional[Msg91Credentials] = None
