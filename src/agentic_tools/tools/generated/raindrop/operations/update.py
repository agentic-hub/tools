from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RaindropCredentials

class RaindropUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bookmark_id: Optional[str] = Field(None, description="The ID of the bookmark to update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    collection_id: Optional[str] = Field(None, description="The ID of the collection to update")
    operation: Optional[str] = Field(None, description="Operation")


class RaindropUpdateTool(BaseTool):
    name: str = "raindrop_update"
    description: str = "Tool for raindrop update operation - update operation"
    args_schema: type[BaseModel] | None = RaindropUpdateToolInput
    credentials: Optional[RaindropCredentials] = None
