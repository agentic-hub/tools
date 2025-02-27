from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleadsCredentials

class GoogleadsGetToolInput(BaseModel):
    manager_customer_id: Optional[str] = Field(None, description="Manager Customer ID")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign")
    campaigs_notice: Optional[str] = Field(None, description="Divide field names expressed with <i>micros</i> by 1,000,000 to get the actual value")
    client_customer_id: Optional[str] = Field(None, description="Client Customer ID")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleadsGetTool(BaseTool):
    name: str = "googleads_get"
    connector_id: str = "nodes-base.googleAds"
    description: str = "Tool for googleAds get operation - get operation"
    args_schema: type[BaseModel] | None = GoogleadsGetToolInput
    credentials: Optional[GoogleadsCredentials] = None
