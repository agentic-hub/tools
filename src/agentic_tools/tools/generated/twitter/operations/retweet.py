from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwitterCredentials

class TwitterRetweetToolInput(BaseModel):
    tweet_id: Optional[Dict[str, Any]] = Field(None, description="The tweet to retweet")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    notice_location: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    notice_attachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to send the message to")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterRetweetTool(BaseTool):
    name: str = "twitter_retweet"
    connector_id: str = "nodes-base.twitter"
    description: str = "Tool for twitter retweet operation - retweet operation"
    args_schema: type[BaseModel] | None = TwitterRetweetToolInput
    credentials: Optional[TwitterCredentials] = None
