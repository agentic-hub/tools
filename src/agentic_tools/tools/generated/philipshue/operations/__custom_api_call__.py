from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhilipshueCredentials

class Philipshue__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class Philipshue__custom_api_call__Tool(BaseTool):
    name: str = "philipshue___custom_api_call__"
    description: str = "Tool for philipsHue __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Philipshue__custom_api_call__ToolInput
    credentials: Optional[PhilipshueCredentials] = None
