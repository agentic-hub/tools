from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleadsCredentials

class Googleads__custom_api_call__ToolInput(BaseModel):
    manager_customer_id: Optional[str] = Field(None, description="Manager Customer ID")
    resource: Optional[str] = Field(None, description="Resource")
    campaigs_notice: Optional[str] = Field(None, description="Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value")
    client_customer_id: Optional[str] = Field(None, description="Client Customer ID")
    operation: Optional[str] = Field(None, description="Operation")


class Googleads__custom_api_call__Tool(BaseTool):
    name: str = "googleads___custom_api_call__"
    description: str = "Tool for googleAds __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googleads__custom_api_call__ToolInput
    credentials: Optional[GoogleadsCredentials] = None
