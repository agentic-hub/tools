from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssnsCredentials

class AwssnsDeleteToolInput(BaseModel):
    topic: Optional[str] = Field(None, description="By URL")
    operation: Optional[str] = Field(None, description="Operation")


class AwssnsDeleteTool(BaseTool):
    name: str = "awssns_delete"
    description: str = "Tool for awsSns delete operation - delete operation"
    args_schema: type[BaseModel] | None = AwssnsDeleteToolInput
    credentials: Optional[AwssnsCredentials] = None
