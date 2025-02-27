from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhilipshueCredentials

class PhilipshueGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueGetTool(BaseTool):
    name: str = "philipshue_get"
    connector_id: str = "nodes-base.philipsHue"
    description: str = "Tool for philipsHue get operation - get operation"
    args_schema: type[BaseModel] | None = PhilipshueGetToolInput
    credentials: Optional[PhilipshueCredentials] = None
