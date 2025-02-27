from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushcutCredentials

class PushcutSendToolInput(BaseModel):
    notification_name: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class PushcutSendTool(BaseTool):
    name: str = "pushcut_send"
    connector_id: str = "nodes-base.pushcut"
    description: str = "Tool for pushcut send operation - send operation"
    args_schema: type[BaseModel] | None = PushcutSendToolInput
    credentials: Optional[PushcutCredentials] = None
