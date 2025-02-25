from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GotifyDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    messageId: Optional[str] = Field(None, description="Message ID")


class GotifyDeleteTool(BaseTool):
    name = "gotify_delete"
    description = "Tool for gotify delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the gotify delete operation."""
        # Implement the tool logic here
        return f"Running gotify delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gotify delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
