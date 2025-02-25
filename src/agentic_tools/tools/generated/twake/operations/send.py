from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwakeSendToolInput(BaseModel):
    content: Optional[str] = Field(None, description="Message content")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    channelId: Optional[str] = Field(None, description="Channel's ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class TwakeSendTool(BaseTool):
    name = "twake_send"
    description = "Tool for twake send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the twake send operation."""
        # Implement the tool logic here
        return f"Running twake send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twake send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
