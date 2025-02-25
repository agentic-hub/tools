from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleanalyticsCredentials(BaseModel):
    """Credentials for googleAnalytics authentication."""
    google_analytics_o_auth2: Optional[Dict[str, Any]] = Field(None, description="googleAnalyticsOAuth2")

class GoogleanalyticsSearchToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogleanalyticsCredentials] = Field(None, description="Custom credentials for authentication")
    date_range: Optional[str] = Field(None, description="Date Range")
    view_id: Optional[str] = Field(None, description="The view from Google Analytics. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="ID of a user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    end_date: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    start_date: Optional[str] = Field(None, description="Start")


class GoogleanalyticsSearchTool(BaseTool):
    name = "googleanalytics_search"
    description = "Tool for googleAnalytics search operation - search operation"
    
    def __init__(self, credentials: Optional[GoogleanalyticsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleAnalytics search operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleAnalytics search operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleAnalytics search operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleAnalytics search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
