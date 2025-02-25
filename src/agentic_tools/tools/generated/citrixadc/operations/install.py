from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CitrixadcCredentials(BaseModel):
    """Credentials for citrixAdc authentication."""
    citrix_adc_api: Optional[Dict[str, Any]] = Field(None, description="citrixAdcApi")

class CitrixadcInstallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CitrixadcCredentials] = Field(None, description="Custom credentials for authentication")
    private_key_file_name: Optional[str] = Field(None, description="Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path.")
    notification_period: Optional[float] = Field(None, description="Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire")
    certificate_key_pair_name: Optional[str] = Field(None, description="Name for the certificate and private-key pair")
    notify_expiration: Optional[bool] = Field(None, description="Whether to alert when the certificate is about to expire")
    binary_property: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    password: Optional[str] = Field(None, description="Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange.")
    operation: Optional[str] = Field(None, description="Operation")
    file_location: Optional[str] = Field(None, description="File Location")
    certificate_bundle: Optional[bool] = Field(None, description="Whether to parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file")
    certificate_format: Optional[str] = Field(None, description="Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange.")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_file_name: Optional[str] = Field(None, description="Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. /nsconfig/ssl/ is the default path.")


class CitrixadcInstallTool(BaseTool):
    name = "citrixadc_install"
    description = "Tool for citrixAdc install operation - install operation"
    
    def __init__(self, credentials: Optional[CitrixadcCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the citrixAdc install operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running citrixAdc install operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running citrixAdc install operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the citrixAdc install operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
