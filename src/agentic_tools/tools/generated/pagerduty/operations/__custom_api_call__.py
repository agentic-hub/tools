from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Pagerduty__custom_api_call__ToolInput(BaseModel):
    conferenceBridgeUi: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    incidentId: Optional[str] = Field(None, description="Unique identifier for the incident")


class Pagerduty__custom_api_call__Tool(BaseTool):
    name = "pagerduty___custom_api_call__"
    description = "Tool for pagerDuty __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the pagerDuty __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running pagerDuty __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pagerDuty __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
