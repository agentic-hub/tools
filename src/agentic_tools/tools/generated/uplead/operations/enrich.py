from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import UpleadCredentials

class UpleadEnrichToolInput(BaseModel):
    company: Optional[str] = Field(None, description="The name of the company (e.g – amazon)")
    lastname: Optional[str] = Field(None, description="Last name of the person (e.g – Benioff)")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address (e.g – mbenioff@salesforce.com)")
    firstname: Optional[str] = Field(None, description="First name of the person (e.g – Marc)")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name (e.g – amazon.com)")


class UpleadEnrichTool(BaseTool):
    name: str = "uplead_enrich"
    connector_id: str = "nodes-base.uplead"
    description: str = "Tool for uplead enrich operation - enrich operation"
    args_schema: type[BaseModel] | None = UpleadEnrichToolInput
    credentials: Optional[UpleadCredentials] = None
