from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CrowddevCredentials

class CrowddevCreateorupdateToolInput(BaseModel):
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    source_id: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    username: Optional[str] = Field(None, description="Username of the member in platform")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevCreateorupdateTool(BaseTool):
    name: str = "crowddev_createorupdate"
    description: str = "Tool for crowdDev createOrUpdate operation - createOrUpdate operation"
    args_schema: type[BaseModel] | None = CrowddevCreateorupdateToolInput
    credentials: Optional[CrowddevCredentials] = None
