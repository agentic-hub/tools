from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailjetSendtemplateToolInput(BaseModel):
    templateId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    variablesJson: Optional[str] = Field(None, description="HTML text message of email")
    toEmail: Optional[str] = Field(None, description="Email address of the recipient. Multiple ones can be separated by comma.")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    variablesUi: Optional[Dict[str, Any]] = Field(None, description="Variables")
    subject: Optional[str] = Field(None, description="Subject line of the email")
    text: Optional[str] = Field(None, description="Plain text message of email")
    fromEmail: Optional[str] = Field(None, description="The title for the email")
    operation: Optional[str] = Field(None, description="Operation")


class MailjetSendtemplateTool(BaseTool):
    name = "mailjet_sendtemplate"
    description = "Tool for mailjet sendTemplate operation - sendTemplate operation"
    
    def _run(self, **kwargs):
        """Run the mailjet sendTemplate operation."""
        # Implement the tool logic here
        return f"Running mailjet sendTemplate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailjet sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
