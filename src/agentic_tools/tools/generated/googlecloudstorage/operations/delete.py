from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class GooglecloudstorageDeleteToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    get_filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    operation: Optional[str] = Field(None, description="Operation")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    get_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    object_name: Optional[str] = Field(None, description="Object Name")


class GooglecloudstorageDeleteTool(BaseTool):
    name: str = "googlecloudstorage_delete"
    connector_id: str = "nodes-base.googleCloudStorage"
    description: str = "Tool for googleCloudStorage delete operation - delete operation"
    args_schema: type[BaseModel] | None = GooglecloudstorageDeleteToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
