from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushbulletCredentials

class PushbulletGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    push_id: Optional[str] = Field(None, description="Push ID")
    operation: Optional[str] = Field(None, description="Operation")


class PushbulletGetallTool(BaseTool):
    name: str = "pushbullet_getall"
    connector_id: str = "nodes-base.pushbullet"
    description: str = "Tool for pushbullet getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = PushbulletGetallToolInput
    credentials: Optional[PushbulletCredentials] = None
