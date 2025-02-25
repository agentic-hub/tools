from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CockpitCredentials(BaseModel):
    """Credentials for cockpit authentication."""
    cockpit_api: Optional[Dict[str, Any]] = Field(None, description="cockpitApi")

class CockpitSubmitToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CockpitCredentials] = Field(None, description="Custom credentials for authentication")
    json_data_fields: Optional[bool] = Field(None, description="Whether form fields should be set via the value-key pair UI or JSON")
    form: Optional[str] = Field(None, description="Name of the form to operate on")
    resource: Optional[str] = Field(None, description="Resource")
    singleton: Optional[str] = Field(None, description="Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    collection: Optional[str] = Field(None, description="Name of the collection to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    data_fields_ui: Optional[Dict[str, Any]] = Field(None, description="Form data to send")
    data_fields_json: Optional[str] = Field(None, description="Form data to send as JSON")
    operation: Optional[str] = Field(None, description="Operation")


class CockpitSubmitTool(BaseTool):
    name = "cockpit_submit"
    description = "Tool for cockpit submit operation - submit operation"
    
    def __init__(self, credentials: Optional[CockpitCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the cockpit submit operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running cockpit submit operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running cockpit submit operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cockpit submit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
