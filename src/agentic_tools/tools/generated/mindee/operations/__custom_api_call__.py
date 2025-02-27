from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MindeeCredentials

class Mindee__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    api_version: Optional[str] = Field(None, description="Which Mindee API Version to use")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    operation: Optional[str] = Field(None, description="Operation")


class Mindee__custom_api_call__Tool(BaseTool):
    name: str = "mindee___custom_api_call__"
    description: str = "Tool for mindee __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Mindee__custom_api_call__ToolInput
    credentials: Optional[MindeeCredentials] = None
