from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscourseCredentials

class DiscourseGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post")
    external_id: Optional[str] = Field(None, description="Discourse SSO external ID")
    post_id: Optional[str] = Field(None, description="ID of the post")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    operation: Optional[str] = Field(None, description="Choose an operation")
    name: Optional[str] = Field(None, description="Name of the group")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    by: Optional[str] = Field(None, description="What to search by")
    username: Optional[str] = Field(None, description="The username of the user to return")
    group_id: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class DiscourseGetTool(BaseTool):
    name: str = "discourse_get"
    description: str = "Tool for discourse get operation - get operation"
    args_schema: type[BaseModel] | None = DiscourseGetToolInput
    credentials: Optional[DiscourseCredentials] = None
