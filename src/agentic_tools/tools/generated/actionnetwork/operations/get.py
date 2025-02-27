from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActionnetworkCredentials

class ActionnetworkGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to retrieve")
    petition_id: Optional[str] = Field(None, description="ID of the petition to retrieve")
    event_id: Optional[str] = Field(None, description="ID of the event whose attendance to retrieve")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    attendance_id: Optional[str] = Field(None, description="ID of the attendance to retrieve")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class ActionnetworkGetTool(BaseTool):
    name: str = "actionnetwork_get"
    connector_id: str = "nodes-base.actionNetwork"
    description: str = "Tool for actionNetwork get operation - get operation"
    args_schema: type[BaseModel] | None = ActionnetworkGetToolInput
    credentials: Optional[ActionnetworkCredentials] = None
