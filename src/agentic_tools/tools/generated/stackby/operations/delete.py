from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StackbyCredentials

class StackbyDeleteToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Enter Table Name")
    id: Optional[str] = Field(None, description="ID of the record to return")
    operation: Optional[str] = Field(None, description="Operation")
    stack_id: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyDeleteTool(BaseTool):
    name: str = "stackby_delete"
    connector_id: str = "nodes-base.stackby"
    description: str = "Tool for stackby delete operation - delete operation"
    args_schema: type[BaseModel] | None = StackbyDeleteToolInput
    credentials: Optional[StackbyCredentials] = None
