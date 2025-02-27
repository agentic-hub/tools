from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftgraphsecurityCredentials

class MicrosoftgraphsecurityUpdateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    secure_score_control_profile_id: Optional[str] = Field(None, description="ID of the secure score control profile to update")
    provider: Optional[str] = Field(None, description="Name of the provider of the security product or service")
    vendor: Optional[str] = Field(None, description="Name of the vendor of the security product or service")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftgraphsecurityUpdateTool(BaseTool):
    name: str = "microsoftgraphsecurity_update"
    connector_id: str = "nodes-base.microsoftGraphSecurity"
    description: str = "Tool for microsoftGraphSecurity update operation - update operation"
    args_schema: type[BaseModel] | None = MicrosoftgraphsecurityUpdateToolInput
    credentials: Optional[MicrosoftgraphsecurityCredentials] = None
