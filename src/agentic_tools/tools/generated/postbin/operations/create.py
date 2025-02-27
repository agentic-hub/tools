from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinCreateToolInput(BaseModel):
    bin_id: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinCreateTool(BaseTool):
    name: str = "postbin_create"
    connector_id: str = "nodes-base.postBin"
    description: str = "Tool for postBin create operation - create operation"
    args_schema: type[BaseModel] | None = PostbinCreateToolInput
