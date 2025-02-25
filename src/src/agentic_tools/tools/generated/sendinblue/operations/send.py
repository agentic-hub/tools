from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueSendToolInput(BaseModel):
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    sendHTML: Optional[bool] = Field(None, description="Send HTML")
    textContent: Optional[str] = Field(None, description="Text content of the message")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    htmlContent: Optional[str] = Field(None, description="HTML content of the message")
    subject: Optional[str] = Field(None, description="Subject of the email")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")
    sender: Optional[str] = Field(None, description="Sender")


class SendinblueSendTool(BaseTool):
    name = "sendinblue_send"
    description = "Tool for sendInBlue send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the sendInBlue send operation."""
        # Implement the tool logic here
        return f"Running sendInBlue send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
