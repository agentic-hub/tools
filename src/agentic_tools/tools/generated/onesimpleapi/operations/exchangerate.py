from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiExchangerateToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    from_currency: Optional[str] = Field(None, description="From Currency")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="Value to convert")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    to_currency: Optional[str] = Field(None, description="To Currency")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiExchangerateTool(BaseTool):
    name: str = "onesimpleapi_exchangerate"
    description: str = "Tool for oneSimpleApi exchangeRate operation - exchangeRate operation"
    args_schema: type[BaseModel] | None = OnesimpleapiExchangerateToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
