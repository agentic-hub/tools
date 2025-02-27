from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CloudflareCredentials

class CloudflareGetmanyToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    zone_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class CloudflareGetmanyTool(BaseTool):
    name: str = "cloudflare_getmany"
    description: str = "Tool for cloudflare getMany operation - getMany operation"
    args_schema: type[BaseModel] | None = CloudflareGetmanyToolInput
    credentials: Optional[CloudflareCredentials] = None
