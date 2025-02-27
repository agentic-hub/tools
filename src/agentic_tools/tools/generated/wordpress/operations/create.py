from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WordpressCredentials

class WordpressCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    post_id: Optional[str] = Field(None, description="Unique identifier for the object")
    user_id: Optional[str] = Field(None, description="Unique identifier for the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last name for the user")
    email: Optional[str] = Field(None, description="The email address for the user")
    password: Optional[str] = Field(None, description="Password for the user (never included)")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Display name for the user")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    username: Optional[str] = Field(None, description="Login name for the user")
    first_name: Optional[str] = Field(None, description="First name for the user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    title: Optional[str] = Field(None, description="The title for the post")


class WordpressCreateTool(BaseTool):
    name: str = "wordpress_create"
    connector_id: str = "nodes-base.wordpress"
    description: str = "Tool for wordpress create operation - create operation"
    args_schema: type[BaseModel] | None = WordpressCreateToolInput
    credentials: Optional[WordpressCredentials] = None
