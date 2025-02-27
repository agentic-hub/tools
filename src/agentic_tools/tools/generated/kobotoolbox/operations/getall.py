from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KobotoolboxCredentials

class KobotoolboxGetallToolInput(BaseModel):
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters\" target=\"_blank\">Formhub API docs</a> to creating filters, using the MongoDB JSON format - e.g. {\"_submission_time\":{\"$lt\":\"2021-10-01T01:02:03\"}}")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property to write the file into")
    operation: Optional[str] = Field(None, description="Operation")
    form_id: Optional[str] = Field(None, description="Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    filter_type: Optional[str] = Field(None, description="Filter")


class KobotoolboxGetallTool(BaseTool):
    name: str = "kobotoolbox_getall"
    description: str = "Tool for koBoToolbox getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = KobotoolboxGetallToolInput
    credentials: Optional[KobotoolboxCredentials] = None
