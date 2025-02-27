from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiPdfToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiPdfTool(BaseTool):
    name: str = "onesimpleapi_pdf"
    description: str = "Tool for oneSimpleApi pdf operation - pdf operation"
    args_schema: type[BaseModel] | None = OnesimpleapiPdfToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
