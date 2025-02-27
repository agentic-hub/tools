from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class LinearDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearDeleteTool(BaseTool):
    name: str = "linear_delete"
    connector_id: str = "nodes-base.linear"
    description: str = "Tool for linear delete operation - delete operation"
    args_schema: type[BaseModel] | None = LinearDeleteToolInput
    credentials: Optional[LinearCredentials] = None
