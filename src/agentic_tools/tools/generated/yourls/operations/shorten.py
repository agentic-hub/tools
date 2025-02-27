from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import YourlsCredentials

class YourlsShortenToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    url: Optional[str] = Field(None, description="The URL to shorten")
    short_url: Optional[str] = Field(None, description="The short URL to expand")
    operation: Optional[str] = Field(None, description="Operation")


class YourlsShortenTool(BaseTool):
    name: str = "yourls_shorten"
    connector_id: str = "nodes-base.yourls"
    description: str = "Tool for yourls shorten operation - shorten operation"
    args_schema: type[BaseModel] | None = YourlsShortenToolInput
    credentials: Optional[YourlsCredentials] = None
