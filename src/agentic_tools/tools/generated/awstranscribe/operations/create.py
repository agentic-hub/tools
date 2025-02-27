from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstranscribeCredentials

class AwstranscribeCreateToolInput(BaseModel):
    language_code: Optional[str] = Field(None, description="Language used in the input media file")
    resource: Optional[str] = Field(None, description="Resource")
    media_file_uri: Optional[str] = Field(None, description="The S3 object location of the input media file")
    transcription_job_name: Optional[str] = Field(None, description="The name of the job")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    detect_language: Optional[bool] = Field(None, description="Whether to set this field to true to enable automatic language identification")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeCreateTool(BaseTool):
    name: str = "awstranscribe_create"
    description: str = "Tool for awsTranscribe create operation - create operation"
    args_schema: type[BaseModel] | None = AwstranscribeCreateToolInput
    credentials: Optional[AwstranscribeCredentials] = None
