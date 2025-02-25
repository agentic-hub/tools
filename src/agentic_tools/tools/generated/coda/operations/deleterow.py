from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CodaCredentials(BaseModel):
    """Credentials for coda authentication."""
    coda_api: Optional[Dict[str, Any]] = Field(None, description="codaApi")

class CodaDeleterowToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CodaCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    doc_id: Optional[str] = Field(None, description="ID of the doc. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    table_id: Optional[str] = Field(None, description="The table to delete the row in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    column_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    row_id: Optional[str] = Field(None, description="Row IDs to delete")
    operation: Optional[str] = Field(None, description="Operation")
    view_id: Optional[str] = Field(None, description="The view to get the row from")


class CodaDeleterowTool(BaseTool):
    name = "coda_deleterow"
    description = "Tool for coda deleteRow operation - deleteRow operation"
    
    def __init__(self, credentials: Optional[CodaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the coda deleteRow operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running coda deleteRow operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running coda deleteRow operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the coda deleteRow operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
