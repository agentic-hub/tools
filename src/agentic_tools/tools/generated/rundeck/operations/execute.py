from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RundeckCredentials

class RundeckExecuteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    filter: Optional[str] = Field(None, description="Filter Rundeck nodes by name")
    jobid: Optional[str] = Field(None, description="The job ID to execute")
    arguments: Optional[Dict[str, Any]] = Field(None, description="Arguments")
    operation: Optional[str] = Field(None, description="Operation")


class RundeckExecuteTool(BaseTool):
    name: str = "rundeck_execute"
    description: str = "Tool for rundeck execute operation - execute operation"
    args_schema: type[BaseModel] | None = RundeckExecuteToolInput
    credentials: Optional[RundeckCredentials] = None
