from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshworkscrmLookupToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointmentId: Optional[str] = Field(None, description="ID of the appointment to delete")
    searchField: Optional[str] = Field(None, description="Field against which the entities have to be searched")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    customFieldValue: Optional[str] = Field(None, description="Custom Field Value")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="ID of the account to delete")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetableType: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    customFieldName: Optional[str] = Field(None, description="Custom Field Name")
    entities: Optional[str] = Field(None, description="entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    dealId: Optional[str] = Field(None, description="ID of the deal to delete")
    salesActivityId: Optional[str] = Field(None, description="ID of the salesActivity to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    ownerId: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    fieldValue: Optional[str] = Field(None, description="Field Value")
    contactId: Optional[str] = Field(None, description="ID of the contact to delete")
    noteId: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the appointment")


class FreshworkscrmLookupTool(BaseTool):
    name = "freshworkscrm_lookup"
    description = "Tool for freshworksCrm lookup operation - lookup operation"
    
    def _run(self, **kwargs):
        """Run the freshworksCrm lookup operation."""
        # Implement the tool logic here
        return f"Running freshworksCrm lookup operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshworksCrm lookup operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
