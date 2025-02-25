from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridSendToolInput(BaseModel):
    contentValue: Optional[str] = Field(None, description="Message body of the email to send")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    subject: Optional[str] = Field(None, description="Subject of the email to send")
    dynamicTemplateFields: Optional[Dict[str, Any]] = Field(None, description="Dynamic Template Fields")
    fromName: Optional[str] = Field(None, description="Name of the sender of the email")
    operation: Optional[str] = Field(None, description="Operation")
    templateId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="ID of the list")
    contentType: Optional[str] = Field(None, description="MIME type of the email to send")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    toEmail: Optional[str] = Field(None, description="Comma-separated list of recipient email addresses")
    fromEmail: Optional[str] = Field(None, description="Email address of the sender of the email")
    dynamicTemplate: Optional[bool] = Field(None, description="Whether this email will contain a dynamic template")


class SendgridSendTool(BaseTool):
    name = "sendgrid_send"
    description = "Tool for sendGrid send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the sendGrid send operation."""
        # Implement the tool logic here
        return f"Running sendGrid send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
