from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleslidesCredentials(BaseModel):
    """Credentials for googleSlides authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_slides_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleSlidesOAuth2Api")

class GoogleslidesReplacetextToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GoogleslidesCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    text_ui: Optional[Dict[str, Any]] = Field(None, description="Texts To Replace")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    presentation_id: Optional[str] = Field(None, description="ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION_ID/edit</code>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleslidesReplacetextTool(BaseTool):
    name = "googleslides_replacetext"
    description = "Tool for googleSlides replaceText operation - replaceText operation"
    
    def __init__(self, credentials: Optional[GoogleslidesCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleSlides replaceText operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleSlides replaceText operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleSlides replaceText operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSlides replaceText operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
