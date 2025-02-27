from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MonicacrmCredentials

class MonicacrmGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tags_to_remove: Optional[str] = Field(None, description="tagsToRemove")
    contact_field_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminder_id: Optional[str] = Field(None, description="ID of the reminder to retrieve")
    journal_id: Optional[str] = Field(None, description="ID of the journal entry to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contact_field_id: Optional[str] = Field(None, description="ID of the contact field to retrieve")
    tags_to_add: Optional[str] = Field(None, description="tagsToAdd")
    activity_id: Optional[str] = Field(None, description="ID of the activity to retrieve")
    happened_at: Optional[str] = Field(None, description="Date when the activity happened")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="ID of the task to retrieve")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    call_id: Optional[str] = Field(None, description="ID of the call to retrieve")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation to retrieve")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of the contact to retrieve")
    note_id: Optional[str] = Field(None, description="ID of the note to retrieve")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmGetTool(BaseTool):
    name: str = "monicacrm_get"
    description: str = "Tool for monicaCrm get operation - get operation"
    args_schema: type[BaseModel] | None = MonicacrmGetToolInput
    credentials: Optional[MonicacrmCredentials] = None
