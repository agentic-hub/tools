from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Grafana__custom_api_call__ToolInput(BaseModel):
    dashboardUidOrUrl: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    userId: Optional[str] = Field(None, description="User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    teamId: Optional[str] = Field(None, description="ID of the team to delete")
    operation: Optional[str] = Field(None, description="Operation")


class Grafana__custom_api_call__Tool(BaseTool):
    name = "grafana___custom_api_call__"
    description = "Tool for grafana __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the grafana __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running grafana __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grafana __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
