from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftgraphsecurityCredentials

class MicrosoftgraphsecurityGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    secure_score_control_profile_id: Optional[str] = Field(None, description="ID of the secure score control profile to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftgraphsecurityGetallTool(BaseTool):
    name: str = "microsoftgraphsecurity_getall"
    description: str = "Tool for microsoftGraphSecurity getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MicrosoftgraphsecurityGetallToolInput
    credentials: Optional[MicrosoftgraphsecurityCredentials] = None
