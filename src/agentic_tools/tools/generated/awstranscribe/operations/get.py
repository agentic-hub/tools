from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstranscribeCredentials

class AwstranscribeGetToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    transcription_job_name: Optional[str] = Field(None, description="The name of the job")
    return_transcript: Optional[bool] = Field(None, description="By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead.")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeGetTool(BaseTool):
    name: str = "awstranscribe_get"
    description: str = "Tool for awsTranscribe get operation - get operation"
    args_schema: type[BaseModel] | None = AwstranscribeGetToolInput
    credentials: Optional[AwstranscribeCredentials] = None
