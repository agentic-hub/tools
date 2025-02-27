from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendgridCredentials

class SendgridSendToolInput(BaseModel):
    content_value: Optional[str] = Field(None, description="Message body of the email to send")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    subject: Optional[str] = Field(None, description="Subject of the email to send")
    dynamic_template_fields: Optional[Dict[str, Any]] = Field(None, description="Dynamic Template Fields")
    from_name: Optional[str] = Field(None, description="Name of the sender of the email")
    operation: Optional[str] = Field(None, description="Operation")
    template_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    content_type: Optional[str] = Field(None, description="MIME type of the email to send")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    to_email: Optional[str] = Field(None, description="Comma-separated list of recipient email addresses")
    from_email: Optional[str] = Field(None, description="Email address of the sender of the email")
    dynamic_template: Optional[bool] = Field(None, description="Whether this email will contain a dynamic template")


class SendgridSendTool(BaseTool):
    name: str = "sendgrid_send"
    connector_id: str = "nodes-base.sendGrid"
    description: str = "Tool for sendGrid send operation - send operation"
    args_schema: type[BaseModel] | None = SendgridSendToolInput
    credentials: Optional[SendgridCredentials] = None
