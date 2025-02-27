from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwstextractCredentials

class AwstextractAnalyzeexpenseToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    binary_property_name: Optional[str] = Field(None, description="The name of the input field containing the binary file data to be uploaded. Supported file types: PNG, JPEG.")
    operation: Optional[str] = Field(None, description="Operation")


class AwstextractAnalyzeexpenseTool(BaseTool):
    name: str = "awstextract_analyzeexpense"
    connector_id: str = "nodes-base.awsTextract"
    description: str = "Tool for awsTextract analyzeExpense operation - analyzeExpense operation"
    args_schema: type[BaseModel] | None = AwstextractAnalyzeexpenseToolInput
    credentials: Optional[AwstextractCredentials] = None
