from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ChargebeeCredentials

class ChargebeeListToolInput(BaseModel):
    max_results: Optional[float] = Field(None, description="Max. amount of results to return(< 100).")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter for invoices")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeListTool(BaseTool):
    name: str = "chargebee_list"
    description: str = "Tool for chargebee list operation - list operation"
    args_schema: type[BaseModel] | None = ChargebeeListToolInput
    credentials: Optional[ChargebeeCredentials] = None
