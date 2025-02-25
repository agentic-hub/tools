from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LinearGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    issueId: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearGetallTool(BaseTool):
    name = "linear_getall"
    description = "Tool for linear getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the linear getAll operation."""
        # Implement the tool logic here
        return f"Running linear getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the linear getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
