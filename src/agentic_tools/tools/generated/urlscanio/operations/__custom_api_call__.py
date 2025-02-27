from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UrlscanioCredentials

class Urlscanio__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Urlscanio__custom_api_call__Tool(BaseTool):
    name: str = "urlscanio___custom_api_call__"
    description: str = "Tool for urlScanIo __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Urlscanio__custom_api_call__ToolInput
    credentials: Optional[UrlscanioCredentials] = None
