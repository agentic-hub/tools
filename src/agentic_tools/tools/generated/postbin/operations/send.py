from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostbinSendToolInput(BaseModel):
    bin_id: Optional[str] = Field(None, description="Unique identifier for each bin")
    resource: Optional[str] = Field(None, description="Resource")
    bin_content: Optional[str] = Field(None, description="Bin Content")
    operation: Optional[str] = Field(None, description="Operation")


class PostbinSendTool(BaseTool):
    name: str = "postbin_send"
    description: str = "Tool for postBin send operation - send operation"
    args_schema: type[BaseModel] | None = PostbinSendToolInput
