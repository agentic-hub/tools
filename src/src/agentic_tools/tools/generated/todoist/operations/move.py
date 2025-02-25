from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TodoistMoveToolInput(BaseModel):
    taskId: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    project: Optional[str] = Field(None, description="ID")
    authentication: Optional[str] = Field(None, description="Authentication")
    section: Optional[str] = Field(None, description="Section to which you want move the task. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistMoveTool(BaseTool):
    name = "todoist_move"
    description = "Tool for todoist move operation - move operation"
    
    def _run(self, **kwargs):
        """Run the todoist move operation."""
        # Implement the tool logic here
        return f"Running todoist move operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the todoist move operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
