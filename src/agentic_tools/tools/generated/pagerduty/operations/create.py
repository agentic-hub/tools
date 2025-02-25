from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PagerdutyCredentials(BaseModel):
    """Credentials for pagerDuty authentication."""
    pager_duty_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyApi")
    pager_duty_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pagerDutyOAuth2Api")

class PagerdutyCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PagerdutyCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The note content")
    conference_bridge_ui: Optional[Dict[str, Any]] = Field(None, description="Conference Bridge")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of a valid user associated with the account making the request")
    service_id: Optional[str] = Field(None, description="The incident will be created on this service. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    title: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the incident")
    operation: Optional[str] = Field(None, description="Operation")
    incident_id: Optional[str] = Field(None, description="Unique identifier for the incident")


class PagerdutyCreateTool(BaseTool):
    name = "pagerduty_create"
    description = "Tool for pagerDuty create operation - create operation"
    
    def __init__(self, credentials: Optional[PagerdutyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the pagerDuty create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running pagerDuty create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running pagerDuty create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the pagerDuty create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
