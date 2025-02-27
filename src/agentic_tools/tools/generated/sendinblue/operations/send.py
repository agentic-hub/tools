from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendinblueCredentials

class SendinblueSendToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    send_html: Optional[bool] = Field(None, description="Send HTML")
    text_content: Optional[str] = Field(None, description="Text content of the message")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    html_content: Optional[str] = Field(None, description="HTML content of the message")
    subject: Optional[str] = Field(None, description="Subject of the email")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    sender: Optional[str] = Field(None, description="Sender")


class SendinblueSendTool(BaseTool):
    name: str = "sendinblue_send"
    connector_id: str = "nodes-base.sendInBlue"
    description: str = "Tool for sendInBlue send operation - send operation"
    args_schema: type[BaseModel] | None = SendinblueSendToolInput
    credentials: Optional[SendinblueCredentials] = None
