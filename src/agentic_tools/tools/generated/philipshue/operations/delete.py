from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhilipshueCredentials

class PhilipshueDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueDeleteTool(BaseTool):
    name: str = "philipshue_delete"
    connector_id: str = "nodes-base.philipsHue"
    description: str = "Tool for philipsHue delete operation - delete operation"
    args_schema: type[BaseModel] | None = PhilipshueDeleteToolInput
    credentials: Optional[PhilipshueCredentials] = None
