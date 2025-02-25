from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PagerdutyGetallToolInput(BaseModel):
    conferenceBridgeUi: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    incidentId: Optional[str] = Field(None, description="Unique identifier for the incident")


class PagerdutyGetallTool(BaseTool):
    name = "pagerduty_getall"
    description = "Tool for pagerDuty getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the pagerDuty getAll operation."""
        # Implement the tool logic here
        return f"Running pagerDuty getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pagerDuty getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
