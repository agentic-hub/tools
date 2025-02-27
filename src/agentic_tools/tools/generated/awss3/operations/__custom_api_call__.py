from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Awss3Credentials

class Awss3__custom_api_call__ToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the bucket")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class Awss3__custom_api_call__Tool(BaseTool):
    name: str = "awss3___custom_api_call__"
    description: str = "Tool for awsS3 __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awss3__custom_api_call__ToolInput
    credentials: Optional[Awss3Credentials] = None
