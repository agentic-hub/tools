from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Msg91SendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number, with coutry code, to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class Msg91SendTool(BaseTool):
    name = "msg91_send"
    description = "Tool for msg91 send operation - send operation"
    
    def _run(self, **kwargs):
        """Run the msg91 send operation."""
        # Implement the tool logic here
        return f"Running msg91 send operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the msg91 send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
