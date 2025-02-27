from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class GooglecloudstorageGetToolInput(BaseModel):
    alt: Optional[str] = Field(None, description="Return Data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    get_filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    operation: Optional[str] = Field(None, description="Operation")
    encryption_headers: Optional[Dict[str, Any]] = Field(None, description="Encryption Headers")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    get_parameters: Optional[Dict[str, Any]] = Field(None, description="Additional Parameters")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")
    object_name: Optional[str] = Field(None, description="Object Name")


class GooglecloudstorageGetTool(BaseTool):
    name: str = "googlecloudstorage_get"
    description: str = "Tool for googleCloudStorage get operation - get operation"
    args_schema: type[BaseModel] | None = GooglecloudstorageGetToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
