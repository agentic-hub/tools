from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HomeassistantCredentials(BaseModel):
    """Credentials for homeAssistant authentication."""
    home_assistant_api: Optional[Dict[str, Any]] = Field(None, description="homeAssistantApi")

class HomeassistantUpsertToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HomeassistantCredentials] = Field(None, description="Custom credentials for authentication")
    entity_id: Optional[str] = Field(None, description="The entity ID for which a state will be created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    state: Optional[str] = Field(None, description="State")
    state_attributes: Optional[Dict[str, Any]] = Field(None, description="State Attributes")
    operation: Optional[str] = Field(None, description="Operation")


class HomeassistantUpsertTool(BaseTool):
    name = "homeassistant_upsert"
    description = "Tool for homeAssistant upsert operation - upsert operation"
    
    def __init__(self, credentials: Optional[HomeassistantCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the homeAssistant upsert operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running homeAssistant upsert operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running homeAssistant upsert operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the homeAssistant upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
