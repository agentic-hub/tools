from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SentryioCredentials

class SentryioGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    project_slug: Optional[str] = Field(None, description="The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    organization_slug: Optional[str] = Field(None, description="The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="The version identifier of the release")
    team_slug: Optional[str] = Field(None, description="The slug of the team to get. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    event_id: Optional[str] = Field(None, description="The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client)")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="ID of issue to get")
    sentry_version: Optional[str] = Field(None, description="Sentry Version")


class SentryioGetTool(BaseTool):
    name: str = "sentryio_get"
    description: str = "Tool for sentryIo get operation - get operation"
    args_schema: type[BaseModel] | None = SentryioGetToolInput
    credentials: Optional[SentryioCredentials] = None
