from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinDeleteToolInput(BaseModel):
    bin_id: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinDeleteTool(BaseTool):
    name: str = "postbin_delete"
    description: str = "Tool for postBin delete operation - delete operation"
    args_schema: type[BaseModel] | None = PostbinDeleteToolInput
