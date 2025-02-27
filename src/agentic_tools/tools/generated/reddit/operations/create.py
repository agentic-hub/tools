from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedditCredentials

class RedditCreateToolInput(BaseModel):
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
    name: str = "reddit_create"
    description: str = "Tool for reddit create operation - create operation"
    args_schema: type[BaseModel] | None = RedditCreateToolInput
    credentials: Optional[RedditCredentials] = None
