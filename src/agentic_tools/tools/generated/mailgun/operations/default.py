from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailgunDefaultToolInput(BaseModel):
    html: Optional[str] = Field(None, description="HTML text message of email")
    toEmail: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    bccEmail: Optional[str] = Field(None, description="Bcc Email address of the recipient. Multiple ones can be separated by comma.")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    fromEmail: Optional[str] = Field(None, description="Email address of the sender optional with name")
    ccEmail: Optional[str] = Field(None, description="Cc Email address of the recipient. Multiple ones can be separated by comma.")
    attachments: Optional[str] = Field(None, description="Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated.")


class MailgunDefaultTool(BaseTool):
    name = "mailgun_default"
    description = "Tool for mailgun default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the mailgun default operation."""
        # Implement the tool logic here
        return f"Running mailgun default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailgun default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
