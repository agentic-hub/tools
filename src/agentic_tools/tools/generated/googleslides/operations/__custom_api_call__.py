from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleslidesCredentials

class Googleslides__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class Googleslides__custom_api_call__Tool(BaseTool):
    name: str = "googleslides___custom_api_call__"
    connector_id: str = "nodes-base.googleSlides"
    description: str = "Tool for googleSlides __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googleslides__custom_api_call__ToolInput
    credentials: Optional[GoogleslidesCredentials] = None
