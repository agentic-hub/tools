from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedditCredentials

class RedditSearchToolInput(BaseModel):
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
    name: str = "reddit_search"
    description: str = "Tool for reddit search operation - search operation"
    args_schema: type[BaseModel] | None = RedditSearchToolInput
    credentials: Optional[RedditCredentials] = None
