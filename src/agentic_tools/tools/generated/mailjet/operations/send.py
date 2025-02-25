from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailjetSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="Message recipient. Should be between 3 and 15 characters in length. The number always starts with a plus sign followed by a country code, followed by the number. Phone numbers are expected to comply with the E.164 format.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    html: Optional[str] = Field(None, description="HTML text message of email")
    variablesJson: Optional[str] = Field(None, description="HTML text message of email")
    toEmail: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    variablesUi: Optional[Dict[str, Any]] = Field(None, description="Variables")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    from: Optional[str] = Field(None, description="Customizable sender name. Should be between 3 and 11 characters in length, only alphanumeric characters are allowed.")
    text: Optional[str] = Field(None, description="Plain text message of email")
    fromEmail: Optional[str] = Field(None, description="The title for the email")
    operation: Optional[str] = Field(None, description="Operation")


class MailjetSendTool(BaseTool):
    name = "mailjet_send"
    description = "Tool for mailjet send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the mailjet send operation."""
        # Implement the tool logic here
        return f"Running mailjet send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailjet send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
