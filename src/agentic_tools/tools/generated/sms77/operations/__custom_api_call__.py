from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Sms77Credentials

class Sms77__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class Sms77__custom_api_call__Tool(BaseTool):
    name: str = "sms77___custom_api_call__"
    connector_id: str = "nodes-base.sms77"
    description: str = "Tool for sms77 __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Sms77__custom_api_call__ToolInput
    credentials: Optional[Sms77Credentials] = None
