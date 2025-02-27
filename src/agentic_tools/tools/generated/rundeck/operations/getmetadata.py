from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RundeckCredentials

class RundeckGetmetadataToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    jobid: Optional[str] = Field(None, description="The job ID to get metadata off")
    operation: Optional[str] = Field(None, description="Operation")


class RundeckGetmetadataTool(BaseTool):
    name: str = "rundeck_getmetadata"
    description: str = "Tool for rundeck getMetadata operation - getMetadata operation"
    args_schema: type[BaseModel] | None = RundeckGetmetadataToolInput
    credentials: Optional[RundeckCredentials] = None
