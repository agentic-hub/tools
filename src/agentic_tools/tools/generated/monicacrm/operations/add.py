from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MonicacrmCredentials

class MonicacrmAddToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the message")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    tags_to_remove: Optional[str] = Field(None, description="tagsToRemove")
    contact_field_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    reminder_id: Optional[str] = Field(None, description="ID of the reminder to delete")
    journal_id: Optional[str] = Field(None, description="ID of the journal entry to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contact_field_id: Optional[str] = Field(None, description="ID of the contactField to delete")
    tags_to_add: Optional[str] = Field(None, description="tagsToAdd")
    activity_id: Optional[str] = Field(None, description="ID of the activity to delete")
    happened_at: Optional[str] = Field(None, description="Date when the activity happened")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    call_id: Optional[str] = Field(None, description="ID of the call to delete")
    conversation_id: Optional[str] = Field(None, description="ID of the contact whose conversation")
    tag_id: Optional[str] = Field(None, description="ID of the tag to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    written_by_me: Optional[str] = Field(None, description="Author of the message")
    contact_id: Optional[str] = Field(None, description="ID of the contact to add a tag to")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    written_at: Optional[str] = Field(None, description="Date when the message was written")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmAddTool(BaseTool):
    name: str = "monicacrm_add"
    connector_id: str = "nodes-base.monicaCrm"
    description: str = "Tool for monicaCrm add operation - add operation"
    args_schema: type[BaseModel] | None = MonicacrmAddToolInput
    credentials: Optional[MonicacrmCredentials] = None
