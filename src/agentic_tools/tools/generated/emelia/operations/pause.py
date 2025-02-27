from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EmeliaCredentials

class EmeliaPauseToolInput(BaseModel):
    contact_email: Optional[str] = Field(None, description="The email of the contact to add to the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="The ID of the campaign to pause. The campaign must be in RUNNING mode.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaign_name: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")


class EmeliaPauseTool(BaseTool):
    name: str = "emelia_pause"
    description: str = "Tool for emelia pause operation - pause operation"
    args_schema: type[BaseModel] | None = EmeliaPauseToolInput
    credentials: Optional[EmeliaCredentials] = None
