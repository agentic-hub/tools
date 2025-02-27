from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudstorageCredentials

class Googlecloudstorage__custom_api_call__ToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    projection: Optional[str] = Field(None, description="Projection")
    resource: Optional[str] = Field(None, description="Resource")


class Googlecloudstorage__custom_api_call__Tool(BaseTool):
    name: str = "googlecloudstorage___custom_api_call__"
    connector_id: str = "nodes-base.googleCloudStorage"
    description: str = "Tool for googleCloudStorage __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlecloudstorage__custom_api_call__ToolInput
    credentials: Optional[GooglecloudstorageCredentials] = None
