from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CloudflareCredentials

class Cloudflare__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Cloudflare__custom_api_call__Tool(BaseTool):
    name: str = "cloudflare___custom_api_call__"
    description: str = "Tool for cloudflare __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Cloudflare__custom_api_call__ToolInput
    credentials: Optional[CloudflareCredentials] = None
