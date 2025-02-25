from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedditCredentials(BaseModel):
    """Credentials for reddit authentication."""
    reddit_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="redditOAuth2Api")

class RedditSearchToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RedditCredentials] = Field(None, description="Custom credentials for authentication")
    post_id: Optional[str] = Field(None, description="ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    location: Optional[str] = Field(None, description="Location where to search for posts")
    comment_id: Optional[str] = Field(None, description="ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subreddit: Optional[str] = Field(None, description="The name of subreddit to search in")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    keyword: Optional[str] = Field(None, description="The keyword for the search")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class RedditSearchTool(BaseTool):
    name = "reddit_search"
    description = "Tool for reddit search operation - search operation"
    
    def __init__(self, credentials: Optional[RedditCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the reddit search operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running reddit search operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running reddit search operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the reddit search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
