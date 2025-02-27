from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GrafanaCredentials

class GrafanaDeleteToolInput(BaseModel):
    dashboard_uid_or_url: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="ID of the user to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    team_id: Optional[str] = Field(None, description="ID of the team to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaDeleteTool(BaseTool):
    name: str = "grafana_delete"
    connector_id: str = "nodes-base.grafana"
    description: str = "Tool for grafana delete operation - delete operation"
    args_schema: type[BaseModel] | None = GrafanaDeleteToolInput
    credentials: Optional[GrafanaCredentials] = None
