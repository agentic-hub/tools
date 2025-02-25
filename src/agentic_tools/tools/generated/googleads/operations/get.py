from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleadsCredentials(BaseModel):
    """Credentials for googleAds authentication."""
    google_ads_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleAdsOAuth2Api")

class GoogleadsGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogleadsCredentials] = Field(None, description="Custom credentials for authentication")
    manager_customer_id: Optional[str] = Field(None, description="Manager Customer ID")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign")
    campaigs_notice: Optional[str] = Field(None, description="Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value")
    client_customer_id: Optional[str] = Field(None, description="Client Customer ID")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleadsGetTool(BaseTool):
    name = "googleads_get"
    description = "Tool for googleAds get operation - get operation"
    
    def __init__(self, credentials: Optional[GoogleadsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleAds get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleAds get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleAds get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleAds get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
