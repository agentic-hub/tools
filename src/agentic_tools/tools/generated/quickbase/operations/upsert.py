from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class QuickbaseCredentials(BaseModel):
    """Credentials for quickbase authentication."""
    quickbase_api: Optional[Dict[str, Any]] = Field(None, description="quickbaseApi")

class QuickbaseUpsertToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[QuickbaseCredentials] = Field(None, description="Custom credentials for authentication")
    update_key: Optional[str] = Field(None, description="Update can use the key field on the table, or any other supported unique field")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="The table identifier")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    merge_field_id: Optional[str] = Field(None, description="<p>You're updating records in a Quick Base table with data from an external file. In order for a merge like this to work, Quick Base needs a way to match records in the source data with corresponding records in the destination table.</p><p>You make this possible by choosing the field in the app table that holds unique matching values. This is called a merge field.</p>. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    report_id: Optional[str] = Field(None, description="The identifier of the report, unique to the table")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class QuickbaseUpsertTool(BaseTool):
    name = "quickbase_upsert"
    description = "Tool for quickbase upsert operation - upsert operation"
    
    def __init__(self, credentials: Optional[QuickbaseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the quickbase upsert operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running quickbase upsert operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running quickbase upsert operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the quickbase upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
