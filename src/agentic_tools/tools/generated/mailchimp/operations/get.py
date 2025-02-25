from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailchimpCredentials(BaseModel):
    """Credentials for mailchimp authentication."""
    mailchimp_api: Optional[Dict[str, Any]] = Field(None, description="mailchimpApi")
    mailchimp_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mailchimpOAuth2Api")

class MailchimpGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MailchimpCredentials] = Field(None, description="Custom credentials for authentication")
    campaign_id: Optional[str] = Field(None, description="List of Campaigns")
    group_json: Optional[str] = Field(None, description="Interest Groups")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    list: Optional[str] = Field(None, description="List of lists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Member's email")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    merge_fields_json: Optional[str] = Field(None, description="Merge Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    location_json: Optional[str] = Field(None, description="Location")


class MailchimpGetTool(BaseTool):
    name = "mailchimp_get"
    description = "Tool for mailchimp get operation - get operation"
    
    def __init__(self, credentials: Optional[MailchimpCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mailchimp get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mailchimp get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mailchimp get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailchimp get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
