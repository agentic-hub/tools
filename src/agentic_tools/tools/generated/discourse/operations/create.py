from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscourseCredentials

class DiscourseCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post")
    post_id: Optional[str] = Field(None, description="ID of the post")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    text_color: Optional[str] = Field(None, description="Text color of the category")
    email: Optional[str] = Field(None, description="Email of the user to create")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    password: Optional[str] = Field(None, description="The password of the user to create")
    operation: Optional[str] = Field(None, description="Choose an operation")
    color: Optional[str] = Field(None, description="Color of the category")
    name: Optional[str] = Field(None, description="Name of the category")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    username: Optional[str] = Field(None, description="The username of the user to create")
    group_id: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title of the post")


class DiscourseCreateTool(BaseTool):
    name: str = "discourse_create"
    description: str = "Tool for discourse create operation - create operation"
    args_schema: type[BaseModel] | None = DiscourseCreateToolInput
    credentials: Optional[DiscourseCredentials] = None
