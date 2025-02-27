from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RaindropCredentials

class RaindropGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    collection_id: Optional[str] = Field(None, description="The ID of the collection from which to retrieve all bookmarks. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class RaindropGetallTool(BaseTool):
    name: str = "raindrop_getall"
    connector_id: str = "nodes-base.raindrop"
    description: str = "Tool for raindrop getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = RaindropGetallToolInput
    credentials: Optional[RaindropCredentials] = None
