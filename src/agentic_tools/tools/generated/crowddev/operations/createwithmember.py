from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CrowddevCreatewithmemberToolInput(BaseModel):
    timestamp: Optional[str] = Field(None, description="Date and time when the activity took place")
    displayName: Optional[str] = Field(None, description="UI friendly name of the member")
    platform: Optional[str] = Field(None, description="Platform on which the activity took place")
    type: Optional[str] = Field(None, description="Type of activity")
    sourceId: Optional[str] = Field(None, description="The ID of the activity in the platform (e.g. the ID of the message in Discord)")
    joinedAt: Optional[str] = Field(None, description="Date of joining the community")
    additionalOptions: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    id: Optional[str] = Field(None, description="The ID of the member")
    operation: Optional[str] = Field(None, description="Operation")
    username: Optional[Dict[str, Any]] = Field(None, description="Username")
    emails: Optional[Dict[str, Any]] = Field(None, description="Email addresses of the member")
    resource: Optional[str] = Field(None, description="Resource")


class CrowddevCreatewithmemberTool(BaseTool):
    name = "crowddev_createwithmember"
    description = "Tool for crowdDev createWithMember operation - createWithMember operation"
    
    def _run(self, **kwargs):
        """Run the crowdDev createWithMember operation."""
        # Implement the tool logic here
        return f"Running crowdDev createWithMember operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the crowdDev createWithMember operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
