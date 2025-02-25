from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StravaCredentials(BaseModel):
    """Credentials for strava authentication."""
    strava_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="stravaOAuth2Api")

class StravaCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[StravaCredentials] = Field(None, description="Custom credentials for authentication")
    name: Optional[str] = Field(None, description="The name of the activity")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activity_id: Optional[str] = Field(None, description="ID or email of activity")
    start_date: Optional[str] = Field(None, description="ISO 8601 formatted date time")
    elapsed_time: Optional[float] = Field(None, description="In seconds")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of activity. For example - Run, Ride etc.")


class StravaCreateTool(BaseTool):
    name = "strava_create"
    description = "Tool for strava create operation - create operation"
    
    def __init__(self, credentials: Optional[StravaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the strava create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running strava create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running strava create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the strava create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
