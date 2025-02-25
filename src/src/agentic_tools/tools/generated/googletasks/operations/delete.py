from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogletasksDeleteToolInput(BaseModel):
    taskId: Optional[str] = Field(None, description="Task ID")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksDeleteTool(BaseTool):
    name = "googletasks_delete"
    description = "Tool for googleTasks delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the googleTasks delete operation."""
        # Implement the tool logic here
        return f"Running googleTasks delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleTasks delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
