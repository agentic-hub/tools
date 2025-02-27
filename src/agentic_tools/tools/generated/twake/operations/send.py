from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwakeCredentials

class TwakeSendToolInput(BaseModel):
    content: Optional[str] = Field(None, description="Message content")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    channel_id: Optional[str] = Field(None, description="Channel's ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class TwakeSendTool(BaseTool):
    name: str = "twake_send"
    connector_id: str = "nodes-base.twake"
    description: str = "Tool for twake send operation - send operation"
    args_schema: type[BaseModel] | None = TwakeSendToolInput
    credentials: Optional[TwakeCredentials] = None
