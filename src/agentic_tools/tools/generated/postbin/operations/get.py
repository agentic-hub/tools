from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinGetToolInput(BaseModel):
    bin_id: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    request_id: Optional[str] = Field(None, description="Unique identifier for each request")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinGetTool(BaseTool):
    name: str = "postbin_get"
    connector_id: str = "nodes-base.postBin"
    description: str = "Tool for postBin get operation - get operation"
    args_schema: type[BaseModel] | None = PostbinGetToolInput
