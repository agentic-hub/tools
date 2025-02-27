from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FlowCredentials

class FlowGetallToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    workspace_id: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowGetallTool(BaseTool):
    name: str = "flow_getall"
    connector_id: str = "nodes-base.flow"
    description: str = "Tool for flow getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = FlowGetallToolInput
    credentials: Optional[FlowCredentials] = None
