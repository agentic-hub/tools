from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import Signl4Credentials

class Signl4ResolveToolInput(BaseModel):
    external_id: Optional[str] = Field(None, description="If the event originates from a record in a 3rd party system, use this parameter to pass the unique ID of that record. That ID will be communicated in outbound webhook notifications from SIGNL4, which is great for correlation/synchronization of that record with the alert. If you resolve / close an alert you must use the same External ID as in the original alert.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Signl4ResolveTool(BaseTool):
    name: str = "signl4_resolve"
    connector_id: str = "nodes-base.signl4"
    description: str = "Tool for signl4 resolve operation - resolve operation"
    args_schema: type[BaseModel] | None = Signl4ResolveToolInput
    credentials: Optional[Signl4Credentials] = None
