from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RedditCredentials

class RedditReplyToolInput(BaseModel):
    post_id: Optional[str] = Field(None, description="ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit_name]/comments/[post_id]/[post_title]</code>")
    comment_id: Optional[str] = Field(None, description="ID of the comment to reply to. To be found in the comment URL: <code>www.reddit.com/r/[subreddit_name]/comments/[post_id]/[post_title]/[comment_id]</code>")
    details: Optional[str] = Field(None, description="Details of my account to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subreddit: Optional[str] = Field(None, description="The name of subreddit where the post is")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    reply_text: Optional[str] = Field(None, description="Text of the reply. Markdown supported.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")


class RedditReplyTool(BaseTool):
    name: str = "reddit_reply"
    connector_id: str = "nodes-base.reddit"
    description: str = "Tool for reddit reply operation - reply operation"
    args_schema: type[BaseModel] | None = RedditReplyToolInput
    credentials: Optional[RedditCredentials] = None
