from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DiscourseCredentials

class DiscourseUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="Content of the post. HTML is supported.")
    post_id: Optional[str] = Field(None, description="ID of the post")
    category_id: Optional[str] = Field(None, description="ID of the category")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    usernames: Optional[str] = Field(None, description="Usernames to add to group. Multiples can be defined separated by comma.")
    operation: Optional[str] = Field(None, description="Choose an operation")
    name: Optional[str] = Field(None, description="New name of the category")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    username: Optional[str] = Field(None, description="The username of the user to create")
    group_id: Optional[str] = Field(None, description="ID of the group to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class DiscourseUpdateTool(BaseTool):
    name: str = "discourse_update"
    connector_id: str = "nodes-base.discourse"
    description: str = "Tool for discourse update operation - update operation"
    args_schema: type[BaseModel] | None = DiscourseUpdateToolInput
    credentials: Optional[DiscourseCredentials] = None
