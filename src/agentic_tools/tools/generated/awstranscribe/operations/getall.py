from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstranscribeCredentials

class AwstranscribeGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeGetallTool(BaseTool):
    name: str = "awstranscribe_getall"
    connector_id: str = "nodes-base.awsTranscribe"
    description: str = "Tool for awsTranscribe getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = AwstranscribeGetallToolInput
    credentials: Optional[AwstranscribeCredentials] = None
