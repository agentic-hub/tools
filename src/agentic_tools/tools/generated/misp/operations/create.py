from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MispCredentials

class MispCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    information: Optional[str] = Field(None, description="Information on the event - max 65535 characters")
    type: Optional[str] = Field(None, description="Type")
    org_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    feed_id: Optional[str] = Field(None, description="UUID or numeric ID of the feed")
    user_id: Optional[str] = Field(None, description="Numeric ID of the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    role_id: Optional[str] = Field(None, description="Role IDs are available in the MISP dashboard at /roles/index")
    value: Optional[str] = Field(None, description="Value")
    email: Optional[str] = Field(None, description="Email")
    organisation_id: Optional[str] = Field(None, description="UUID or numeric ID of the organisation")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attribute_id: Optional[str] = Field(None, description="UUID or numeric ID of the attribute")
    url: Optional[str] = Field(None, description="URL")
    galaxy_id: Optional[str] = Field(None, description="UUID or numeric ID of the galaxy")
    event_id: Optional[str] = Field(None, description="UUID of the event to attach the attribute to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    provider: Optional[str] = Field(None, description="Provider")


class MispCreateTool(BaseTool):
    name: str = "misp_create"
    description: str = "Tool for misp create operation - create operation"
    args_schema: type[BaseModel] | None = MispCreateToolInput
    credentials: Optional[MispCredentials] = None
