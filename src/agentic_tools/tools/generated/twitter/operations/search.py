from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwitterCredentials(BaseModel):
    """Credentials for twitter authentication."""
    twitter_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="twitterOAuth2Api")

class TwitterSearchToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwitterCredentials] = Field(None, description="Custom credentials for authentication")
    tweet_id: Optional[Dict[str, Any]] = Field(None, description="The tweet to like")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    notice_location: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    notice_attachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to send the message to")
    search_text: Optional[str] = Field(None, description="A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href=\"https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators\">here</a>.")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterSearchTool(BaseTool):
    name = "twitter_search"
    description = "Tool for twitter search operation - search operation"
    
    def __init__(self, credentials: Optional[TwitterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twitter search operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twitter search operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twitter search operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twitter search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
