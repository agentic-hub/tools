from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WebhookCredentials(BaseModel):
    """Credentials for webhook authentication."""
    http_basic_auth: Optional[Dict[str, Any]] = Field(None, description="httpBasicAuth")
    http_header_auth: Optional[Dict[str, Any]] = Field(None, description="httpHeaderAuth")

class WebhookDefaultToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[WebhookCredentials] = Field(None, description="Custom credentials for authentication")
    response_data: Optional[str] = Field(None, description="What data should be returned. If it should return all items as an array or only the first item as object.")
    http_method: Optional[str] = Field(None, description="The HTTP method to listen to")
    webhook_notice: Optional[str] = Field(None, description="Insert a 'Respond to Webhook' node to control when and how you respond. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook/\" target=\"_blank\">More details</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    response_mode: Optional[str] = Field(None, description="When and how to respond to the webhook")
    response_binary_property_name: Optional[str] = Field(None, description="Name of the binary property to return")
    response_code: Optional[float] = Field(None, description="The HTTP Response code to return")
    path: Optional[str] = Field(None, description="The path to listen to")


class WebhookDefaultTool(BaseTool):
    name = "webhook_default"
    description = "Tool for webhook default operation - default operation"
    
    def __init__(self, credentials: Optional[WebhookCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the webhook default operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running webhook default operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running webhook default operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the webhook default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
