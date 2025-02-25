from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StravaGetcommentsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activityId: Optional[str] = Field(None, description="ID or email of activity")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")


class StravaGetcommentsTool(BaseTool):
    name = "strava_getcomments"
    description = "Tool for strava getComments operation - getComments operation"
    
    def _run(self, **kwargs):
        """Run the strava getComments operation."""
        # Implement the tool logic here
        return f"Running strava getComments operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strava getComments operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
