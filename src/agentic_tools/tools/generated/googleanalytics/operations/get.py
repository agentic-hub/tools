from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleanalyticsCredentials(BaseModel):
    """Credentials for googleAnalytics authentication."""
    google_analytics_o_auth2: Optional[Dict[str, Any]] = Field(None, description="googleAnalyticsOAuth2")

class GoogleanalyticsGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogleanalyticsCredentials] = Field(None, description="Custom credentials for authentication")
    date_range: Optional[str] = Field(None, description="Date Range")
    metrics_ga4: Optional[Dict[str, Any]] = Field(None, description="The quantitative measurements of a report. For example, the metric eventCount is the total number of events. Requests are allowed up to 10 metrics.")
    property_id: Optional[str] = Field(None, description="By URL")
    view_id: Optional[Dict[str, Any]] = Field(None, description="The View of Google Analytics")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    dimensions_ua: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension ga:city indicates the city, for example, \"Paris\" or \"New York\", from which a session originates.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    property_type: Optional[str] = Field(None, description="Google Analytics 4 is the latest version. Universal Analytics is an older version that is not fully functional after the end of June 2023.")
    end_date: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    dimensions_ga4: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be \"Paris\" or \"New York\". Requests are allowed up to 9 dimensions.")
    start_date: Optional[str] = Field(None, description="Start")
    metrics_ua: Optional[Dict[str, Any]] = Field(None, description="Metrics in the request")


class GoogleanalyticsGetTool(BaseTool):
    name = "googleanalytics_get"
    description = "Tool for googleAnalytics get operation - get operation"
    
    def __init__(self, credentials: Optional[GoogleanalyticsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleAnalytics get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleAnalytics get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleAnalytics get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleAnalytics get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
