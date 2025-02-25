from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwilioSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    toWhatsapp: Optional[bool] = Field(None, description="Whether the message should be sent to WhatsApp")
    operation: Optional[str] = Field(None, description="Operation")


class TwilioSendTool(BaseTool):
    name = "twilio_send"
    description = "Tool for twilio send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the twilio send operation."""
        # Implement the tool logic here
        return f"Running twilio send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twilio send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
