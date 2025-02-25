from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HubspotCredentials(BaseModel):
    """Credentials for hubspot authentication."""
    hubspot_api: Optional[Dict[str, Any]] = Field(None, description="hubspotApi")
    hubspot_app_token: Optional[Dict[str, Any]] = Field(None, description="hubspotAppToken")
    hubspot_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="hubspotOAuth2Api")

class HubspotSearchbydomainToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HubspotCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    engagement_id: Optional[Dict[str, Any]] = Field(None, description="Engagement to Get")
    email: Optional[str] = Field(None, description="Email")
    ticket_id: Optional[Dict[str, Any]] = Field(None, description="Ticket to Update")
    id: Optional[float] = Field(None, description="Contact to Add")
    company_id: Optional[Dict[str, Any]] = Field(None, description="Company to Update")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[float] = Field(None, description="List to Add To")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadata")
    domain: Optional[str] = Field(None, description="The company's website domain to search for, like n8n.io")
    deal_id: Optional[Dict[str, Any]] = Field(None, description="Deal to Update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Contact Properties")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[Dict[str, Any]] = Field(None, description="This is not a contact's email but a number like 1485")
    filter_groups_ui: Optional[Dict[str, Any]] = Field(None, description="When multiple filters are provided within a Filter Group, they will be combined using a logical AND operator. When multiple Filter Groups are provided, they will be combined using a logical OR operator. The system supports a maximum of three Filter Groups with up to three filters each. More info <a href=\"https://developers.hubspot.com/docs/api/crm/search\">here</a>")


class HubspotSearchbydomainTool(BaseTool):
    name = "hubspot_searchbydomain"
    description = "Tool for hubspot searchByDomain operation - searchByDomain operation"
    
    def __init__(self, credentials: Optional[HubspotCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the hubspot searchByDomain operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running hubspot searchByDomain operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running hubspot searchByDomain operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the hubspot searchByDomain operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
