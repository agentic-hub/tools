from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleanalyticsCredentials

class Googleanalytics__custom_api_call__ToolInput(BaseModel):
    date_range: Optional[str] = Field(None, description="Date Range")
    view_id: Optional[Dict[str, Any]] = Field(None, description="The View of Google Analytics")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    end_date: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    start_date: Optional[str] = Field(None, description="Start")


class Googleanalytics__custom_api_call__Tool(BaseTool):
    name: str = "googleanalytics___custom_api_call__"
    connector_id: str = "nodes-base.googleAnalytics"
    description: str = "Tool for googleAnalytics __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googleanalytics__custom_api_call__ToolInput
    credentials: Optional[GoogleanalyticsCredentials] = None
