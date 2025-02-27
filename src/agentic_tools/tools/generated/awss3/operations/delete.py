from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Awss3Credentials

class Awss3DeleteToolInput(BaseModel):
    folder_key: Optional[str] = Field(None, description="Folder Key")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the AWS S3 bucket to delete")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class Awss3DeleteTool(BaseTool):
    name: str = "awss3_delete"
    connector_id: str = "nodes-base.awsS3"
    description: str = "Tool for awsS3 delete operation - delete operation"
    args_schema: type[BaseModel] | None = Awss3DeleteToolInput
    credentials: Optional[Awss3Credentials] = None
