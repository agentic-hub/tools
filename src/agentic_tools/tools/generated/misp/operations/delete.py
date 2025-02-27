from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MispCredentials

class MispDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    feed_id: Optional[str] = Field(None, description="UUID or numeric ID of the feed")
    user_id: Optional[str] = Field(None, description="Numeric ID of the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organisation_id: Optional[str] = Field(None, description="UUID or numeric ID of the organisation")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="Numeric ID of the attribute")
    attribute_id: Optional[str] = Field(None, description="UUID or numeric ID of the attribute")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID or numeric ID of the event")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MispDeleteTool(BaseTool):
    name: str = "misp_delete"
    connector_id: str = "nodes-base.misp"
    description: str = "Tool for misp delete operation - delete operation"
    args_schema: type[BaseModel] | None = MispDeleteToolInput
    credentials: Optional[MispCredentials] = None
