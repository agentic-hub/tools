from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglebigqueryCredentials(BaseModel):
    """Credentials for googleBigQuery authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_big_query_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleBigQueryOAuth2Api")

class GooglebigqueryInsertToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglebigqueryCredentials] = Field(None, description="Custom credentials for authentication")
    data_mode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="By ID")
    dataset_id: Optional[str] = Field(None, description="By ID")
    project_id: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sql_query: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in BigQuery. (Use an 'Edit Fields' node before this node to change them if required.)")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class GooglebigqueryInsertTool(BaseTool):
    name = "googlebigquery_insert"
    description = "Tool for googleBigQuery insert operation - insert operation"
    
    def __init__(self, credentials: Optional[GooglebigqueryCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleBigQuery insert operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleBigQuery insert operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleBigQuery insert operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleBigQuery insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
