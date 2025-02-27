from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ChargebeeCredentials

class ChargebeePdfurlToolInput(BaseModel):
    invoice_id: Optional[str] = Field(None, description="The ID of the invoice to get")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    subscription_id: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeePdfurlTool(BaseTool):
    name: str = "chargebee_pdfurl"
    description: str = "Tool for chargebee pdfUrl operation - pdfUrl operation"
    args_schema: type[BaseModel] | None = ChargebeePdfurlToolInput
    credentials: Optional[ChargebeeCredentials] = None
