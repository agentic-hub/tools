from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CrowddevCredentials

class CrowddevCreateToolInput(BaseModel):
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    source_id: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    trigger: Optional[str] = Field(None, description="What will trigger an automation")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the organization")
    body: Optional[str] = Field(None, description="The body of the note")
    url: Optional[str] = Field(None, description="URL to POST webhook data to")
    username: Optional[Dict[str, Any]] = Field(None, description="Username")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevCreateTool(BaseTool):
    name: str = "crowddev_create"
    connector_id: str = "nodes-base.crowdDev"
    description: str = "Tool for crowdDev create operation - create operation"
    args_schema: type[BaseModel] | None = CrowddevCreateToolInput
    credentials: Optional[CrowddevCredentials] = None
