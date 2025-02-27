from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SentryioCredentials

class SentryioUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    project_slug: Optional[str] = Field(None, description="The slug of the project to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    organization_slug: Optional[str] = Field(None, description="The slug of the organization to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    organization_slug: Optional[str] = Field(None, description="The slug of the organization the project belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="A version identifier for this release. Can be a version number, a commit hash etc.")
    team_slug: Optional[str] = Field(None, description="The slug of the team to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="ID of issue to get")
    sentry_version: Optional[str] = Field(None, description="Sentry Version")


class SentryioUpdateTool(BaseTool):
    name: str = "sentryio_update"
    connector_id: str = "nodes-base.sentryIo"
    description: str = "Tool for sentryIo update operation - update operation"
    args_schema: type[BaseModel] | None = SentryioUpdateToolInput
    credentials: Optional[SentryioCredentials] = None
