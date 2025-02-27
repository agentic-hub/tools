from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TravisciCredentials

class TravisciRestartToolInput(BaseModel):
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciRestartTool(BaseTool):
    name: str = "travisci_restart"
    connector_id: str = "nodes-base.travisCi"
    description: str = "Tool for travisCi restart operation - restart operation"
    args_schema: type[BaseModel] | None = TravisciRestartToolInput
    credentials: Optional[TravisciCredentials] = None
