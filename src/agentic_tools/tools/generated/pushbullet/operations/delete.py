from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushbulletCredentials

class PushbulletDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")


class PushbulletDeleteTool(BaseTool):
    name: str = "pushbullet_delete"
    description: str = "Tool for pushbullet delete operation - delete operation"
    args_schema: type[BaseModel] | None = PushbulletDeleteToolInput
    credentials: Optional[PushbulletCredentials] = None
