from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZulipSendprivateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the message")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    userId: Optional[str] = Field(None, description="The ID of user to get")
    additionalFieldsJson: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    streamId: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    messageId: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class ZulipSendprivateTool(BaseTool):
    name = "zulip_sendprivate"
    description = "Tool for zulip sendPrivate operation - sendPrivate operation"
    
    def _run(self, **kwargs):
        """Run the zulip sendPrivate operation."""
        # Implement the tool logic here
        return f"Running zulip sendPrivate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zulip sendPrivate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
