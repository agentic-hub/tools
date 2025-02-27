from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnesimpleapiCredentials

class OnesimpleapiSpotifyartistprofileToolInput(BaseModel):
    download: Optional[bool] = Field(None, description="Whether to download the PDF or return a link to it")
    output: Optional[str] = Field(None, description="The name of the output field to put the binary file data in")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    artist_name: Optional[str] = Field(None, description="Artist name to get details for")
    operation: Optional[str] = Field(None, description="Operation")
    link: Optional[str] = Field(None, description="Link to webpage to convert")


class OnesimpleapiSpotifyartistprofileTool(BaseTool):
    name: str = "onesimpleapi_spotifyartistprofile"
    connector_id: str = "nodes-base.oneSimpleApi"
    description: str = "Tool for oneSimpleApi spotifyArtistProfile operation - spotifyArtistProfile operation"
    args_schema: type[BaseModel] | None = OnesimpleapiSpotifyartistprofileToolInput
    credentials: Optional[OnesimpleapiCredentials] = None
