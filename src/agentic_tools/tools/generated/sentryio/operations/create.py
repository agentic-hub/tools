from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SentryioCredentials

class SentryioCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    project_slug: Optional[str] = Field(None, description="The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    agree_terms: Optional[bool] = Field(None, description="Whether you agree to the applicable terms of service and privacy policy of Sentry.io")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="A URL that points to the release. This can be the path to an online interface to the sourcecode for instance.")
    organization_slug: Optional[str] = Field(None, description="The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="A version identifier for this release. Can be a version number, a commit hash etc.")
    team_slug: Optional[str] = Field(None, description="The slug of the team to create a new project for. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="ID of issue to get")
    sentry_version: Optional[str] = Field(None, description="Sentry Version")


class SentryioCreateTool(BaseTool):
    name: str = "sentryio_create"
    connector_id: str = "nodes-base.sentryIo"
    description: str = "Tool for sentryIo create operation - create operation"
    args_schema: type[BaseModel] | None = SentryioCreateToolInput
    credentials: Optional[SentryioCredentials] = None
