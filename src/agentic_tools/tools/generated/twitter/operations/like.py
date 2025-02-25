from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwitterCredentials(BaseModel):
    """Credentials for twitter authentication."""
    twitter_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="twitterOAuth2Api")

class TwitterLikeToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwitterCredentials] = Field(None, description="Custom credentials for authentication")
    tweet_id: Optional[Dict[str, Any]] = Field(None, description="The tweet to like")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    notice_location: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    notice_attachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to send the message to")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterLikeTool(BaseTool):
    name = "twitter_like"
    description = "Tool for twitter like operation - like operation"
    
    def __init__(self, credentials: Optional[TwitterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twitter like operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twitter like operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twitter like operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twitter like operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
