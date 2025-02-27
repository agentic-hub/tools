from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedditCredentials

class RedditDeleteToolInput(BaseModel):
    post_id: Optional[str] = Field(None, description="ID of the post to delete. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    comment_id: Optional[str] = Field(None, description="ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subreddit: Optional[str] = Field(None, description="The name of subreddit where the post is")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")


class RedditDeleteTool(BaseTool):
    name: str = "reddit_delete"
    description: str = "Tool for reddit delete operation - delete operation"
    args_schema: type[BaseModel] | None = RedditDeleteToolInput
    credentials: Optional[RedditCredentials] = None
