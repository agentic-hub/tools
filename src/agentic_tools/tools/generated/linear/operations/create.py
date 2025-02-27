from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class LinearCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    team_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class LinearCreateTool(BaseTool):
    name: str = "linear_create"
    description: str = "Tool for linear create operation - create operation"
    args_schema: type[BaseModel] | None = LinearCreateToolInput
    credentials: Optional[LinearCredentials] = None
