from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Awss3Credentials

class Awss3UploadToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    file_content: Optional[str] = Field(None, description="The text content of the file to upload")
    tags_ui: Optional[Dict[str, Any]] = Field(None, description="Optional extra headers to add to the message (most headers are allowed)")
    operation: Optional[str] = Field(None, description="Operation")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    name: Optional[str] = Field(None, description="A succinct description of the nature, symptoms, cause, or effect of the bucket")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="File Name")
    file_key: Optional[str] = Field(None, description="File Key")


class Awss3UploadTool(BaseTool):
    name: str = "awss3_upload"
    connector_id: str = "nodes-base.awsS3"
    description: str = "Tool for awsS3 upload operation - upload operation"
    args_schema: type[BaseModel] | None = Awss3UploadToolInput
    credentials: Optional[Awss3Credentials] = None
