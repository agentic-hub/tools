from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RaindropCredentials

class RaindropGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to retrieve")
    user_id: Optional[str] = Field(None, description="The ID of the user to retrieve")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    self: Optional[bool] = Field(None, description="Whether to return details on the logged-in user")
    collection_id: Optional[str] = Field(None, description="The ID of the collection to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class RaindropGetTool(BaseTool):
    name: str = "raindrop_get"
    connector_id: str = "nodes-base.raindrop"
    description: str = "Tool for raindrop get operation - get operation"
    args_schema: type[BaseModel] | None = RaindropGetToolInput
    credentials: Optional[RaindropCredentials] = None
