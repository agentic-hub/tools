from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CitrixadcCredentials

class CitrixadcUploadToolInput(BaseModel):
    private_key_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.")
    binary_property: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    operation: Optional[str] = Field(None, description="Operation")
    file_location: Optional[str] = Field(None, description="File Location")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    certificate_format: Optional[str] = Field(None, description="Format in which the certificate is stored on the appliance")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.")


class CitrixadcUploadTool(BaseTool):
    name: str = "citrixadc_upload"
    description: str = "Tool for citrixAdc upload operation - upload operation"
    args_schema: type[BaseModel] | None = CitrixadcUploadToolInput
    credentials: Optional[CitrixadcCredentials] = None
