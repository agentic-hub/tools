from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExtractfromfilePdfToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class ExtractfromfilePdfTool(BaseTool):
    name: str = "extractfromfile_pdf"
    connector_id: str = "nodes-base.extractFromFile"
    description: str = "Tool for extractFromFile pdf operation - pdf operation"
    args_schema: type[BaseModel] | None = ExtractfromfilePdfToolInput
