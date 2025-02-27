from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActionnetworkCredentials

class Actionnetwork__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to retrieve")
    person_id: Optional[str] = Field(None, description="ID of the person to create an attendance for")
    petition_id: Optional[str] = Field(None, description="ID of the petition to retrieve")
    event_id: Optional[str] = Field(None, description="ID of the event to create an attendance for")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class Actionnetwork__custom_api_call__Tool(BaseTool):
    name: str = "actionnetwork___custom_api_call__"
    connector_id: str = "nodes-base.actionNetwork"
    description: str = "Tool for actionNetwork __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Actionnetwork__custom_api_call__ToolInput
    credentials: Optional[ActionnetworkCredentials] = None
