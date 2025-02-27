from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiInstagramprofileToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    profile_name: Optional[str] = Field(None, description="Profile name to get details of")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiInstagramprofileTool(BaseTool):
    name: str = "onesimpleapi_instagramprofile"
    description: str = "Tool for oneSimpleApi instagramProfile operation - instagramProfile operation"
    args_schema: type[BaseModel] | None = OnesimpleapiInstagramprofileToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
