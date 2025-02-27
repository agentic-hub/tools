from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshserviceCredentials

class FreshserviceCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    release_id: Optional[str] = Field(None, description="ID of the release to delete")
    software_id: Optional[str] = Field(None, description="ID of the software application to delete")
    location_id: Optional[str] = Field(None, description="ID of the location to delete")
    description: Optional[str] = Field(None, description="HTML supported")
    announcement_id: Optional[str] = Field(None, description="ID of the announcement to delete")
    body_html: Optional[str] = Field(None, description="HTML supported")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agent_group_id: Optional[str] = Field(None, description="ID of the agent group to delete")
    visible_from: Optional[str] = Field(None, description="Timestamp at which announcement becomes active")
    subject: Optional[str] = Field(None, description="Subject")
    ticket_id: Optional[str] = Field(None, description="ID of the ticket to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    asset_type_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    agent_id: Optional[str] = Field(None, description="ID of the agent to delete")
    requester_id: Optional[str] = Field(None, description="ID of the requester of the change. Choose from the list or specify an ID. You can also specify the ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    change_id: Optional[str] = Field(None, description="ID of the change to delete")
    release_type: Optional[str] = Field(None, description="Release Type")
    roles: Optional[Dict[str, Any]] = Field(None, description="Role to assign to the agent")
    problem_id: Optional[str] = Field(None, description="ID of the problem to delete")
    department_id: Optional[str] = Field(None, description="ID of the department to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    planned_end_date: Optional[str] = Field(None, description="Planned End Date")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    visibility: Optional[str] = Field(None, description="Visibility")
    status: Optional[str] = Field(None, description="Status")
    application_type: Optional[str] = Field(None, description="Application Type")
    due_by: Optional[str] = Field(None, description="Date when the problem is due to be solved")
    priority: Optional[str] = Field(None, description="Priority")
    title: Optional[str] = Field(None, description="Title")
    planned_start_date: Optional[str] = Field(None, description="Planned Start Date")
    requester_group_id: Optional[str] = Field(None, description="ID of the requester group to delete")
    product_id: Optional[str] = Field(None, description="ID of the product to delete")
    primary_email: Optional[str] = Field(None, description="Primary Email")


class FreshserviceCreateTool(BaseTool):
    name: str = "freshservice_create"
    connector_id: str = "nodes-base.freshservice"
    description: str = "Tool for freshservice create operation - create operation"
    args_schema: type[BaseModel] | None = FreshserviceCreateToolInput
    credentials: Optional[FreshserviceCredentials] = None
