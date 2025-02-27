from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MispCredentials

class MispUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    feed_id: Optional[str] = Field(None, description="ID of the feed to update")
    user_id: Optional[str] = Field(None, description="ID of the user to update")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organisation_id: Optional[str] = Field(None, description="ID of the organisation to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="ID of the tag to update")
    attribute_id: Optional[str] = Field(None, description="ID of the attribute to update")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID or numeric ID of the event")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MispUpdateTool(BaseTool):
    name: str = "misp_update"
    description: str = "Tool for misp update operation - update operation"
    args_schema: type[BaseModel] | None = MispUpdateToolInput
    credentials: Optional[MispCredentials] = None
