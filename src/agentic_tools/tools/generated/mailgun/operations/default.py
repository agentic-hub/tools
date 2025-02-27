from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailgunCredentials

class MailgunDefaultToolInput(BaseModel):
    html: Optional[str] = Field(None, description="HTML text message of email")
    to_email: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    bcc_email: Optional[str] = Field(None, description="Bcc Email address of the recipient. Multiple ones can be separated by comma.")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    from_email: Optional[str] = Field(None, description="Email address of the sender optional with name")
    cc_email: Optional[str] = Field(None, description="Cc Email address of the recipient. Multiple ones can be separated by comma.")
    attachments: Optional[str] = Field(None, description="Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated.")


class MailgunDefaultTool(BaseTool):
    name: str = "mailgun_default"
    connector_id: str = "nodes-base.mailgun"
    description: str = "Tool for mailgun default operation - default operation"
    args_schema: type[BaseModel] | None = MailgunDefaultToolInput
    credentials: Optional[MailgunCredentials] = None
