from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinRemovefirstToolInput(BaseModel):
    bin_id: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinRemovefirstTool(BaseTool):
    name: str = "postbin_removefirst"
    connector_id: str = "nodes-base.postBin"
    description: str = "Tool for postBin removeFirst operation - removeFirst operation"
    args_schema: type[BaseModel] | None = PostbinRemovefirstToolInput
