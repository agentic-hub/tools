from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VenafitlsprotectcloudCredentials(BaseModel):
    """Credentials for venafiTlsProtectCloud authentication."""
    venafi_tls_protect_cloud_api: Optional[Dict[str, Any]] = Field(None, description="venafiTlsProtectCloudApi")

class VenafitlsprotectcloudDownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[VenafitlsprotectcloudCredentials] = Field(None, description="Custom credentials for authentication")
    certificate_issuing_template_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    certificate_id: Optional[str] = Field(None, description="Certificate ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    operation: Optional[str] = Field(None, description="Operation")
    application_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    private_key_passphrase: Optional[str] = Field(None, description="Private Key Passphrase")
    certificate_signing_request: Optional[str] = Field(None, description="Certificate Signing Request")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    keystore_passphrase: Optional[str] = Field(None, description="Keystore Passphrase")
    certificate_label: Optional[str] = Field(None, description="Certificate Label")
    resource: Optional[str] = Field(None, description="Resource")
    download_item: Optional[str] = Field(None, description="Download Item")
    keystore_type: Optional[str] = Field(None, description="Keystore Type")


class VenafitlsprotectcloudDownloadTool(BaseTool):
    name = "venafitlsprotectcloud_download"
    description = "Tool for venafiTlsProtectCloud download operation - download operation"
    
    def __init__(self, credentials: Optional[VenafitlsprotectcloudCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the venafiTlsProtectCloud download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running venafiTlsProtectCloud download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running venafiTlsProtectCloud download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the venafiTlsProtectCloud download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
