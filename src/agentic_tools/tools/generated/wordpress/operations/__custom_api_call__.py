from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import WordpressCredentials

class Wordpress__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    post_id: Optional[str] = Field(None, description="Unique identifier for the object")
    user_id: Optional[str] = Field(None, description="Unique identifier for the user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class Wordpress__custom_api_call__Tool(BaseTool):
    name: str = "wordpress___custom_api_call__"
    connector_id: str = "nodes-base.wordpress"
    description: str = "Tool for wordpress __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Wordpress__custom_api_call__ToolInput
    credentials: Optional[WordpressCredentials] = None
