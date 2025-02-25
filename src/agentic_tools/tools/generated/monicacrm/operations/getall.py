from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MonicacrmGetallToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tagsToRemove: Optional[str] = Field(None, description="tagsToRemove")
    contactFieldTypeId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminderId: Optional[str] = Field(None, description="ID of the reminder to delete")
    journalId: Optional[str] = Field(None, description="ID of the journal entry to delete")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contactFieldId: Optional[str] = Field(None, description="ID of the contactField to delete")
    tagsToAdd: Optional[str] = Field(None, description="tagsToAdd")
    activityId: Optional[str] = Field(None, description="ID of the activity to delete")
    happenedAt: Optional[str] = Field(None, description="Date when the activity happened")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    callId: Optional[str] = Field(None, description="ID of the call to delete")
    conversationId: Optional[str] = Field(None, description="ID of the conversation to delete")
    tagId: Optional[str] = Field(None, description="ID of the tag to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="ID of the contact whose fields to retrieve")
    noteId: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmGetallTool(BaseTool):
    name = "monicacrm_getall"
    description = "Tool for monicaCrm getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the monicaCrm getAll operation."""
        # Implement the tool logic here
        return f"Running monicaCrm getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the monicaCrm getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
