from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailjetCredentials

class Mailjet__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    variables_json: Optional[str] = Field(None, description="HTML text message of email")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    variables_ui: Optional[Dict[str, Any]] = Field(None, description="Variables")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    from_email: Optional[str] = Field(None, description="The title for the email")
    operation: Optional[str] = Field(None, description="Operation")


class Mailjet__custom_api_call__Tool(BaseTool):
    name: str = "mailjet___custom_api_call__"
    connector_id: str = "nodes-base.mailjet"
    description: str = "Tool for mailjet __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Mailjet__custom_api_call__ToolInput
    credentials: Optional[MailjetCredentials] = None
