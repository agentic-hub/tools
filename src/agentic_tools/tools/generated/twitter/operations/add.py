from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwitterCredentials

class TwitterAddToolInput(BaseModel):
    list: Optional[str] = Field(None, description="By ID")
    tweet_id: Optional[Dict[str, Any]] = Field(None, description="The tweet to like")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    notice_location: Optional[str] = Field(None, description="Locations are not supported due to Twitter V2 API limitations")
    notice_attachments: Optional[str] = Field(None, description="Attachements are not supported due to Twitter V2 API limitations")
    user: Optional[Dict[str, Any]] = Field(None, description="The user you want to add to the list")
    text: Optional[str] = Field(None, description="The text of the direct message. URL encoding is required. Max length of 10,000 characters.")
    operation: Optional[str] = Field(None, description="Operation")


class TwitterAddTool(BaseTool):
    name: str = "twitter_add"
    connector_id: str = "nodes-base.twitter"
    description: str = "Tool for twitter add operation - add operation"
    args_schema: type[BaseModel] | None = TwitterAddToolInput
    credentials: Optional[TwitterCredentials] = None
