from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class GooglecloudstorageCreateToolInput(BaseModel):
    create_data: Optional[Dict[str, Any]] = Field(None, description="Create Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    create_content: Optional[str] = Field(None, description="Content of the file to be uploaded")
    create_acl: Optional[Dict[str, Any]] = Field(None, description="Predefined Access Control")
    create_body: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    operation: Optional[str] = Field(None, description="Operation")
    encryption_headers: Optional[Dict[str, Any]] = Field(None, description="Encryption Headers")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    create_query: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    update_projection: Optional[str] = Field(None, description="Projection")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    project_id: Optional[str] = Field(None, description="Project ID")
    object_name: Optional[str] = Field(None, description="Object Name")
    create_from_binary: Optional[bool] = Field(None, description="Whether the data for creating a file should come from a binary field")
    create_binary_property_name: Optional[str] = Field(None, description="Input Binary Field")


class GooglecloudstorageCreateTool(BaseTool):
    name: str = "googlecloudstorage_create"
    description: str = "Tool for googleCloudStorage create operation - create operation"
    args_schema: type[BaseModel] | None = GooglecloudstorageCreateToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
