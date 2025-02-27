from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwitterCredentials

class TwitterSearchToolInput(BaseModel):
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
    name: str = "twitter_search"
    description: str = "Tool for twitter search operation - search operation"
    args_schema: type[BaseModel] | None = TwitterSearchToolInput
    credentials: Optional[TwitterCredentials] = None
