from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GrafanaDeleteToolInput(BaseModel):
    dashboardUidOrUrl: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    userId: Optional[str] = Field(None, description="ID of the user to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    teamId: Optional[str] = Field(None, description="ID of the team to delete")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaDeleteTool(BaseTool):
    name = "grafana_delete"
    description = "Tool for grafana delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the grafana delete operation."""
        # Implement the tool logic here
        return f"Running grafana delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grafana delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
