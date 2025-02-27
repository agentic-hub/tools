from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglechatCredentials

class GooglechatGetToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    member_id: Optional[str] = Field(None, description="Member to be retrieved in the form \"spaces/*/members/*\"")
    json_parameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    space_id: Optional[str] = Field(None, description="Resource name of the space, in the form \"spaces/*\"")
    message_id: Optional[str] = Field(None, description="Resource name of the message to be retrieved, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatGetTool(BaseTool):
    name: str = "googlechat_get"
    description: str = "Tool for googleChat get operation - get operation"
    args_schema: type[BaseModel] | None = GooglechatGetToolInput
    credentials: Optional[GooglechatCredentials] = None
