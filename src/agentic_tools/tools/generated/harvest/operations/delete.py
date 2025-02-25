from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HarvestDeleteToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    spentDate: Optional[str] = Field(None, description="Date the expense occurred")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the client you want to delete")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    taskId: Optional[str] = Field(None, description="The ID of the task to associate with the time entry")
    name: Optional[str] = Field(None, description="The name of the client")
    clientId: Optional[str] = Field(None, description="The ID of the client associated with this contact")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    firstName: Optional[str] = Field(None, description="The first name of the contact")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    projectId: Optional[str] = Field(None, description="The ID of the project associated with this expense")
    authentication: Optional[str] = Field(None, description="Authentication")


class HarvestDeleteTool(BaseTool):
    name = "harvest_delete"
    description = "Tool for harvest delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the harvest delete operation."""
        # Implement the tool logic here
        return f"Running harvest delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the harvest delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
