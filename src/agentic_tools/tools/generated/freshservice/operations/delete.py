from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshserviceCredentials

class FreshserviceDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    release_id: Optional[str] = Field(None, description="ID of the release to delete")
    software_id: Optional[str] = Field(None, description="ID of the software application to delete")
    location_id: Optional[str] = Field(None, description="ID of the location to delete")
    announcement_id: Optional[str] = Field(None, description="ID of the announcement to delete")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agent_group_id: Optional[str] = Field(None, description="ID of the agent group to delete")
    subject: Optional[str] = Field(None, description="Subject")
    ticket_id: Optional[str] = Field(None, description="ID of the ticket to delete")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    asset_type_id: Optional[str] = Field(None, description="ID of the asset type to delete")
    agent_id: Optional[str] = Field(None, description="ID of the agent to delete")
    requester_id: Optional[str] = Field(None, description="ID of the requester to delete")
    change_id: Optional[str] = Field(None, description="ID of the change to delete")
    problem_id: Optional[str] = Field(None, description="ID of the problem to delete")
    department_id: Optional[str] = Field(None, description="ID of the department to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    planned_end_date: Optional[str] = Field(None, description="Planned End Date")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    planned_start_date: Optional[str] = Field(None, description="Planned Start Date")
    requester_group_id: Optional[str] = Field(None, description="ID of the requester group to delete")
    product_id: Optional[str] = Field(None, description="ID of the product to delete")


class FreshserviceDeleteTool(BaseTool):
    name: str = "freshservice_delete"
    connector_id: str = "nodes-base.freshservice"
    description: str = "Tool for freshservice delete operation - delete operation"
    args_schema: type[BaseModel] | None = FreshserviceDeleteToolInput
    credentials: Optional[FreshserviceCredentials] = None
