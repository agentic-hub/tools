from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IfDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    conditions: Optional[str] = Field(None, description="conditions")


class IfDefaultTool(BaseTool):
    name: str = "if_default"
    description: str = "Tool for if default operation - default operation"
    args_schema: type[BaseModel] | None = IfDefaultToolInput
