from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssnsCredentials

class AwssnsPublishToolInput(BaseModel):
    message: Optional[str] = Field(None, description="The message you want to send")
    subject: Optional[str] = Field(None, description="Subject when the message is delivered to email endpoints")
    topic: Optional[str] = Field(None, description="By URL")
    operation: Optional[str] = Field(None, description="Operation")


class AwssnsPublishTool(BaseTool):
    name: str = "awssns_publish"
    description: str = "Tool for awsSns publish operation - publish operation"
    args_schema: type[BaseModel] | None = AwssnsPublishToolInput
    credentials: Optional[AwssnsCredentials] = None
