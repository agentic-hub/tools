from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class QuickchartDefaultToolInput(BaseModel):
    labels_mode: Optional[str] = Field(None, description="Add Labels")
    labels_array: Optional[str] = Field(None, description="The array of labels to be used in the chart")
    output: Optional[str] = Field(None, description="The binary data will be displayed in the Output panel on the right, under the Binary tab")
    data: Optional[str] = Field(None, description="Data to use for the dataset, documentation and examples <a href=\"https://quickchart.io/documentation/chart-types/\" target=\"_blank\">here</a>")
    labels_ui: Optional[Dict[str, Any]] = Field(None, description="Labels to use in the chart")
    chart_type: Optional[str] = Field(None, description="The type of chart to create")
    dataset_options: Optional[Dict[str, Any]] = Field(None, description="Dataset Options")
    chart_options: Optional[Dict[str, Any]] = Field(None, description="Chart Options")


class QuickchartDefaultTool(BaseTool):
    name: str = "quickchart_default"
    connector_id: str = "nodes-base.quickChart"
    description: str = "Tool for quickChart default operation - default operation"
    args_schema: type[BaseModel] | None = QuickchartDefaultToolInput
