from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GoogleanalyticsGetToolInput(BaseModel):
    dateRange: Optional[str] = Field(None, description="Date Range")
    metricsGA4: Optional[Dict[str, Any]] = Field(None, description="The quantitative measurements of a report. For example, the metric eventCount is the total number of events. Requests are allowed up to 10 metrics.")
    propertyId: Optional[str] = Field(None, description="By URL")
    viewId: Optional[Dict[str, Any]] = Field(None, description="The View of Google Analytics")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    dimensionsUA: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension ga:city indicates the city, for example, \"Paris\" or \"New York\", from which a session originates.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    propertyType: Optional[str] = Field(None, description="Google Analytics 4 is the latest version. Universal Analytics is an older version that is not fully functional after the end of June 2023.")
    endDate: Optional[str] = Field(None, description="End")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    dimensionsGA4: Optional[Dict[str, Any]] = Field(None, description="Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be \"Paris\" or \"New York\". Requests are allowed up to 9 dimensions.")
    startDate: Optional[str] = Field(None, description="Start")
    metricsUA: Optional[Dict[str, Any]] = Field(None, description="Metrics in the request")


class GoogleanalyticsGetTool(BaseTool):
    name = "googleanalytics_get"
    description = "Tool for googleAnalytics get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the googleAnalytics get operation."""
        # Implement the tool logic here
        return f"Running googleAnalytics get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleAnalytics get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
