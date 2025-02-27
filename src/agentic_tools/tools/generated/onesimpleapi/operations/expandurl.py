from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiExpandurlToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="URL to unshorten")


class OnesimpleapiExpandurlTool(BaseTool):
    name: str = "onesimpleapi_expandurl"
    description: str = "Tool for oneSimpleApi expandURL operation - expandURL operation"
    args_schema: type[BaseModel] | None = OnesimpleapiExpandurlToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
