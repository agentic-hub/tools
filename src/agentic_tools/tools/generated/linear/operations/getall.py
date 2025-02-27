from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class LinearGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearGetallTool(BaseTool):
    name: str = "linear_getall"
    description: str = "Tool for linear getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = LinearGetallToolInput
    credentials: Optional[LinearCredentials] = None
