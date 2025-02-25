from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshworkscrmCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointmentId: Optional[str] = Field(None, description="ID of the appointment to delete")
    sales_activity_type_id: Optional[str] = Field(None, description="ID of a sales activity type for which the sales activity is created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    description: Optional[str] = Field(None, description="Content of the note")
    from_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    lastName: Optional[str] = Field(None, description="Last name of the contact")
    fromDate: Optional[str] = Field(None, description="Timestamp that denotes the start of appointment. Start date if this is an all-day appointment.")
    operation: Optional[str] = Field(None, description="Operation")
    accountId: Optional[str] = Field(None, description="ID of the account to delete")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetableType: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    end_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    entities: Optional[str] = Field(None, description="entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    endDate: Optional[str] = Field(None, description="Timestamp that denotes the end of appointment. End date if this is an all-day appointment.")
    emails: Optional[str] = Field(None, description="Email addresses of the contact")
    dealId: Optional[str] = Field(None, description="ID of the deal to delete")
    salesActivityId: Optional[str] = Field(None, description="ID of the salesActivity to delete")
    firstName: Optional[str] = Field(None, description="First name of the contact")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    ownerId: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    dueDate: Optional[str] = Field(None, description="Timestamp that denotes when the task is due to be completed")
    contactId: Optional[str] = Field(None, description="ID of the contact to delete")
    noteId: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the appointment")
    amount: Optional[float] = Field(None, description="Value of the deal")
    attendees: Optional[Dict[str, Any]] = Field(None, description="Attendees")


class FreshworkscrmCreateTool(BaseTool):
    name = "freshworkscrm_create"
    description = "Tool for freshworksCrm create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the freshworksCrm create operation."""
        # Implement the tool logic here
        return f"Running freshworksCrm create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshworksCrm create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
