from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinRemovefirstToolInput(BaseModel):
    binId: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinRemovefirstTool(BaseTool):
    name = "postbin_removefirst"
    description = "Tool for postBin removeFirst operation - removeFirst operation"
    
    def _run(self, **kwargs):
        """Run the postBin removeFirst operation."""
        # Implement the tool logic here
        return f"Running postBin removeFirst operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the postBin removeFirst operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
