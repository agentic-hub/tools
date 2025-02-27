from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FlowCredentials

class FlowGetToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    workspace_id: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowGetTool(BaseTool):
    name: str = "flow_get"
    description: str = "Tool for flow get operation - get operation"
    args_schema: type[BaseModel] | None = FlowGetToolInput
    credentials: Optional[FlowCredentials] = None
