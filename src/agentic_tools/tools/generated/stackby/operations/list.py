from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StackbyCredentials

class StackbyListToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    table: Optional[str] = Field(None, description="Enter Table Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")
    stack_id: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyListTool(BaseTool):
    name: str = "stackby_list"
    description: str = "Tool for stackby list operation - list operation"
    args_schema: type[BaseModel] | None = StackbyListToolInput
    credentials: Optional[StackbyCredentials] = None
