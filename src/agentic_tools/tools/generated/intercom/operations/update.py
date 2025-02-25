from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntercomCredentials(BaseModel):
    """Credentials for intercom authentication."""
    intercom_api: Optional[Dict[str, Any]] = Field(None, description="intercomApi")

class IntercomUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[IntercomCredentials] = Field(None, description="Custom credentials for authentication")
    custom_attributes_json: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="Value of the property to identify the user to update")
    select_by: Optional[str] = Field(None, description="The property to select the user by")
    company_id: Optional[str] = Field(None, description="The company ID you have defined for the company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_by: Optional[str] = Field(None, description="The property via which to query the user")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    custom_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomUpdateTool(BaseTool):
    name = "intercom_update"
    description = "Tool for intercom update operation - update operation"
    
    def __init__(self, credentials: Optional[IntercomCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the intercom update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running intercom update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running intercom update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the intercom update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
