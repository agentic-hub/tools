from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SentryioGetToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    projectSlug: Optional[str] = Field(None, description="The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    organizationSlug: Optional[str] = Field(None, description="The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="The version identifier of the release")
    teamSlug: Optional[str] = Field(None, description="The slug of the team to get. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    eventId: Optional[str] = Field(None, description="The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client)")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issueId: Optional[str] = Field(None, description="ID of issue to get")
    sentryVersion: Optional[str] = Field(None, description="Sentry Version")


class SentryioGetTool(BaseTool):
    name = "sentryio_get"
    description = "Tool for sentryIo get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the sentryIo get operation."""
        # Implement the tool logic here
        return f"Running sentryIo get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sentryIo get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
