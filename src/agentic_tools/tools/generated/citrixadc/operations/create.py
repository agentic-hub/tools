from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CitrixadcCredentials

class CitrixadcCreateToolInput(BaseModel):
    private_key_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.")
    private_key_format: Optional[str] = Field(None, description="Format in which the key is stored on the appliance")
    ca_private_key_file_format: Optional[str] = Field(None, description="Format of the CA certificate")
    certificate_request_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path.")
    binary_property: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    operation: Optional[str] = Field(None, description="Operation")
    ca_private_key_file_name: Optional[str] = Field(None, description="Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key.")
    file_location: Optional[str] = Field(None, description="File Location")
    certificate_type: Optional[str] = Field(None, description="Certificate Type")
    certificate_format: Optional[str] = Field(None, description="Format in which the certificate is stored on the appliance")
    ca_certificate_file_name: Optional[str] = Field(None, description="Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates")
    resource: Optional[str] = Field(None, description="Resource")
    ca_serial_file_number: Optional[str] = Field(None, description="Serial number file maintained for the CA certificate. This file contains the serial number of the next certificate to be issued or signed by the CA.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    ca_certificate_file_format: Optional[str] = Field(None, description="Format of the CA certificate")
    certificate_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.")


class CitrixadcCreateTool(BaseTool):
    name: str = "citrixadc_create"
    description: str = "Tool for citrixAdc create operation - create operation"
    args_schema: type[BaseModel] | None = CitrixadcCreateToolInput
    credentials: Optional[CitrixadcCredentials] = None
