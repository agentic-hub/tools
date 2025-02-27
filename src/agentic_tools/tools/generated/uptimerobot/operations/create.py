from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UptimerobotCredentials

class UptimerobotCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    start_time: Optional[str] = Field(None, description="The maintenance window start datetime")
    type: Optional[str] = Field(None, description="The type of the monitor")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The correspondent value for the alert contact type")
    monitors: Optional[str] = Field(None, description="Monitor IDs to be displayed in status page (the values are separated with a dash (-) or 0 for all monitors)")
    id: Optional[str] = Field(None, description="The ID of the monitor")
    week_day: Optional[str] = Field(None, description="Week Day")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="The URL/IP of the monitor")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    friendly_name: Optional[str] = Field(None, description="The friendly name of the monitor")
    month_day: Optional[float] = Field(None, description="Month Day")
    duration: Optional[float] = Field(None, description="The maintenance window activation period (minutes)")


class UptimerobotCreateTool(BaseTool):
    name: str = "uptimerobot_create"
    connector_id: str = "nodes-base.uptimeRobot"
    description: str = "Tool for uptimeRobot create operation - create operation"
    args_schema: type[BaseModel] | None = UptimerobotCreateToolInput
    credentials: Optional[UptimerobotCredentials] = None
