from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StravaGetzonesToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activityId: Optional[str] = Field(None, description="ID or email of activity")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")


class StravaGetzonesTool(BaseTool):
    name = "strava_getzones"
    description = "Tool for strava getZones operation - getZones operation"
    
    def _run(self, **kwargs):
        """Run the strava getZones operation."""
        # Implement the tool logic here
        return f"Running strava getZones operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strava getZones operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
