from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleperspectiveCredentials

class Googleperspective__custom_api_call__ToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")


class Googleperspective__custom_api_call__Tool(BaseTool):
    name: str = "googleperspective___custom_api_call__"
    description: str = "Tool for googlePerspective __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googleperspective__custom_api_call__ToolInput
    credentials: Optional[GoogleperspectiveCredentials] = None
