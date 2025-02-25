from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendinblueCredentials(BaseModel):
    """Credentials for sendInBlue authentication."""
    send_in_blue_api: Optional[Dict[str, Any]] = Field(None, description="sendInBlueApi")

class SendinblueSendtemplateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendinblueCredentials] = Field(None, description="Custom credentials for authentication")
    identifier: Optional[str] = Field(None, description="Email (urlencoded) OR ID of the contact OR its SMS attribute value")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the sender")
    receipients: Optional[str] = Field(None, description="Receipients")
    operation: Optional[str] = Field(None, description="Operation")
    template_id: Optional[str] = Field(None, description="Template ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional fields to add")


class SendinblueSendtemplateTool(BaseTool):
    name = "sendinblue_sendtemplate"
    description = "Tool for sendInBlue sendTemplate operation - sendTemplate operation"
    
    def __init__(self, credentials: Optional[SendinblueCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendInBlue sendTemplate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendInBlue sendTemplate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendInBlue sendTemplate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendInBlue sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
