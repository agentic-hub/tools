from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AsanaSearchToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The workspace in which the task is searched. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    tag: Optional[str] = Field(None, description="The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The plain text of the comment to add")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    searchTaskProperties: Optional[Dict[str, Any]] = Field(None, description="Properties to search for")
    id: Optional[str] = Field(None, description="The ID of the task to delete")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="The task to operate on")
    name: Optional[str] = Field(None, description="The name of the subtask to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="The project where the task will be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Properties of the task comment")
    authentication: Optional[str] = Field(None, description="Authentication")
    otherProperties: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class AsanaSearchTool(BaseTool):
    name = "asana_search"
    description = "Tool for asana search operation - search operation"
    
    def _run(self, **kwargs):
        """Run the asana search operation."""
        # Implement the tool logic here
        return f"Running asana search operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the asana search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
