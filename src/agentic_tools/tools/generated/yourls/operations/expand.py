from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import YourlsCredentials

class YourlsExpandToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    short_url: Optional[str] = Field(None, description="The short URL to expand")
    operation: Optional[str] = Field(None, description="Operation")


class YourlsExpandTool(BaseTool):
    name: str = "yourls_expand"
    connector_id: str = "nodes-base.yourls"
    description: str = "Tool for yourls expand operation - expand operation"
    args_schema: type[BaseModel] | None = YourlsExpandToolInput
    credentials: Optional[YourlsCredentials] = None
