from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushbulletCredentials

class Pushbullet__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")


class Pushbullet__custom_api_call__Tool(BaseTool):
    name: str = "pushbullet___custom_api_call__"
    connector_id: str = "nodes-base.pushbullet"
    description: str = "Tool for pushbullet __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Pushbullet__custom_api_call__ToolInput
    credentials: Optional[PushbulletCredentials] = None
