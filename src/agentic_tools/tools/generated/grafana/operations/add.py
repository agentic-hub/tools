from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GrafanaAddToolInput(BaseModel):
    dashboardUidOrUrl: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    userId: Optional[str] = Field(None, description="User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    teamId: Optional[str] = Field(None, description="Team to add the user to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaAddTool(BaseTool):
    name = "grafana_add"
    description = "Tool for grafana add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the grafana add operation."""
        # Implement the tool logic here
        return f"Running grafana add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grafana add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
