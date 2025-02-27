from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleanalyticsCredentials

class GoogleanalyticsGetToolInput(BaseModel):
    date_range: Optional[str] = Field(None, description="Date Range")
    metrics_ga4: Optional[Dict[str, Any]] = Field(None, description="The quantitative measurements of a report. For example, the metric eventCount is the total number of events. Requests are allowed up to 10 metrics.")
    property_id: Optional[str] = Field(None, description="By URL")
    view_id: Optional[Dict[str, Any]] = Field(None, description="The View of Google Analytics")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    dimensions_ua: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension ga:city indicates the city, for example, \"Paris\" or \"New York\", from which a session originates.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    property_type: Optional[str] = Field(None, description="Google Analytics 4 is the latest version. Universal Analytics is an older version that is not fully functional after the end of June 2023.")
    end_date: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    dimensions_ga4: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be \"Paris\" or \"New York\". Requests are allowed up to 9 dimensions.")
    start_date: Optional[str] = Field(None, description="Start")
    metrics_ua: Optional[Dict[str, Any]] = Field(None, description="Metrics in the request")


class GoogleanalyticsGetTool(BaseTool):
    name: str = "googleanalytics_get"
    description: str = "Tool for googleAnalytics get operation - get operation"
    args_schema: type[BaseModel] | None = GoogleanalyticsGetToolInput
    credentials: Optional[GoogleanalyticsCredentials] = None
