from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftsqlCredentials(BaseModel):
    """Credentials for microsoftSql authentication."""
    microsoft_sql: Optional[Dict[str, Any]] = Field(None, description="microsoftSql")

class MicrosoftsqlDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MicrosoftsqlCredentials] = Field(None, description="Custom credentials for authentication")
    table: Optional[str] = Field(None, description="Name of the table in which to delete data")
    delete_key: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be deleted. Normally that would be \"id\".")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlDeleteTool(BaseTool):
    name = "microsoftsql_delete"
    description = "Tool for microsoftSql delete operation - delete operation"
    
    def __init__(self, credentials: Optional[MicrosoftsqlCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the microsoftSql delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running microsoftSql delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running microsoftSql delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftSql delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
