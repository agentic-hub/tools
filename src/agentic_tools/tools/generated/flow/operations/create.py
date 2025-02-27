from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FlowCredentials

class FlowCreateToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    name: Optional[str] = Field(None, description="The title of the task")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    workspace_id: Optional[str] = Field(None, description="Create resources under the given workspace")
    operation: Optional[str] = Field(None, description="Operation")


class FlowCreateTool(BaseTool):
    name: str = "flow_create"
    connector_id: str = "nodes-base.flow"
    description: str = "Tool for flow create operation - create operation"
    args_schema: type[BaseModel] | None = FlowCreateToolInput
    credentials: Optional[FlowCredentials] = None
