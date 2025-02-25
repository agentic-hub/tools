from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WhatsappCredentials(BaseModel):
    """Credentials for whatsApp authentication."""
    whats_app_api: Optional[Dict[str, Any]] = Field(None, description="whatsAppApi")

class WhatsappSendtemplateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[WhatsappCredentials] = Field(None, description="Custom credentials for authentication")
    recipient_phone_number: Optional[str] = Field(None, description="Phone number of the recipient of the message")
    template: Optional[str] = Field(None, description="Name of the template")
    media_path: Optional[str] = Field(None, description="Use a link, an ID, or n8n to upload an audio file")
    operation: Optional[str] = Field(None, description="Operation")
    messaging_product: Optional[str] = Field(None, description="Messaging Product")
    components: Optional[Dict[str, Any]] = Field(None, description="Components")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    media_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    phone_number_id: Optional[str] = Field(None, description="The ID of the business account's phone number from which the message will be sent from")


class WhatsappSendtemplateTool(BaseTool):
    name = "whatsapp_sendtemplate"
    description = "Tool for whatsApp sendTemplate operation - sendTemplate operation"
    
    def __init__(self, credentials: Optional[WhatsappCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the whatsApp sendTemplate operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running whatsApp sendTemplate operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running whatsApp sendTemplate operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the whatsApp sendTemplate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
