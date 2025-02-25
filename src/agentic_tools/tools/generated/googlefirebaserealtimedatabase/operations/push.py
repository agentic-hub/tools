from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglefirebaserealtimedatabaseCredentials(BaseModel):
    """Credentials for googleFirebaseRealtimeDatabase authentication."""
    google_firebase_realtime_database_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleFirebaseRealtimeDatabaseOAuth2Api")

class GooglefirebaserealtimedatabasePushToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = Field(None, description="Custom credentials for authentication")
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    attributes: Optional[str] = Field(None, description="Attributes to save")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class GooglefirebaserealtimedatabasePushTool(BaseTool):
    name = "googlefirebaserealtimedatabase_push"
    description = "Tool for googleFirebaseRealtimeDatabase push operation - push operation"
    
    def __init__(self, credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleFirebaseRealtimeDatabase push operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleFirebaseRealtimeDatabase push operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleFirebaseRealtimeDatabase push operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleFirebaseRealtimeDatabase push operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
