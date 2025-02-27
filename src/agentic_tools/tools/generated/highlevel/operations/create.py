from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HighlevelCredentials

class HighlevelCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email or Phone are required to create contact")
    phone: Optional[str] = Field(None, description="Phone or Email are required to create contact. Phone number has to start with a valid <a href=\"https://en.wikipedia.org/wiki/List_of_country_calling_codes\">country code</a> leading with + sign.")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="Task ID")
    opportunity_id: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    contact_identifier: Optional[str] = Field(None, description="Either Email, Phone or Contact ID")
    stage_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    due_date: Optional[str] = Field(None, description="Due Date")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    contact_id: Optional[str] = Field(None, description="Contact the task belongs to")
    pipeline_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    title: Optional[str] = Field(None, description="Title")
    contact_create_notice: Optional[str] = Field(None, description="Create a new contact or update an existing one if email or phone matches (upsert)")


class HighlevelCreateTool(BaseTool):
    name: str = "highlevel_create"
    connector_id: str = "nodes-base.highLevel"
    description: str = "Tool for highLevel create operation - create operation"
    args_schema: type[BaseModel] | None = HighlevelCreateToolInput
    credentials: Optional[HighlevelCredentials] = None
