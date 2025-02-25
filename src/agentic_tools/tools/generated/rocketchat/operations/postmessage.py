from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RocketchatPostmessageToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    attachmentsJson: Optional[str] = Field(None, description="Attachments")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    channel: Optional[str] = Field(None, description="The channel name with the prefix in front of it")
    operation: Optional[str] = Field(None, description="Operation")
    text: Optional[str] = Field(None, description="The text of the message to send, is optional because of attachments")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachments: Optional[List[Any]] = Field(None, description="Attachments")


class RocketchatPostmessageTool(BaseTool):
    name = "rocketchat_postmessage"
    description = "Tool for rocketchat postMessage operation - postMessage operation"
    
    def _run(self, **kwargs):
        """Run the rocketchat postMessage operation."""
        # Implement the tool logic here
        return f"Running rocketchat postMessage operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rocketchat postMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
