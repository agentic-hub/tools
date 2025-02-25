from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SentryioDeleteToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    projectSlug: Optional[str] = Field(None, description="The slug of the project to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The slug of the organization the team should be created for")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    organizationSlug: Optional[str] = Field(None, description="The slug of the organization the project belong to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    projects: Optional[str] = Field(None, description="projects")
    version: Optional[str] = Field(None, description="The version identifier of the release")
    teamSlug: Optional[str] = Field(None, description="The slug of the team to delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    issueId: Optional[str] = Field(None, description="ID of issue to get")
    sentryVersion: Optional[str] = Field(None, description="Sentry Version")


class SentryioDeleteTool(BaseTool):
    name = "sentryio_delete"
    description = "Tool for sentryIo delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the sentryIo delete operation."""
        # Implement the tool logic here
        return f"Running sentryIo delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sentryIo delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
