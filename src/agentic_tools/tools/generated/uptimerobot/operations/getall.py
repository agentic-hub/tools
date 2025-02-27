from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UptimerobotCredentials

class UptimerobotGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    type: Optional[str] = Field(None, description="The type of the monitor")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the monitor")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    friendly_name: Optional[str] = Field(None, description="The friendly name of the monitor")
    duration: Optional[float] = Field(None, description="The maintenance window activation period (minutes)")


class UptimerobotGetallTool(BaseTool):
    name: str = "uptimerobot_getall"
    description: str = "Tool for uptimeRobot getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = UptimerobotGetallToolInput
    credentials: Optional[UptimerobotCredentials] = None
