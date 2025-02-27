from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MessagebirdCredentials

class MessagebirdGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MessagebirdGetTool(BaseTool):
    name: str = "messagebird_get"
    connector_id: str = "nodes-base.messageBird"
    description: str = "Tool for messageBird get operation - get operation"
    args_schema: type[BaseModel] | None = MessagebirdGetToolInput
    credentials: Optional[MessagebirdCredentials] = None
