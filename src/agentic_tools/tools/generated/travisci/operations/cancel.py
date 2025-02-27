from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TravisciCredentials

class TravisciCancelToolInput(BaseModel):
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciCancelTool(BaseTool):
    name: str = "travisci_cancel"
    connector_id: str = "nodes-base.travisCi"
    description: str = "Tool for travisCi cancel operation - cancel operation"
    args_schema: type[BaseModel] | None = TravisciCancelToolInput
    credentials: Optional[TravisciCredentials] = None
