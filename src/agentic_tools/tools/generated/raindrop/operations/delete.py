from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RaindropCredentials

class RaindropDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tags: Optional[str] = Field(None, description="One or more tags to delete. Enter comma-separated values to delete multiple tags.")
    collection_id: Optional[str] = Field(None, description="The ID of the collection to delete")
    operation: Optional[str] = Field(None, description="Operation")


class RaindropDeleteTool(BaseTool):
    name: str = "raindrop_delete"
    connector_id: str = "nodes-base.raindrop"
    description: str = "Tool for raindrop delete operation - delete operation"
    args_schema: type[BaseModel] | None = RaindropDeleteToolInput
    credentials: Optional[RaindropCredentials] = None
