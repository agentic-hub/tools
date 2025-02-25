from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GrafanaGetallToolInput(BaseModel):
    dashboardUidOrUrl: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    userId: Optional[str] = Field(None, description="User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    teamId: Optional[str] = Field(None, description="Team to retrieve all members from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaGetallTool(BaseTool):
    name = "grafana_getall"
    description = "Tool for grafana getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the grafana getAll operation."""
        # Implement the tool logic here
        return f"Running grafana getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grafana getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
