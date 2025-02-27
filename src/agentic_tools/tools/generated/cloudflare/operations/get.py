from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CloudflareCredentials

class CloudflareGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    certificate_id: Optional[str] = Field(None, description="Certificate ID")


class CloudflareGetTool(BaseTool):
    name: str = "cloudflare_get"
    connector_id: str = "nodes-base.cloudflare"
    description: str = "Tool for cloudflare get operation - get operation"
    args_schema: type[BaseModel] | None = CloudflareGetToolInput
    credentials: Optional[CloudflareCredentials] = None
