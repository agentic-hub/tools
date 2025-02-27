from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VenafitlsprotectcloudCredentials

class VenafitlsprotectcloudDownloadToolInput(BaseModel):
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
    name: str = "venafitlsprotectcloud_download"
    description: str = "Tool for venafiTlsProtectCloud download operation - download operation"
    args_schema: type[BaseModel] | None = VenafitlsprotectcloudDownloadToolInput
    credentials: Optional[VenafitlsprotectcloudCredentials] = None
