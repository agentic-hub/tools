from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RaindropCredentials

class RaindropCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    title: Optional[str] = Field(None, description="Title of the collection to create")
    collection_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link of the bookmark to be created")


class RaindropCreateTool(BaseTool):
    name: str = "raindrop_create"
    description: str = "Tool for raindrop create operation - create operation"
    args_schema: type[BaseModel] | None = RaindropCreateToolInput
    credentials: Optional[RaindropCredentials] = None
