from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GrafanaCredentials

class GrafanaUpdateToolInput(BaseModel):
    dashboard_uid_or_url: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to update")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="ID of the user to update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    team_id: Optional[str] = Field(None, description="ID of the team to update")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaUpdateTool(BaseTool):
    name: str = "grafana_update"
    description: str = "Tool for grafana update operation - update operation"
    args_schema: type[BaseModel] | None = GrafanaUpdateToolInput
    credentials: Optional[GrafanaCredentials] = None
