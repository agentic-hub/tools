from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LinearGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issueId: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearGetTool(BaseTool):
    name = "linear_get"
    description = "Tool for linear get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the linear get operation."""
        # Implement the tool logic here
        return f"Running linear get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the linear get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
