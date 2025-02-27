from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CrowddevCredentials

class CrowddevCreatewithmemberToolInput(BaseModel):
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    display_name: Optional[str] = Field(None, description="UI friendly name of the member")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    source_id: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    joined_at: Optional[str] = Field(None, description="Date of joining the community")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    username: Optional[Dict[str, Any]] = Field(None, description="Username")
    emails: Optional[Dict[str, Any]] = Field(None, description="Email addresses of the member")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevCreatewithmemberTool(BaseTool):
    name: str = "crowddev_createwithmember"
    description: str = "Tool for crowdDev createWithMember operation - createWithMember operation"
    args_schema: type[BaseModel] | None = CrowddevCreatewithmemberToolInput
    credentials: Optional[CrowddevCredentials] = None
