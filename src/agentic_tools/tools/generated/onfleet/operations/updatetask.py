from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnfleetCredentials

class OnfleetUpdatetaskToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    container_id: Optional[str] = Field(None, description="The object ID according to the container chosen")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="The phone of the recipient for lookup")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    tasks: Optional[str] = Field(None, description="Task's ID that are going to be used")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class OnfleetUpdatetaskTool(BaseTool):
    name: str = "onfleet_updatetask"
    connector_id: str = "nodes-base.onfleet"
    description: str = "Tool for onfleet updateTask operation - updateTask operation"
    args_schema: type[BaseModel] | None = OnfleetUpdatetaskToolInput
    credentials: Optional[OnfleetCredentials] = None
