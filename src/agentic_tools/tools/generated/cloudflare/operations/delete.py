from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CloudflareCredentials

class CloudflareDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    certificate_id: Optional[str] = Field(None, description="Certificate ID")


class CloudflareDeleteTool(BaseTool):
    name: str = "cloudflare_delete"
    description: str = "Tool for cloudflare delete operation - delete operation"
    args_schema: type[BaseModel] | None = CloudflareDeleteToolInput
    credentials: Optional[CloudflareCredentials] = None
