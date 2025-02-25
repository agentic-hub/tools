from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MailerliteGetToolInput(BaseModel):
    subscriberId: Optional[str] = Field(None, description="Email of subscriber to get")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MailerliteGetTool(BaseTool):
    name = "mailerlite_get"
    description = "Tool for mailerLite get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the mailerLite get operation."""
        # Implement the tool logic here
        return f"Running mailerLite get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mailerLite get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
