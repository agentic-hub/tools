from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedditCredentials(BaseModel):
    """Credentials for reddit authentication."""
    reddit_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="redditOAuth2Api")

class RedditCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RedditCredentials] = Field(None, description="Custom credentials for authentication")
    post_id: Optional[str] = Field(None, description="ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    comment_id: Optional[str] = Field(None, description="ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    resubmit: Optional[bool] = Field(None, description="Whether the URL will be posted even if it was already posted to the subreddit before. Otherwise, the re-posting will trigger an error.")
    text: Optional[str] = Field(None, description="Text of the post. Markdown supported.")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    kind: Optional[str] = Field(None, description="The kind of the post to create")
    subreddit: Optional[str] = Field(None, description="Subreddit to create the post in")
    comment_text: Optional[str] = Field(None, description="Text of the comment. Markdown supported.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="URL of the post")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    title: Optional[str] = Field(None, description="Title of the post, up to 300 characters long")


class RedditCreateTool(BaseTool):
    name = "reddit_create"
    description = "Tool for reddit create operation - create operation"
    
    def __init__(self, credentials: Optional[RedditCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the reddit create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running reddit create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running reddit create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the reddit create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
