from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Awss3Credentials

class Awss3CopyToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the bucket")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    destination_path: Optional[str] = Field(None, description="The name of the destination bucket and key name of the destination object, separated by a slash (/)")
    source_path: Optional[str] = Field(None, description="The name of the source bucket and key name of the source object, separated by a slash (/)")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class Awss3CopyTool(BaseTool):
    name: str = "awss3_copy"
    connector_id: str = "nodes-base.awsS3"
    description: str = "Tool for awsS3 copy operation - copy operation"
    args_schema: type[BaseModel] | None = Awss3CopyToolInput
    credentials: Optional[Awss3Credentials] = None
