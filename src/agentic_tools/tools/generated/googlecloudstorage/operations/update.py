from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class GooglecloudstorageUpdateToolInput(BaseModel):
    metagen_and_acl_query: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    create_acl: Optional[Dict[str, Any]] = Field(None, description="Predefined Access Control")
    create_body: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    get_filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    operation: Optional[str] = Field(None, description="Operation")
    encryption_headers: Optional[Dict[str, Any]] = Field(None, description="Encryption Headers")
    update_data: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    update_projection: Optional[str] = Field(None, description="Projection")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    object_name: Optional[str] = Field(None, description="Object Name")


class GooglecloudstorageUpdateTool(BaseTool):
    name: str = "googlecloudstorage_update"
    description: str = "Tool for googleCloudStorage update operation - update operation"
    args_schema: type[BaseModel] | None = GooglecloudstorageUpdateToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
