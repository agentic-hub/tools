from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZulipCredentials

class ZulipSendstreamToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message")
    stream: Optional[str] = Field(None, description="The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    user_id: Optional[str] = Field(None, description="The ID of user to get")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    stream_id: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    topic: Optional[str] = Field(None, description="The topic of the message. Only required if type is stream, ignored otherwise. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ZulipSendstreamTool(BaseTool):
    name: str = "zulip_sendstream"
    connector_id: str = "nodes-base.zulip"
    description: str = "Tool for zulip sendStream operation - sendStream operation"
    args_schema: type[BaseModel] | None = ZulipSendstreamToolInput
    credentials: Optional[ZulipCredentials] = None
