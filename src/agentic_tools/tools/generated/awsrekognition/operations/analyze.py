from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwsrekognitionCredentials

class AwsrekognitionAnalyzeToolInput(BaseModel):
    name: Optional[str] = Field(None, description="S3 object key name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    bucket: Optional[str] = Field(None, description="Name of the S3 bucket")
    binary_data: Optional[bool] = Field(None, description="Whether the image to analyze should be taken from binary field")
    type: Optional[str] = Field(None, description="Type")


class AwsrekognitionAnalyzeTool(BaseTool):
    name: str = "awsrekognition_analyze"
    description: str = "Tool for awsRekognition analyze operation - analyze operation"
    args_schema: type[BaseModel] | None = AwsrekognitionAnalyzeToolInput
    credentials: Optional[AwsrekognitionCredentials] = None
