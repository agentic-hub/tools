from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StackbyCredentials

class StackbyAppendToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Enter Table Name")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")
    stack_id: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyAppendTool(BaseTool):
    name: str = "stackby_append"
    connector_id: str = "nodes-base.stackby"
    description: str = "Tool for stackby append operation - append operation"
    args_schema: type[BaseModel] | None = StackbyAppendToolInput
    credentials: Optional[StackbyCredentials] = None
