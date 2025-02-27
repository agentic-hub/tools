from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhantombusterCredentials

class PhantombusterGetToolInput(BaseModel):
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Agent ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetTool(BaseTool):
    name: str = "phantombuster_get"
    connector_id: str = "nodes-base.phantombuster"
    description: str = "Tool for phantombuster get operation - get operation"
    args_schema: type[BaseModel] | None = PhantombusterGetToolInput
    credentials: Optional[PhantombusterCredentials] = None
