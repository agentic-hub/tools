from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhilipshueCredentials

class PhilipshueGetallToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    light_id: Optional[str] = Field(None, description="Light ID")
    operation: Optional[str] = Field(None, description="Operation")


class PhilipshueGetallTool(BaseTool):
    name: str = "philipshue_getall"
    connector_id: str = "nodes-base.philipsHue"
    description: str = "Tool for philipsHue getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = PhilipshueGetallToolInput
    credentials: Optional[PhilipshueCredentials] = None
