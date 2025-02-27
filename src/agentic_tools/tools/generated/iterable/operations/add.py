from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import IterableCredentials

class IterableAddToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="Unique identifier for a particular user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="Value")
    by: Optional[str] = Field(None, description="Identifier to be used")
    list_id: Optional[str] = Field(None, description="Identifier to be used. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    identifier: Optional[str] = Field(None, description="Identifier to be used")
    email: Optional[str] = Field(None, description="Email for a particular user")
    operation: Optional[str] = Field(None, description="Operation")


class IterableAddTool(BaseTool):
    name: str = "iterable_add"
    description: str = "Tool for iterable add operation - add operation"
    args_schema: type[BaseModel] | None = IterableAddToolInput
    credentials: Optional[IterableCredentials] = None
