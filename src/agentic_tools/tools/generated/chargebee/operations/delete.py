from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ChargebeeCredentials

class ChargebeeDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to delete")


class ChargebeeDeleteTool(BaseTool):
    name: str = "chargebee_delete"
    description: str = "Tool for chargebee delete operation - delete operation"
    args_schema: type[BaseModel] | None = ChargebeeDeleteToolInput
    credentials: Optional[ChargebeeCredentials] = None
