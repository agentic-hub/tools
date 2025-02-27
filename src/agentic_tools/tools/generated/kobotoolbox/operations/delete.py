from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KobotoolboxCredentials

class KobotoolboxDeleteToolInput(BaseModel):
    file_id: Optional[str] = Field(None, description="Uid of the file (should start with \"af\" e.g. \"afQoJxA4kmKEXVpkH6SYbhb\"")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property to write the file into")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    submission_id: Optional[str] = Field(None, description="Submission ID (number, e.g. 245128)")


class KobotoolboxDeleteTool(BaseTool):
    name: str = "kobotoolbox_delete"
    connector_id: str = "nodes-base.koBoToolbox"
    description: str = "Tool for koBoToolbox delete operation - delete operation"
    args_schema: type[BaseModel] | None = KobotoolboxDeleteToolInput
    credentials: Optional[KobotoolboxCredentials] = None
