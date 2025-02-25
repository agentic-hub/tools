from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogletasksGetToolInput(BaseModel):
    taskId: Optional[str] = Field(None, description="Task ID")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksGetTool(BaseTool):
    name = "googletasks_get"
    description = "Tool for googleTasks get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the googleTasks get operation."""
        # Implement the tool logic here
        return f"Running googleTasks get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleTasks get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
