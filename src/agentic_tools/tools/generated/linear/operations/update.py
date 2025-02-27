from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class LinearUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearUpdateTool(BaseTool):
    name: str = "linear_update"
    connector_id: str = "nodes-base.linear"
    description: str = "Tool for linear update operation - update operation"
    args_schema: type[BaseModel] | None = LinearUpdateToolInput
    credentials: Optional[LinearCredentials] = None
