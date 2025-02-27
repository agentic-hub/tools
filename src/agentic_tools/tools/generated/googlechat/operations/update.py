from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglechatCredentials

class GooglechatUpdateToolInput(BaseModel):
    update_fields_ui: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_fields_json: Optional[str] = Field(None, description="Message input as JSON Object or JSON String")
    json_parameters: Optional[bool] = Field(None, description="Whether to pass the update fields object as JSON")
    space_id: Optional[str] = Field(None, description="The name of the space for which to retrieve members, in the form \"spaces/*\". Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    message_id: Optional[str] = Field(None, description="Resource name of the message to be updated, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatUpdateTool(BaseTool):
    name: str = "googlechat_update"
    connector_id: str = "nodes-base.googleChat"
    description: str = "Tool for googleChat update operation - update operation"
    args_schema: type[BaseModel] | None = GooglechatUpdateToolInput
    credentials: Optional[GooglechatCredentials] = None
