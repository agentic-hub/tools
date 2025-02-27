from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KobotoolboxCredentials

class KobotoolboxGetlogsToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property to write the file into")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    hook_id: Optional[str] = Field(None, description="Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4)")
    end_date: Optional[str] = Field(None, description="Maximum date for the hook log to retrieve")
    resource: Optional[str] = Field(None, description="Resource")
    status: Optional[str] = Field(None, description="Only retrieve logs with a specific status")
    start_date: Optional[str] = Field(None, description="Minimum date for the hook log to retrieve")


class KobotoolboxGetlogsTool(BaseTool):
    name: str = "kobotoolbox_getlogs"
    description: str = "Tool for koBoToolbox getLogs operation - getLogs operation"
    args_schema: type[BaseModel] | None = KobotoolboxGetlogsToolInput
    credentials: Optional[KobotoolboxCredentials] = None
