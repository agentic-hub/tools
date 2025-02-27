from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TravisciCredentials

class TravisciGetToolInput(BaseModel):
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciGetTool(BaseTool):
    name: str = "travisci_get"
    connector_id: str = "nodes-base.travisCi"
    description: str = "Tool for travisCi get operation - get operation"
    args_schema: type[BaseModel] | None = TravisciGetToolInput
    credentials: Optional[TravisciCredentials] = None
