from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ActionnetworkCredentials

class ActionnetworkAddToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    signature_id: Optional[str] = Field(None, description="ID of the signature to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to add. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    person_id: Optional[str] = Field(None, description="ID of the person to add the tag to")
    petition_id: Optional[str] = Field(None, description="ID of the petition to retrieve")
    event_id: Optional[str] = Field(None, description="ID of the event to create an attendance for")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the event to create")
    origin_system: Optional[str] = Field(None, description="Source where the event originated")


class ActionnetworkAddTool(BaseTool):
    name: str = "actionnetwork_add"
    description: str = "Tool for actionNetwork add operation - add operation"
    args_schema: type[BaseModel] | None = ActionnetworkAddToolInput
    credentials: Optional[ActionnetworkCredentials] = None
