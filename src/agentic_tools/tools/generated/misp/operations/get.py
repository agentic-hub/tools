from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MispCredentials

class MispGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    feed_id: Optional[str] = Field(None, description="UUID or numeric ID of the feed")
    user_id: Optional[str] = Field(None, description="Numeric ID of the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    organisation_id: Optional[str] = Field(None, description="UUID or numeric ID of the organisation")
    warninglist_id: Optional[str] = Field(None, description="Numeric ID of the warninglist")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attribute_id: Optional[str] = Field(None, description="UUID or numeric ID of the attribute")
    noticelist_id: Optional[str] = Field(None, description="Numeric ID of the noticelist")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID or numeric ID of the event")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MispGetTool(BaseTool):
    name: str = "misp_get"
    description: str = "Tool for misp get operation - get operation"
    args_schema: type[BaseModel] | None = MispGetToolInput
    credentials: Optional[MispCredentials] = None
