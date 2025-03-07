from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MispCredentials

class Misp__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    feed_id: Optional[str] = Field(None, description="UUID or numeric ID of the feed")
    user_id: Optional[str] = Field(None, description="Numeric ID of the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organisation_id: Optional[str] = Field(None, description="UUID or numeric ID of the organisation")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attribute_id: Optional[str] = Field(None, description="UUID or numeric ID of the attribute")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID of the event to attach the attribute to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class Misp__custom_api_call__Tool(BaseTool):
    name: str = "misp___custom_api_call__"
    connector_id: str = "nodes-base.misp"
    description: str = "Tool for misp __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Misp__custom_api_call__ToolInput
    credentials: Optional[MispCredentials] = None
