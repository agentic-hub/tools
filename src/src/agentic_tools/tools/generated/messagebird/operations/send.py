from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MessagebirdSendToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    message: Optional[str] = Field(None, description="The message to be send")
    recipients: Optional[str] = Field(None, description="All recipients separated by commas")
    originator: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class MessagebirdSendTool(BaseTool):
    name = "messagebird_send"
    description = "Tool for messageBird send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the messageBird send operation."""
        # Implement the tool logic here
        return f"Running messageBird send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the messageBird send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
