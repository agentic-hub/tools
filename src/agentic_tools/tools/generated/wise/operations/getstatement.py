from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WiseCredentials(BaseModel):
    """Credentials for wise authentication."""
    wise_api: Optional[Dict[str, Any]] = Field(None, description="wiseApi")

class WiseGetstatementToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[WiseCredentials] = Field(None, description="Custom credentials for authentication")
    format: Optional[str] = Field(None, description="File format to retrieve the statement in")
    quote_id: Optional[str] = Field(None, description="ID of the quote to retrieve")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    borderless_account_id: Optional[str] = Field(None, description="ID of the borderless account to retrieve the statement of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    transfer_id: Optional[str] = Field(None, description="ID of the transfer to delete")
    target_account_id: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    currency: Optional[str] = Field(None, description="Code of the currency of the borderless account to retrieve the statement of")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profile_id: Optional[str] = Field(None, description="ID of the user profile whose account to retrieve the statement of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    file_name: Optional[str] = Field(None, description="Name of the file that will be downloaded")


class WiseGetstatementTool(BaseTool):
    name = "wise_getstatement"
    description = "Tool for wise getStatement operation - getStatement operation"
    
    def __init__(self, credentials: Optional[WiseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the wise getStatement operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running wise getStatement operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running wise getStatement operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wise getStatement operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
