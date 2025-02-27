from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OuraCredentials

class OuraGetactivityToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class OuraGetactivityTool(BaseTool):
    name: str = "oura_getactivity"
    description: str = "Tool for oura getActivity operation - getActivity operation"
    args_schema: type[BaseModel] | None = OuraGetactivityToolInput
    credentials: Optional[OuraCredentials] = None
