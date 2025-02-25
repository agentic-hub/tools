from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CustomerioCredentials(BaseModel):
    """Credentials for customerIo authentication."""
    customer_io_api: Optional[Dict[str, Any]] = Field(None, description="customerIoApi")

class CustomerioRemoveToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CustomerioCredentials] = Field(None, description="Custom credentials for authentication")
    event_name: Optional[str] = Field(None, description="Name of the event to track")
    customer_ids: Optional[str] = Field(None, description="A list of customer IDs to add to the segment")
    segment_id: Optional[float] = Field(None, description="The unique identifier of the segment")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioRemoveTool(BaseTool):
    name = "customerio_remove"
    description = "Tool for customerIo remove operation - remove operation"
    
    def __init__(self, credentials: Optional[CustomerioCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the customerIo remove operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running customerIo remove operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running customerIo remove operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the customerIo remove operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
