from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KobotoolboxCredentials

class KobotoolboxCreateToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property containing the file to upload. Supported types: image, audio, video, csv, xml, zip.")
    file_mode: Optional[str] = Field(None, description="File Upload Mode")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    file_url: Optional[str] = Field(None, description="HTTP(s) link to the file to upload")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")


class KobotoolboxCreateTool(BaseTool):
    name: str = "kobotoolbox_create"
    description: str = "Tool for koBoToolbox create operation - create operation"
    args_schema: type[BaseModel] | None = KobotoolboxCreateToolInput
    credentials: Optional[KobotoolboxCredentials] = None
