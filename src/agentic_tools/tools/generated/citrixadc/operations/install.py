from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CitrixadcCredentials

class CitrixadcInstallToolInput(BaseModel):
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
    name: str = "citrixadc_install"
    connector_id: str = "nodes-base.citrixAdc"
    description: str = "Tool for citrixAdc install operation - install operation"
    args_schema: type[BaseModel] | None = CitrixadcInstallToolInput
    credentials: Optional[CitrixadcCredentials] = None
