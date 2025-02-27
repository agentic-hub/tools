from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiImagemetadataToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Image to get metadata from")


class OnesimpleapiImagemetadataTool(BaseTool):
    name: str = "onesimpleapi_imagemetadata"
    description: str = "Tool for oneSimpleApi imageMetadata operation - imageMetadata operation"
    args_schema: type[BaseModel] | None = OnesimpleapiImagemetadataToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
