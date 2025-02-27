from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscourseCredentials

class DiscourseGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post")
    post_id: Optional[str] = Field(None, description="ID of the post")
    flag: Optional[str] = Field(None, description="User flags to search for")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    operation: Optional[str] = Field(None, description="Choose an operation")
    name: Optional[str] = Field(None, description="Name of the category")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    username: Optional[str] = Field(None, description="The username of the user to create")
    group_id: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class DiscourseGetallTool(BaseTool):
    name: str = "discourse_getall"
    description: str = "Tool for discourse getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = DiscourseGetallToolInput
    credentials: Optional[DiscourseCredentials] = None
