from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HarvestCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    budgetBy: Optional[str] = Field(None, description="The email of the user or \"none\"")
    isBillable: Optional[bool] = Field(None, description="Whether the project is billable or not")
    spentDate: Optional[str] = Field(None, description="Date the expense occurred")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    lastName: Optional[str] = Field(None, description="The last name of the user")
    email: Optional[str] = Field(None, description="The email of the user")
    billBy: Optional[str] = Field(None, description="The method by which the project is invoiced")
    id: Optional[str] = Field(None, description="The ID of the client you are retrieving")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    taskId: Optional[str] = Field(None, description="The ID of the task to associate with the time entry")
    name: Optional[str] = Field(None, description="The name of the client")
    expenseCategoryId: Optional[str] = Field(None, description="The ID of the expense category this expense is being tracked against")
    clientId: Optional[str] = Field(None, description="The ID of the client associated with this contact")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    firstName: Optional[str] = Field(None, description="The first name of the contact")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    projectId: Optional[str] = Field(None, description="The ID of the project associated with this expense")
    authentication: Optional[str] = Field(None, description="Authentication")


class HarvestCreateTool(BaseTool):
    name = "harvest_create"
    description = "Tool for harvest create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the harvest create operation."""
        # Implement the tool logic here
        return f"Running harvest create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the harvest create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
