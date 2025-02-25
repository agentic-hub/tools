from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MessagebirdGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MessagebirdGetTool(BaseTool):
    name = "messagebird_get"
    description = "Tool for messageBird get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the messageBird get operation."""
        # Implement the tool logic here
        return f"Running messageBird get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the messageBird get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
