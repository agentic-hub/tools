from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnfleetCredentials

class OnfleetAddtaskToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    container_type: Optional[str] = Field(None, description="Container Type")
    container_id: Optional[str] = Field(None, description="The object ID according to the container chosen")
    index: Optional[float] = Field(None, description="The index given indicates the position where the tasks are going to be inserted")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    type: Optional[str] = Field(None, description="Insert Type")
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


class OnfleetAddtaskTool(BaseTool):
    name: str = "onfleet_addtask"
    connector_id: str = "nodes-base.onfleet"
    description: str = "Tool for onfleet addTask operation - addTask operation"
    args_schema: type[BaseModel] | None = OnfleetAddtaskToolInput
    credentials: Optional[OnfleetCredentials] = None
