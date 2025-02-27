from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstranscribeCredentials

class AwstranscribeDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    transcription_job_name: Optional[str] = Field(None, description="The name of the job")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeDeleteTool(BaseTool):
    name: str = "awstranscribe_delete"
    connector_id: str = "nodes-base.awsTranscribe"
    description: str = "Tool for awsTranscribe delete operation - delete operation"
    args_schema: type[BaseModel] | None = AwstranscribeDeleteToolInput
    credentials: Optional[AwstranscribeCredentials] = None
