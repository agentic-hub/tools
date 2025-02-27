from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Signl4Credentials

class Signl4SendToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="A more detailed description for the alert")
    operation: Optional[str] = Field(None, description="Operation")


class Signl4SendTool(BaseTool):
    name: str = "signl4_send"
    connector_id: str = "nodes-base.signl4"
    description: str = "Tool for signl4 send operation - send operation"
    args_schema: type[BaseModel] | None = Signl4SendToolInput
    credentials: Optional[Signl4Credentials] = None
