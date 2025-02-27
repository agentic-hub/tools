from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StravaCredentials

class StravaGetkudosToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activity_id: Optional[str] = Field(None, description="ID or email of activity")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")


class StravaGetkudosTool(BaseTool):
    name: str = "strava_getkudos"
    connector_id: str = "nodes-base.strava"
    description: str = "Tool for strava getKudos operation - getKudos operation"
    args_schema: type[BaseModel] | None = StravaGetkudosToolInput
    credentials: Optional[StravaCredentials] = None
