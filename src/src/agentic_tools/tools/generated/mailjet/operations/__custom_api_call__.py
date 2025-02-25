from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Mailjet__custom_api_call__ToolInput(BaseModel):
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


class Mailjet__custom_api_call__Tool(BaseTool):
    name = "mailjet___custom_api_call__"
    description = "Tool for mailjet __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the mailjet __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running mailjet __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailjet __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
