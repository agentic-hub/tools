from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssnsCredentials

class AwssnsCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class AwssnsCreateTool(BaseTool):
    name: str = "awssns_create"
    description: str = "Tool for awsSns create operation - create operation"
    args_schema: type[BaseModel] | None = AwssnsCreateToolInput
    credentials: Optional[AwssnsCredentials] = None
