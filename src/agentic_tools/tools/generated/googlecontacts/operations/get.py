from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglecontactsCredentials(BaseModel):
    """Credentials for googleContacts authentication."""
    google_contacts_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleContactsOAuth2Api")

class GooglecontactsGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglecontactsCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsGetTool(BaseTool):
    name = "googlecontacts_get"
    description = "Tool for googleContacts get operation - get operation"
    
    def __init__(self, credentials: Optional[GooglecontactsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleContacts get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleContacts get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleContacts get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleContacts get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
