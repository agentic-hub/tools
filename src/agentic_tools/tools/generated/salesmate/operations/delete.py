from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SalesmateCredentials(BaseModel):
    """Credentials for salesmate authentication."""
    salesmate_api: Optional[Dict[str, Any]] = Field(None, description="salesmateApi")

class SalesmateDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SalesmateCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    raw_data: Optional[bool] = Field(None, description="Whether the data should include the fields details")
    id: Optional[str] = Field(None, description="If more than one company add them separated by ,")
    operation: Optional[str] = Field(None, description="Operation")
    filters_json: Optional[str] = Field(None, description="Filters")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    title: Optional[str] = Field(None, description="Title")
    owner: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class SalesmateDeleteTool(BaseTool):
    name = "salesmate_delete"
    description = "Tool for salesmate delete operation - delete operation"
    
    def __init__(self, credentials: Optional[SalesmateCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the salesmate delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running salesmate delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running salesmate delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the salesmate delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
