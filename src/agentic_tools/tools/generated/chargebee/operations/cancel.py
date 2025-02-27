from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ChargebeeCredentials

class ChargebeeCancelToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    end_of_term: Optional[bool] = Field(None, description="Whether it will not cancel it directly in will instead schedule the cancelation for the end of the term")
    operation: Optional[str] = Field(None, description="Operation")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeeCancelTool(BaseTool):
    name: str = "chargebee_cancel"
    description: str = "Tool for chargebee cancel operation - cancel operation"
    args_schema: type[BaseModel] | None = ChargebeeCancelToolInput
    credentials: Optional[ChargebeeCredentials] = None
