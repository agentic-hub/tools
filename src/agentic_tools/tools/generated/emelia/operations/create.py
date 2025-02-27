from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EmeliaCredentials

class EmeliaCreateToolInput(BaseModel):
    contact_email: Optional[str] = Field(None, description="The email of the contact to add to the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="The ID of the campaign to add the contact to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaign_name: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")


class EmeliaCreateTool(BaseTool):
    name: str = "emelia_create"
    description: str = "Tool for emelia create operation - create operation"
    args_schema: type[BaseModel] | None = EmeliaCreateToolInput
    credentials: Optional[EmeliaCredentials] = None
