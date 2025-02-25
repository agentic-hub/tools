from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FlowGetallToolInput(BaseModel):
    taskId: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    workspaceId: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowGetallTool(BaseTool):
    name = "flow_getall"
    description = "Tool for flow getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the flow getAll operation."""
        # Implement the tool logic here
        return f"Running flow getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the flow getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
