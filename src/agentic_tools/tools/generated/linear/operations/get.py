from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class LinearGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearGetTool(BaseTool):
    name: str = "linear_get"
    connector_id: str = "nodes-base.linear"
    description: str = "Tool for linear get operation - get operation"
    args_schema: type[BaseModel] | None = LinearGetToolInput
    credentials: Optional[LinearCredentials] = None
