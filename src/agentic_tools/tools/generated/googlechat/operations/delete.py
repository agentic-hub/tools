from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglechatCredentials

class GooglechatDeleteToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    json_parameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    space_id: Optional[str] = Field(None, description="The name of the space for which to retrieve members, in the form \"spaces/*\". Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    message_id: Optional[str] = Field(None, description="Resource name of the message to be deleted, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatDeleteTool(BaseTool):
    name: str = "googlechat_delete"
    description: str = "Tool for googleChat delete operation - delete operation"
    args_schema: type[BaseModel] | None = GooglechatDeleteToolInput
    credentials: Optional[GooglechatCredentials] = None
