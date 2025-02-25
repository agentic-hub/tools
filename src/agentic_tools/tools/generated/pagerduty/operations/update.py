from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PagerdutyCredentials(BaseModel):
    """Credentials for pagerDuty authentication."""
    pager_duty_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyApi")
    pager_duty_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyOAuth2Api")

class PagerdutyUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PagerdutyCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    conference_bridge_ui: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    incident_id: Optional[str] = Field(None, description="Unique identifier for the incident")


class PagerdutyUpdateTool(BaseTool):
    name = "pagerduty_update"
    description = "Tool for pagerDuty update operation - update operation"
    
    def __init__(self, credentials: Optional[PagerdutyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pagerDuty update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pagerDuty update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pagerDuty update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pagerDuty update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
