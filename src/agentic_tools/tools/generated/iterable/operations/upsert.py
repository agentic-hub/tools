from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import IterableCredentials

class IterableUpsertToolInput(BaseModel):
    prefer_user_id: Optional[bool] = Field(None, description="Whether to create a new user if the idetifier does not exist")
    user_id: Optional[str] = Field(None, description="Unique identifier for a particular user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="Value")
    by: Optional[str] = Field(None, description="Identifier to be used")
    list_id: Optional[str] = Field(None, description="Identifier to be used. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    identifier: Optional[str] = Field(None, description="Identifier to be used")
    email: Optional[str] = Field(None, description="Email for a particular user")
    operation: Optional[str] = Field(None, description="Operation")


class IterableUpsertTool(BaseTool):
    name: str = "iterable_upsert"
    description: str = "Tool for iterable upsert operation - upsert operation"
    args_schema: type[BaseModel] | None = IterableUpsertToolInput
    credentials: Optional[IterableCredentials] = None
