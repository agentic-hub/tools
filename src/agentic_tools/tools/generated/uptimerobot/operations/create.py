from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class UptimerobotCredentials(BaseModel):
    """Credentials for uptimeRobot authentication."""
    uptime_robot_api: Optional[Dict[str, Any]] = Field(None, description="uptimeRobotApi")

class UptimerobotCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[UptimerobotCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    start_time: Optional[str] = Field(None, description="The maintenance window start datetime")
    type: Optional[str] = Field(None, description="The type of the monitor")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="The correspondent value for the alert contact type")
    monitors: Optional[str] = Field(None, description="Monitor IDs to be displayed in status page (the values are separated with a dash (-) or 0 for all monitors)")
    id: Optional[str] = Field(None, description="The ID of the monitor")
    week_day: Optional[str] = Field(None, description="Week Day")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    url: Optional[str] = Field(None, description="The URL/IP of the monitor")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    friendly_name: Optional[str] = Field(None, description="The friendly name of the monitor")
    month_day: Optional[float] = Field(None, description="Month Day")
    duration: Optional[float] = Field(None, description="The maintenance window activation period (minutes)")


class UptimerobotCreateTool(BaseTool):
    name = "uptimerobot_create"
    description = "Tool for uptimeRobot create operation - create operation"
    
    def __init__(self, credentials: Optional[UptimerobotCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the uptimeRobot create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running uptimeRobot create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running uptimeRobot create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the uptimeRobot create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
