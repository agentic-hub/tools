from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpontitCredentials

class SpontitCreateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="To provide text in a push, supply one of either \"content\" or \"pushContent\" (or both). Limited to 2500 characters. (Required if a value for \"pushContent\" is not provided).")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class SpontitCreateTool(BaseTool):
    name: str = "spontit_create"
    description: str = "Tool for spontit create operation - create operation"
    args_schema: type[BaseModel] | None = SpontitCreateToolInput
    credentials: Optional[SpontitCredentials] = None
