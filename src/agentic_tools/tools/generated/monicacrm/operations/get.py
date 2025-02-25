from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MonicacrmGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tagsToRemove: Optional[str] = Field(None, description="tagsToRemove")
    contactFieldTypeId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminderId: Optional[str] = Field(None, description="ID of the reminder to retrieve")
    journalId: Optional[str] = Field(None, description="ID of the journal entry to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contactFieldId: Optional[str] = Field(None, description="ID of the contact field to retrieve")
    tagsToAdd: Optional[str] = Field(None, description="tagsToAdd")
    activityId: Optional[str] = Field(None, description="ID of the activity to retrieve")
    happenedAt: Optional[str] = Field(None, description="Date when the activity happened")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="ID of the task to retrieve")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    callId: Optional[str] = Field(None, description="ID of the call to retrieve")
    conversationId: Optional[str] = Field(None, description="ID of the conversation to retrieve")
    tagId: Optional[str] = Field(None, description="ID of the tag to retrieve")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="ID of the contact to retrieve")
    noteId: Optional[str] = Field(None, description="ID of the note to retrieve")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmGetTool(BaseTool):
    name = "monicacrm_get"
    description = "Tool for monicaCrm get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the monicaCrm get operation."""
        # Implement the tool logic here
        return f"Running monicaCrm get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the monicaCrm get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
