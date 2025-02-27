from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Sms77Credentials

class Sms77SendToolInput(BaseModel):
    to: Optional[str] = Field(None, description="The number of your recipient(s) separated by comma. Can be regular numbers or contact/groups from seven.")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send. Max. 1520 characters")
    from: Optional[str] = Field(None, description="The caller ID displayed in the receivers display. Max 16 numeric or 11 alphanumeric characters.")
    operation: Optional[str] = Field(None, description="Operation")


class Sms77SendTool(BaseTool):
    name: str = "sms77_send"
    connector_id: str = "nodes-base.sms77"
    description: str = "Tool for sms77 send operation - send operation"
    args_schema: type[BaseModel] | None = Sms77SendToolInput
    credentials: Optional[Sms77Credentials] = None
