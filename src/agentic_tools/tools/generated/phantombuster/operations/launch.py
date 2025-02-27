from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhantombusterCredentials

class PhantombusterLaunchToolInput(BaseModel):
    resolve_data: Optional[bool] = Field(None, description="By default the launch just include the container ID. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterLaunchTool(BaseTool):
    name: str = "phantombuster_launch"
    connector_id: str = "nodes-base.phantombuster"
    description: str = "Tool for phantombuster launch operation - launch operation"
    args_schema: type[BaseModel] | None = PhantombusterLaunchToolInput
    credentials: Optional[PhantombusterCredentials] = None
