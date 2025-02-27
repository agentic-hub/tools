from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TravisciCredentials

class TravisciGetallToolInput(BaseModel):
    build_id: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciGetallTool(BaseTool):
    name: str = "travisci_getall"
    connector_id: str = "nodes-base.travisCi"
    description: str = "Tool for travisCi getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = TravisciGetallToolInput
    credentials: Optional[TravisciCredentials] = None
