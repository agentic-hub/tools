from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VonageCredentials

class VonageSendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number that the message should be sent to. Numbers are specified in E.164 format.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    message: Optional[str] = Field(None, description="The body of the message being sent")
    from: Optional[str] = Field(None, description="The name or number the message should be sent from")
    operation: Optional[str] = Field(None, description="Operation")


class VonageSendTool(BaseTool):
    name: str = "vonage_send"
    connector_id: str = "nodes-base.vonage"
    description: str = "Tool for vonage send operation - send operation"
    args_schema: type[BaseModel] | None = VonageSendToolInput
    credentials: Optional[VonageCredentials] = None
