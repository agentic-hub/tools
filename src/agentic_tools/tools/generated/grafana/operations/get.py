from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GrafanaCredentials

class GrafanaGetToolInput(BaseModel):
    dashboard_uid_or_url: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to retrieve")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    team_id: Optional[str] = Field(None, description="ID of the team to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaGetTool(BaseTool):
    name: str = "grafana_get"
    connector_id: str = "nodes-base.grafana"
    description: str = "Tool for grafana get operation - get operation"
    args_schema: type[BaseModel] | None = GrafanaGetToolInput
    credentials: Optional[GrafanaCredentials] = None
