from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MonicacrmCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    contacts: Optional[str] = Field(None, description="Comma-separated list of IDs of the contacts to associate the activity with")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    summary: Optional[str] = Field(None, description="Brief description of the activity - max 255 characters")
    tagsToRemove: Optional[str] = Field(None, description="tagsToRemove")
    contactFieldTypeId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    initialDate: Optional[str] = Field(None, description="Date of the reminder")
    frequencyType: Optional[str] = Field(None, description="Type of frequency of the reminder")
    reminderId: Optional[str] = Field(None, description="ID of the reminder to delete")
    post: Optional[str] = Field(None, description="Content of the journal entry - max 100,000 characters")
    journalId: Optional[str] = Field(None, description="ID of the journal entry to delete")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contactFieldId: Optional[str] = Field(None, description="ID of the contactField to delete")
    tagsToAdd: Optional[str] = Field(None, description="tagsToAdd")
    activityId: Optional[str] = Field(None, description="ID of the activity to delete")
    happenedAt: Optional[str] = Field(None, description="Date when the activity happened")
    activityTypeId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    genderId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    callId: Optional[str] = Field(None, description="ID of the call to delete")
    conversationId: Optional[str] = Field(None, description="ID of the conversation to delete")
    frequencyNumber: Optional[float] = Field(None, description="Interval for the reminder")
    tagId: Optional[str] = Field(None, description="ID of the tag to delete")
    body: Optional[str] = Field(None, description="Body of the note - max 100,000 characters")
    calledAt: Optional[str] = Field(None, description="Date when the call happened")
    firstName: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="ID of the contact to associate the call with")
    noteId: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmCreateTool(BaseTool):
    name = "monicacrm_create"
    description = "Tool for monicaCrm create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the monicaCrm create operation."""
        # Implement the tool logic here
        return f"Running monicaCrm create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the monicaCrm create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
