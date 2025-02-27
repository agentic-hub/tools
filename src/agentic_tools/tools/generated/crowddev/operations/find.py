from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CrowddevCredentials

class CrowddevFindToolInput(BaseModel):
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    source_id: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    username: Optional[Dict[str, Any]] = Field(None, description="Username")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevFindTool(BaseTool):
    name: str = "crowddev_find"
    description: str = "Tool for crowdDev find operation - find operation"
    args_schema: type[BaseModel] | None = CrowddevFindToolInput
    credentials: Optional[CrowddevCredentials] = None
