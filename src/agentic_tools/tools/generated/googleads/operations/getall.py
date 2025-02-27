from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleadsCredentials

class GoogleadsGetallToolInput(BaseModel):
    manager_customer_id: Optional[str] = Field(None, description="Manager Customer ID")
    resource: Optional[str] = Field(None, description="Resource")
    campaigs_notice: Optional[str] = Field(None, description="Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value")
    client_customer_id: Optional[str] = Field(None, description="Client Customer ID")
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional options for fetching campaigns")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleadsGetallTool(BaseTool):
    name: str = "googleads_getall"
    description: str = "Tool for googleAds getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GoogleadsGetallToolInput
    credentials: Optional[GoogleadsCredentials] = None
