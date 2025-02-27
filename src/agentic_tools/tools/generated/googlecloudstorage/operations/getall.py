from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class GooglecloudstorageGetallToolInput(BaseModel):
    list_filters: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    max_results: Optional[float] = Field(None, description="Max number of results to return")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    prefix: Optional[str] = Field(None, description="Prefix")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    project_id: Optional[str] = Field(None, description="Project ID")


class GooglecloudstorageGetallTool(BaseTool):
    name: str = "googlecloudstorage_getall"
    connector_id: str = "nodes-base.googleCloudStorage"
    description: str = "Tool for googleCloudStorage getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GooglecloudstorageGetallToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
