from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosofttodoDeleteToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    taskId: Optional[str] = Field(None, description="Task ID")
    taskListId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    listId: Optional[str] = Field(None, description="The identifier of the list, unique in the user's mailbox")
    linkedResourceId: Optional[str] = Field(None, description="Linked Resource ID")
    displayName: Optional[str] = Field(None, description="Field indicating title of the linked entity")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosofttodoDeleteTool(BaseTool):
    name = "microsofttodo_delete"
    description = "Tool for microsoftToDo delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the microsoftToDo delete operation."""
        # Implement the tool logic here
        return f"Running microsoftToDo delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftToDo delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
