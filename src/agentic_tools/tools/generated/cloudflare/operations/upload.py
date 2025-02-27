from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CloudflareCredentials

class CloudflareUploadToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    private_key: Optional[str] = Field(None, description="Private Key")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    certificate: Optional[str] = Field(None, description="The zone's leaf certificate")
    operation: Optional[str] = Field(None, description="Operation")


class CloudflareUploadTool(BaseTool):
    name: str = "cloudflare_upload"
    connector_id: str = "nodes-base.cloudflare"
    description: str = "Tool for cloudflare upload operation - upload operation"
    args_schema: type[BaseModel] | None = CloudflareUploadToolInput
    credentials: Optional[CloudflareCredentials] = None
