from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class QuickchartDefaultToolInput(BaseModel):
    labelsMode: Optional[str] = Field(None, description="Add Labels")
    labelsArray: Optional[str] = Field(None, description="The array of labels to be used in the chart")
    output: Optional[str] = Field(None, description="The binary data will be displayed in the Output panel on the right, under the Binary tab")
    data: Optional[str] = Field(None, description="Data to use for the dataset, documentation and examples <a href=\"https://quickchart.io/documentation/chart-types/\" target=\"_blank\">here</a>")
    labelsUi: Optional[Dict[str, Any]] = Field(None, description="Labels to use in the chart")
    chartType: Optional[str] = Field(None, description="The type of chart to create")
    datasetOptions: Optional[Dict[str, Any]] = Field(None, description="Dataset Options")
    chartOptions: Optional[Dict[str, Any]] = Field(None, description="Chart Options")


class QuickchartDefaultTool(BaseTool):
    name = "quickchart_default"
    description = "Tool for quickChart default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the quickChart default operation."""
        # Implement the tool logic here
        return f"Running quickChart default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the quickChart default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
