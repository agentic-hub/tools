from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshworkscrmCredentials

class FreshworkscrmCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointment_id: Optional[str] = Field(None, description="ID of the appointment to delete")
    sales_activity_type_id: Optional[str] = Field(None, description="ID of a sales activity type for which the sales activity is created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    description: Optional[str] = Field(None, description="Content of the note")
    from_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last name of the contact")
    from_date: Optional[str] = Field(None, description="Timestamp that denotes the start of appointment. Start date if this is an all-day appointment.")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of the account to delete")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetable_type: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    end_date: Optional[str] = Field(None, description="Timestamp that denotes the end of sales activity")
    entities: Optional[str] = Field(None, description="entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    end_date: Optional[str] = Field(None, description="Timestamp that denotes the end of appointment. End date if this is an all-day appointment.")
    emails: Optional[str] = Field(None, description="Email addresses of the contact")
    deal_id: Optional[str] = Field(None, description="ID of the deal to delete")
    sales_activity_id: Optional[str] = Field(None, description="ID of the salesActivity to delete")
    first_name: Optional[str] = Field(None, description="First name of the contact")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    owner_id: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    due_date: Optional[str] = Field(None, description="Timestamp that denotes when the task is due to be completed")
    contact_id: Optional[str] = Field(None, description="ID of the contact to delete")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the appointment")
    amount: Optional[float] = Field(None, description="Value of the deal")
    attendees: Optional[Dict[str, Any]] = Field(None, description="Attendees")


class FreshworkscrmCreateTool(BaseTool):
    name: str = "freshworkscrm_create"
    description: str = "Tool for freshworksCrm create operation - create operation"
    args_schema: type[BaseModel] | None = FreshworkscrmCreateToolInput
    credentials: Optional[FreshworkscrmCredentials] = None
