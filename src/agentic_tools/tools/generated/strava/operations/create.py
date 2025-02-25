from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StravaCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="The name of the activity")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activityId: Optional[str] = Field(None, description="ID or email of activity")
    startDate: Optional[str] = Field(None, description="ISO 8601 formatted date time")
    elapsedTime: Optional[float] = Field(None, description="In seconds")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of activity. For example - Run, Ride etc.")


class StravaCreateTool(BaseTool):
    name = "strava_create"
    description = "Tool for strava create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the strava create operation."""
        # Implement the tool logic here
        return f"Running strava create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strava create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
