from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshserviceCredentials

class FreshserviceUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    release_id: Optional[str] = Field(None, description="ID of the release to update")
    software_id: Optional[str] = Field(None, description="ID of the software application to update")
    location_id: Optional[str] = Field(None, description="ID of the location to update")
    announcement_id: Optional[str] = Field(None, description="ID of the announcement to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    agent_group_id: Optional[str] = Field(None, description="ID of the agent group to update")
    subject: Optional[str] = Field(None, description="Subject")
    ticket_id: Optional[str] = Field(None, description="ID of the ticket to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    asset_type_id: Optional[str] = Field(None, description="ID of the asset type to update")
    agent_id: Optional[str] = Field(None, description="ID of the agent to update")
    requester_id: Optional[str] = Field(None, description="ID of the requester to update")
    change_id: Optional[str] = Field(None, description="ID of the change to update")
    problem_id: Optional[str] = Field(None, description="ID of the problem to update")
    department_id: Optional[str] = Field(None, description="ID of the department to update")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    planned_end_date: Optional[str] = Field(None, description="Planned End Date")
    first_name: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    planned_start_date: Optional[str] = Field(None, description="Planned Start Date")
    requester_group_id: Optional[str] = Field(None, description="ID of the requester group to update")
    product_id: Optional[str] = Field(None, description="ID of the product to update")


class FreshserviceUpdateTool(BaseTool):
    name: str = "freshservice_update"
    description: str = "Tool for freshservice update operation - update operation"
    args_schema: type[BaseModel] | None = FreshserviceUpdateToolInput
    credentials: Optional[FreshserviceCredentials] = None
