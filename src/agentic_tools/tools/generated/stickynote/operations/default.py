from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StickynoteDefaultToolInput(BaseModel):
    content: Optional[str] = Field(None, description="Content")
    width: Optional[float] = Field(None, description="Width")
    height: Optional[float] = Field(None, description="Height")
    color: Optional[float] = Field(None, description="Color")


class StickynoteDefaultTool(BaseTool):
    name: str = "stickynote_default"
    description: str = "Tool for stickyNote default operation - default operation"
    args_schema: type[BaseModel] | None = StickynoteDefaultToolInput
