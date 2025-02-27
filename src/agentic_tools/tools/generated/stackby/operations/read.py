from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StackbyCredentials

class StackbyReadToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Enter Table Name")
    id: Optional[str] = Field(None, description="ID of the record to return")
    operation: Optional[str] = Field(None, description="Operation")
    stack_id: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyReadTool(BaseTool):
    name: str = "stackby_read"
    connector_id: str = "nodes-base.stackby"
    description: str = "Tool for stackby read operation - read operation"
    args_schema: type[BaseModel] | None = StackbyReadToolInput
    credentials: Optional[StackbyCredentials] = None
