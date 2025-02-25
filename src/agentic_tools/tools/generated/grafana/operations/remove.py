from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GrafanaCredentials(BaseModel):
    """Credentials for grafana authentication."""
    grafana_api: Optional[Dict[str, Any]] = Field(None, description="grafanaApi")

class GrafanaRemoveToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GrafanaCredentials] = Field(None, description="Custom credentials for authentication")
    dashboard_uid_or_url: Optional[str] = Field(None, description="Unique alphabetic identifier or URL of the dashboard to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_id: Optional[str] = Field(None, description="User to add to a team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    team_id: Optional[str] = Field(None, description="Team to remove the user from. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    member_id: Optional[str] = Field(None, description="User to remove from the team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class GrafanaRemoveTool(BaseTool):
    name = "grafana_remove"
    description = "Tool for grafana remove operation - remove operation"
    
    def __init__(self, credentials: Optional[GrafanaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the grafana remove operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running grafana remove operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running grafana remove operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the grafana remove operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
