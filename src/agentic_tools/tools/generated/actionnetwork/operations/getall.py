from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActionnetworkCredentials

class ActionnetworkGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to create an attendance for")
    petition_id: Optional[str] = Field(None, description="ID of the petition whose signatures to retrieve")
    event_id: Optional[str] = Field(None, description="ID of the event to create an attendance for")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class ActionnetworkGetallTool(BaseTool):
    name: str = "actionnetwork_getall"
    connector_id: str = "nodes-base.actionNetwork"
    description: str = "Tool for actionNetwork getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ActionnetworkGetallToolInput
    credentials: Optional[ActionnetworkCredentials] = None
