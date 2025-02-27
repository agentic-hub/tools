from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MonicacrmCredentials

class MonicacrmUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tags_to_remove: Optional[str] = Field(None, description="tagsToRemove")
    contact_field_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminder_id: Optional[str] = Field(None, description="ID of the reminder to update")
    journal_id: Optional[str] = Field(None, description="ID of the journal entry to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contact_field_id: Optional[str] = Field(None, description="ID of the contact field to update")
    tags_to_add: Optional[str] = Field(None, description="tagsToAdd")
    activity_id: Optional[str] = Field(None, description="ID of the activity to update")
    happened_at: Optional[str] = Field(None, description="Date when the conversation happened")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="ID of the task to update")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    call_id: Optional[str] = Field(None, description="ID of the call to update")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation to update")
    tag_id: Optional[str] = Field(None, description="ID of the tag to update")
    message_id: Optional[str] = Field(None, description="ID of the message to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of the contact to update")
    note_id: Optional[str] = Field(None, description="ID of the note to update")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmUpdateTool(BaseTool):
    name: str = "monicacrm_update"
    description: str = "Tool for monicaCrm update operation - update operation"
    args_schema: type[BaseModel] | None = MonicacrmUpdateToolInput
    credentials: Optional[MonicacrmCredentials] = None
