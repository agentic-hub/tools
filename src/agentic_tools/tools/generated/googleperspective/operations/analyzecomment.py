from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleperspectiveCredentials(BaseModel):
    """Credentials for googlePerspective authentication."""
    google_perspective_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googlePerspectiveOAuth2Api")

class GoogleperspectiveAnalyzecommentToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogleperspectiveCredentials] = Field(None, description="Custom credentials for authentication")
    requested_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Attributes to Analyze")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    text: Optional[str] = Field(None, description="Text")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleperspectiveAnalyzecommentTool(BaseTool):
    name = "googleperspective_analyzecomment"
    description = "Tool for googlePerspective analyzeComment operation - analyzeComment operation"
    
    def __init__(self, credentials: Optional[GoogleperspectiveCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googlePerspective analyzeComment operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googlePerspective analyzeComment operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googlePerspective analyzeComment operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googlePerspective analyzeComment operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
