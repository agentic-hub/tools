from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ProfitwellCredentials

class ProfitwellGetsettingToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class ProfitwellGetsettingTool(BaseTool):
    name: str = "profitwell_getsetting"
    description: str = "Tool for profitWell getSetting operation - getSetting operation"
    args_schema: type[BaseModel] | None = ProfitwellGetsettingToolInput
    credentials: Optional[ProfitwellCredentials] = None
