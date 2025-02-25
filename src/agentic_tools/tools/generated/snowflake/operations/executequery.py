from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SnowflakeCredentials(BaseModel):
    """Credentials for snowflake authentication."""
    snowflake: Optional[Dict[str, Any]] = Field(None, description="snowflake")

class SnowflakeExecutequeryToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SnowflakeCredentials] = Field(None, description="Custom credentials for authentication")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    query: Optional[str] = Field(None, description="The SQL query to execute")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class SnowflakeExecutequeryTool(BaseTool):
    name = "snowflake_executequery"
    description = "Tool for snowflake executeQuery operation - executeQuery operation"
    
    def __init__(self, credentials: Optional[SnowflakeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the snowflake executeQuery operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running snowflake executeQuery operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running snowflake executeQuery operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the snowflake executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
