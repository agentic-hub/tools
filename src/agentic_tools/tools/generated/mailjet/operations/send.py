from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailjetCredentials

class MailjetSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="Message recipient. Should be between 3 and 15 characters in length. The number always starts with a plus sign followed by a country code, followed by the number. Phone numbers are expected to comply with the E.164 format.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    html: Optional[str] = Field(None, description="HTML text message of email")
    variables_json: Optional[str] = Field(None, description="HTML text message of email")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    variables_ui: Optional[Dict[str, Any]] = Field(None, description="Variables")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    from: Optional[str] = Field(None, description="Customizable sender name. Should be between 3 and 11 characters in length, only alphanumeric characters are allowed.")
    text: Optional[str] = Field(None, description="Plain text message of email")
    from_email: Optional[str] = Field(None, description="The title for the email")
    operation: Optional[str] = Field(None, description="Operation")


class MailjetSendTool(BaseTool):
    name: str = "mailjet_send"
    connector_id: str = "nodes-base.mailjet"
    description: str = "Tool for mailjet send operation - send operation"
    args_schema: type[BaseModel] | None = MailjetSendToolInput
    credentials: Optional[MailjetCredentials] = None
