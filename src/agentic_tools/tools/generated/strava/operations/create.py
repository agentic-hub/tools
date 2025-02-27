from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StravaCredentials

class StravaCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="The name of the activity")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activity_id: Optional[str] = Field(None, description="ID or email of activity")
    start_date: Optional[str] = Field(None, description="ISO 8601 formatted date time")
    elapsed_time: Optional[float] = Field(None, description="In seconds")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of activity. For example - Run, Ride etc.")


class StravaCreateTool(BaseTool):
    name: str = "strava_create"
    connector_id: str = "nodes-base.strava"
    description: str = "Tool for strava create operation - create operation"
    args_schema: type[BaseModel] | None = StravaCreateToolInput
    credentials: Optional[StravaCredentials] = None
