from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DropcontactCredentials

class DropcontactEnrichToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    simplify: Optional[bool] = Field(None, description="When off, waits for the contact data before completing. Waiting time can be adjusted with Extend Wait Time option. When on, returns a request_id that can be used later in the Fetch Request operation.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="Email")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class DropcontactEnrichTool(BaseTool):
    name: str = "dropcontact_enrich"
    description: str = "Tool for dropcontact enrich operation - enrich operation"
    args_schema: type[BaseModel] | None = DropcontactEnrichToolInput
    credentials: Optional[DropcontactCredentials] = None
