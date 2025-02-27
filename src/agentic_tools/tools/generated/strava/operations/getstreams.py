from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StravaCredentials

class StravaGetstreamsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    activity_id: Optional[str] = Field(None, description="ID or email of activity")
    keys: Optional[str] = Field(None, description="keys")
    operation: Optional[str] = Field(None, description="Operation")


class StravaGetstreamsTool(BaseTool):
    name: str = "strava_getstreams"
    connector_id: str = "nodes-base.strava"
    description: str = "Tool for strava getStreams operation - getStreams operation"
    args_schema: type[BaseModel] | None = StravaGetstreamsToolInput
    credentials: Optional[StravaCredentials] = None
