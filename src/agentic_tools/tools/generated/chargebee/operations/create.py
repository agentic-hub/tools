from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ChargebeeCredentials

class ChargebeeCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties to set on the new user")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeCreateTool(BaseTool):
    name: str = "chargebee_create"
    description: str = "Tool for chargebee create operation - create operation"
    args_schema: type[BaseModel] | None = ChargebeeCreateToolInput
    credentials: Optional[ChargebeeCredentials] = None
