from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PeekalinkCredentials

class PeekalinkPreviewToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")
    url: Optional[str] = Field(None, description="URL")


class PeekalinkPreviewTool(BaseTool):
    name: str = "peekalink_preview"
    description: str = "Tool for peekalink preview operation - preview operation"
    args_schema: type[BaseModel] | None = PeekalinkPreviewToolInput
    credentials: Optional[PeekalinkCredentials] = None
