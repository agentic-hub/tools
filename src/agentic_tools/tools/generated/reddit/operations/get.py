from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedditCredentials(BaseModel):
    """Credentials for reddit authentication."""
    reddit_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="redditOAuth2Api")

class RedditGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RedditCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="Subreddit content to retrieve")
    post_id: Optional[str] = Field(None, description="ID of the post to retrieve. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    comment_id: Optional[str] = Field(None, description="ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subreddit: Optional[str] = Field(None, description="The name of subreddit to retrieve the content from")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    username: Optional[str] = Field(None, description="Reddit ID of the user to retrieve")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")


class RedditGetTool(BaseTool):
    name = "reddit_get"
    description = "Tool for reddit get operation - get operation"
    
    def __init__(self, credentials: Optional[RedditCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the reddit get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running reddit get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running reddit get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the reddit get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
