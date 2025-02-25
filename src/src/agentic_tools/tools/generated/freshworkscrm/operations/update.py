from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshworkscrmUpdateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointmentId: Optional[str] = Field(None, description="ID of the appointment to update")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="ID of the account to update")
    taskId: Optional[str] = Field(None, description="ID of the task to update")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetableType: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    entities: Optional[str] = Field(None, description="entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    dealId: Optional[str] = Field(None, description="ID of the deal to update")
    salesActivityId: Optional[str] = Field(None, description="ID of the salesActivity to update")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    ownerId: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contactId: Optional[str] = Field(None, description="ID of the contact to update")
    noteId: Optional[str] = Field(None, description="ID of the note to update")
    title: Optional[str] = Field(None, description="Title of the appointment")


class FreshworkscrmUpdateTool(BaseTool):
    name = "freshworkscrm_update"
    description = "Tool for freshworksCrm update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the freshworksCrm update operation."""
        # Implement the tool logic here
        return f"Running freshworksCrm update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshworksCrm update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
