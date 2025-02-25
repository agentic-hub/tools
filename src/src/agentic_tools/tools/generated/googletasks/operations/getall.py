from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogletasksGetallToolInput(BaseModel):
    taskId: Optional[str] = Field(None, description="Task ID")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksGetallTool(BaseTool):
    name = "googletasks_getall"
    description = "Tool for googleTasks getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the googleTasks getAll operation."""
        # Implement the tool logic here
        return f"Running googleTasks getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleTasks getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
