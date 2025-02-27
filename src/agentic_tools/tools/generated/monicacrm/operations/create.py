from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MonicacrmCredentials

class MonicacrmCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Description of the call - max 100,000 characters")
    contacts: Optional[str] = Field(None, description="Comma-separated list of IDs of the contacts to associate the activity with")
    data: Optional[str] = Field(None, description="Content of the contact field - max 255 characters")
    summary: Optional[str] = Field(None, description="Brief description of the activity - max 255 characters")
    tags_to_remove: Optional[str] = Field(None, description="tagsToRemove")
    contact_field_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    initial_date: Optional[str] = Field(None, description="Date of the reminder")
    frequency_type: Optional[str] = Field(None, description="Type of frequency of the reminder")
    reminder_id: Optional[str] = Field(None, description="ID of the reminder to delete")
    post: Optional[str] = Field(None, description="Content of the journal entry - max 100,000 characters")
    journal_id: Optional[str] = Field(None, description="ID of the journal entry to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    contact_field_id: Optional[str] = Field(None, description="ID of the contactField to delete")
    tags_to_add: Optional[str] = Field(None, description="tagsToAdd")
    activity_id: Optional[str] = Field(None, description="ID of the activity to delete")
    happened_at: Optional[str] = Field(None, description="Date when the activity happened")
    activity_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the tag - max 250 characters")
    gender_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    call_id: Optional[str] = Field(None, description="ID of the call to delete")
    conversation_id: Optional[str] = Field(None, description="ID of the conversation to delete")
    frequency_number: Optional[float] = Field(None, description="Interval for the reminder")
    tag_id: Optional[str] = Field(None, description="ID of the tag to delete")
    body: Optional[str] = Field(None, description="Body of the note - max 100,000 characters")
    called_at: Optional[str] = Field(None, description="Date when the call happened")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of the contact to associate the call with")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the journal entry - max 250 characters")


class MonicacrmCreateTool(BaseTool):
    name: str = "monicacrm_create"
    connector_id: str = "nodes-base.monicaCrm"
    description: str = "Tool for monicaCrm create operation - create operation"
    args_schema: type[BaseModel] | None = MonicacrmCreateToolInput
    credentials: Optional[MonicacrmCredentials] = None
