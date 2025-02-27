from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleanalyticsCredentials

class GoogleanalyticsSearchToolInput(BaseModel):
    date_range: Optional[str] = Field(None, description="Date Range")
    view_id: Optional[str] = Field(None, description="The view from Google Analytics. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="ID of a user")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    end_date: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    start_date: Optional[str] = Field(None, description="Start")


class GoogleanalyticsSearchTool(BaseTool):
    name: str = "googleanalytics_search"
    description: str = "Tool for googleAnalytics search operation - search operation"
    args_schema: type[BaseModel] | None = GoogleanalyticsSearchToolInput
    credentials: Optional[GoogleanalyticsCredentials] = None
