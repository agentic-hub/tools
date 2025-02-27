from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushbulletCredentials

class PushbulletCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    target: Optional[str] = Field(None, description="Define the medium that will be used to send the push")
    body: Optional[str] = Field(None, description="Body of the push")
    url: Optional[str] = Field(None, description="URL of the push")
    title: Optional[str] = Field(None, description="Title of the push")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class PushbulletCreateTool(BaseTool):
    name: str = "pushbullet_create"
    description: str = "Tool for pushbullet create operation - create operation"
    args_schema: type[BaseModel] | None = PushbulletCreateToolInput
    credentials: Optional[PushbulletCredentials] = None
