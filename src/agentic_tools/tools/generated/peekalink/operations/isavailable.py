from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PeekalinkCredentials

class PeekalinkIsavailableToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")
    url: Optional[str] = Field(None, description="URL")


class PeekalinkIsavailableTool(BaseTool):
    name: str = "peekalink_isavailable"
    description: str = "Tool for peekalink isAvailable operation - isAvailable operation"
    args_schema: type[BaseModel] | None = PeekalinkIsavailableToolInput
    credentials: Optional[PeekalinkCredentials] = None
