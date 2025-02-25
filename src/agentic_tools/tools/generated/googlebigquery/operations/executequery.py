from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglebigqueryCredentials(BaseModel):
    """Credentials for googleBigQuery authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_big_query_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleBigQueryOAuth2Api")

class GooglebigqueryExecutequeryToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglebigqueryCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    project_id: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sql_query: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebigqueryExecutequeryTool(BaseTool):
    name = "googlebigquery_executequery"
    description = "Tool for googleBigQuery executeQuery operation - executeQuery operation"
    
    def __init__(self, credentials: Optional[GooglebigqueryCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleBigQuery executeQuery operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleBigQuery executeQuery operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleBigQuery executeQuery operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleBigQuery executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
