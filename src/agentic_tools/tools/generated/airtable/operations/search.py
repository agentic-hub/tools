from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AirtableCredentials(BaseModel):
    """Credentials for airtable authentication."""
    airtable_token_api: Optional[Dict[str, Any]] = Field(None, description="airtableTokenApi")
    airtable_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="airtableOAuth2Api")

class AirtableSearchToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AirtableCredentials] = Field(None, description="Custom credentials for authentication")
    sort: Optional[Dict[str, Any]] = Field(None, description="Defines how the returned records should be ordered")
    table: Optional[str] = Field(None, description="By URL")
    base: Optional[Dict[str, Any]] = Field(None, description="Base")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional options which decide which records should be returned")
    authentication: Optional[str] = Field(None, description="Authentication")
    filter_by_formula: Optional[str] = Field(None, description="The formula will be evaluated for each record, and if the result is not 0, false, \"\", NaN, [], or #Error! the record will be included in the response. <a href=\"https://support.airtable.com/docs/formula-field-reference\" target=\"_blank\">More info</a>.")
    id: Optional[str] = Field(None, description="ID of the record to delete. <a href=\"https://support.airtable.com/docs/record-id\" target=\"_blank\">More info</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="columns")


class AirtableSearchTool(BaseTool):
    name = "airtable_search"
    description = "Tool for airtable search operation - search operation"
    
    def __init__(self, credentials: Optional[AirtableCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the airtable search operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running airtable search operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running airtable search operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the airtable search operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
