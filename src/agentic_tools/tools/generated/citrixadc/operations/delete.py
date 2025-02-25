from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CitrixadcCredentials(BaseModel):
    """Credentials for citrixAdc authentication."""
    citrix_adc_api: Optional[Dict[str, Any]] = Field(None, description="citrixAdcApi")

class CitrixadcDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CitrixadcCredentials] = Field(None, description="Custom credentials for authentication")
    private_key_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.")
    binary_property: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    operation: Optional[str] = Field(None, description="Operation")
    file_location: Optional[str] = Field(None, description="File Location")
    certificate_format: Optional[str] = Field(None, description="Format in which the certificate is stored on the appliance")
    resource: Optional[str] = Field(None, description="Resource")
    file_name: Optional[str] = Field(None, description="Name of the file. It should not include filepath.")
    certificate_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.")


class CitrixadcDeleteTool(BaseTool):
    name = "citrixadc_delete"
    description = "Tool for citrixAdc delete operation - delete operation"
    
    def __init__(self, credentials: Optional[CitrixadcCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the citrixAdc delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running citrixAdc delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running citrixAdc delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the citrixAdc delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
