from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LinearDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issueId: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearDeleteTool(BaseTool):
    name = "linear_delete"
    description = "Tool for linear delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the linear delete operation."""
        # Implement the tool logic here
        return f"Running linear delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the linear delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
