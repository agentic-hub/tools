from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClearbitCredentials

class ClearbitEnrichToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="The email address to look up")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain to look up")


class ClearbitEnrichTool(BaseTool):
    name: str = "clearbit_enrich"
    connector_id: str = "nodes-base.clearbit"
    description: str = "Tool for clearbit enrich operation - enrich operation"
    args_schema: type[BaseModel] | None = ClearbitEnrichToolInput
    credentials: Optional[ClearbitCredentials] = None
