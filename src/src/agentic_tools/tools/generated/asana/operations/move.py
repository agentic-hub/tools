from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AsanaMoveToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The workspace to create the task in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    tag: Optional[str] = Field(None, description="The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The plain text of the comment to add")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the task to be moved")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="The task to operate on")
    name: Optional[str] = Field(None, description="The name of the subtask to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="The project where the task will be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Properties of the task comment")
    projectId: Optional[str] = Field(None, description="Project to show the sections of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="Authentication")
    section: Optional[str] = Field(None, description="The Section to move the task to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    otherProperties: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class AsanaMoveTool(BaseTool):
    name = "asana_move"
    description = "Tool for asana move operation - move operation"
    
    def _run(self, **kwargs):
        """Run the asana move operation."""
        # Implement the tool logic here
        return f"Running asana move operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the asana move operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
