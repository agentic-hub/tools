from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiQrcodeToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the QR code or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The text that should be turned into a QR code - like a website URL")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiQrcodeTool(BaseTool):
    name: str = "onesimpleapi_qrcode"
    description: str = "Tool for oneSimpleApi qrCode operation - qrCode operation"
    args_schema: type[BaseModel] | None = OnesimpleapiQrcodeToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
