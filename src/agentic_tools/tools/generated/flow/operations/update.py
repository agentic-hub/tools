from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FlowCredentials

class FlowUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    workspace_id: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowUpdateTool(BaseTool):
    name: str = "flow_update"
    connector_id: str = "nodes-base.flow"
    description: str = "Tool for flow update operation - update operation"
    args_schema: type[BaseModel] | None = FlowUpdateToolInput
    credentials: Optional[FlowCredentials] = None
