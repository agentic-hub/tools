from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CryptoDefaultToolInput(BaseModel):
    secret: Optional[str] = Field(None, description="Secret")
    action: Optional[str] = Field(None, description="Action")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property which contains the input data")
    value: Optional[str] = Field(None, description="The value that should be hashed")
    encoding: Optional[str] = Field(None, description="Encoding")
    private_key: Optional[str] = Field(None, description="Private key to use when signing the string")
    encoding_type: Optional[str] = Field(None, description="Encoding that will be used to generate string")
    string_length: Optional[float] = Field(None, description="Length of the generated string")
    algorithm: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    binary_data: Optional[bool] = Field(None, description="Whether the data to hashed should be taken from binary field")
    data_property_name: Optional[str] = Field(None, description="Name of the property to which to write the hash")
    type: Optional[str] = Field(None, description="The hash type to use")


class CryptoDefaultTool(BaseTool):
    name: str = "crypto_default"
    description: str = "Tool for crypto default operation - default operation"
    args_schema: type[BaseModel] | None = CryptoDefaultToolInput
