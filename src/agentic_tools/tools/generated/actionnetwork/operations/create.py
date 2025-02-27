from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActionnetworkCredentials

class ActionnetworkCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email_addresses: Optional[Dict[str, Any]] = Field(None, description="Person’s email addresses")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the tag to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to create an attendance for")
    petition_id: Optional[str] = Field(None, description="ID of the petition to sign")
    event_id: Optional[str] = Field(None, description="ID of the event to create an attendance for")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class ActionnetworkCreateTool(BaseTool):
    name: str = "actionnetwork_create"
    description: str = "Tool for actionNetwork create operation - create operation"
    args_schema: type[BaseModel] | None = ActionnetworkCreateToolInput
    credentials: Optional[ActionnetworkCredentials] = None
