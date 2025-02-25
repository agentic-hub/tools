from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VenafitlsprotectdatacenterCredentials(BaseModel):
    """Credentials for venafiTlsProtectDatacenter authentication."""
    venafi_tls_protect_datacenter_api: Optional[Dict[str, Any]] = Field(None, description="venafiTlsProtectDatacenterApi")

class VenafitlsprotectdatacenterDownloadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[VenafitlsprotectdatacenterCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_dn: Optional[str] = Field(None, description="Certificate DN")
    binary_property: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded")
    password: Optional[str] = Field(None, description="Password")
    operation: Optional[str] = Field(None, description="Operation")
    include_private_key: Optional[bool] = Field(None, description="Include Private Key")


class VenafitlsprotectdatacenterDownloadTool(BaseTool):
    name = "venafitlsprotectdatacenter_download"
    description = "Tool for venafiTlsProtectDatacenter download operation - download operation"
    
    def __init__(self, credentials: Optional[VenafitlsprotectdatacenterCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the venafiTlsProtectDatacenter download operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running venafiTlsProtectDatacenter download operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running venafiTlsProtectDatacenter download operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the venafiTlsProtectDatacenter download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
