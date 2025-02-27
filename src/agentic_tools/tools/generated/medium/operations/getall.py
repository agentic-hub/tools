from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MediumCredentials

class MediumGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class MediumGetallTool(BaseTool):
    name: str = "medium_getall"
    connector_id: str = "nodes-base.medium"
    description: str = "Tool for medium getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MediumGetallToolInput
    credentials: Optional[MediumCredentials] = None
