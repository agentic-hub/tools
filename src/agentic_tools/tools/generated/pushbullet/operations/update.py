from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushbulletCredentials

class PushbulletUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    dismissed: Optional[bool] = Field(None, description="Whether to mark a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")


class PushbulletUpdateTool(BaseTool):
    name: str = "pushbullet_update"
    description: str = "Tool for pushbullet update operation - update operation"
    args_schema: type[BaseModel] | None = PushbulletUpdateToolInput
    credentials: Optional[PushbulletCredentials] = None
