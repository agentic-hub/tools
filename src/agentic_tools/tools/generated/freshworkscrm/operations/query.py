from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshworkscrmCredentials

class FreshworkscrmQueryToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    appointment_id: Optional[str] = Field(None, description="ID of the appointment to delete")
    view: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of the account to delete")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    name: Optional[str] = Field(None, description="Name of the account")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    targetable_type: Optional[str] = Field(None, description="Type of the entity for which the note is created")
    entities: Optional[str] = Field(None, description="entities")
    query: Optional[str] = Field(None, description="Enter a term that will be used for searching entities")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    targetable_id: Optional[str] = Field(None, description="ID of the entity for which note is created. The type of entity is selected in \"Target Type\".")
    deal_id: Optional[str] = Field(None, description="ID of the deal to delete")
    sales_activity_id: Optional[str] = Field(None, description="ID of the salesActivity to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    owner_id: Optional[str] = Field(None, description="ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contact_id: Optional[str] = Field(None, description="ID of the contact to delete")
    note_id: Optional[str] = Field(None, description="ID of the note to delete")
    title: Optional[str] = Field(None, description="Title of the appointment")


class FreshworkscrmQueryTool(BaseTool):
    name: str = "freshworkscrm_query"
    description: str = "Tool for freshworksCrm query operation - query operation"
    args_schema: type[BaseModel] | None = FreshworkscrmQueryToolInput
    credentials: Optional[FreshworkscrmCredentials] = None
