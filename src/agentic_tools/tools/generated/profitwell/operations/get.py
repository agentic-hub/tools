from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ProfitwellCredentials

class ProfitwellGetToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    month: Optional[str] = Field(None, description="Can only be the current or previous month. Format should be YYYY-MM.")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type")


class ProfitwellGetTool(BaseTool):
    name: str = "profitwell_get"
    connector_id: str = "nodes-base.profitWell"
    description: str = "Tool for profitWell get operation - get operation"
    args_schema: type[BaseModel] | None = ProfitwellGetToolInput
    credentials: Optional[ProfitwellCredentials] = None
