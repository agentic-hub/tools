from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PlivoSendToolInput(BaseModel):
    media_urls: Optional[str] = Field(None, description="Comma-separated list of media URLs of the files from your file server")
    to: Optional[str] = Field(None, description="Phone number to send the message to")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message to send")
    from: Optional[str] = Field(None, description="Plivo Number to send the SMS from")
    operation: Optional[str] = Field(None, description="Operation")


class PlivoSendTool(BaseTool):
    name = "plivo_send"
    description = "Tool for plivo send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the plivo send operation."""
        # Implement the tool logic here
        return f"Running plivo send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the plivo send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
