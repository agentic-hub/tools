from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RundeckCredentials

class Rundeck__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    jobid: Optional[str] = Field(None, description="The job ID to execute")
    operation: Optional[str] = Field(None, description="Operation")


class Rundeck__custom_api_call__Tool(BaseTool):
    name: str = "rundeck___custom_api_call__"
    description: str = "Tool for rundeck __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Rundeck__custom_api_call__ToolInput
    credentials: Optional[RundeckCredentials] = None
