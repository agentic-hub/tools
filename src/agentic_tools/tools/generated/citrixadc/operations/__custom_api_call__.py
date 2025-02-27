from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CitrixadcCredentials

class Citrixadc__custom_api_call__ToolInput(BaseModel):
    private_key_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.")
    binary_property: Optional[str] = Field(None, description="The name of the incoming field containing the binary file data to be processed")
    operation: Optional[str] = Field(None, description="Operation")
    file_location: Optional[str] = Field(None, description="File Location")
    certificate_format: Optional[str] = Field(None, description="Format in which the certificate is stored on the appliance")
    resource: Optional[str] = Field(None, description="Resource")
    certificate_file_name: Optional[str] = Field(None, description="Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.")


class Citrixadc__custom_api_call__Tool(BaseTool):
    name: str = "citrixadc___custom_api_call__"
    description: str = "Tool for citrixAdc __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Citrixadc__custom_api_call__ToolInput
    credentials: Optional[CitrixadcCredentials] = None
