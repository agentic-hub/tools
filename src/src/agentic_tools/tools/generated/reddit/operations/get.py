from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RedditGetToolInput(BaseModel):
    content: Optional[str] = Field(None, description="Subreddit content to retrieve")
    postId: Optional[str] = Field(None, description="ID of the post to retrieve. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    commentId: Optional[str] = Field(None, description="ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subreddit: Optional[str] = Field(None, description="The name of subreddit to retrieve the content from")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    username: Optional[str] = Field(None, description="Reddit ID of the user to retrieve")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")


class RedditGetTool(BaseTool):
    name = "reddit_get"
    description = "Tool for reddit get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the reddit get operation."""
        # Implement the tool logic here
        return f"Running reddit get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the reddit get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
