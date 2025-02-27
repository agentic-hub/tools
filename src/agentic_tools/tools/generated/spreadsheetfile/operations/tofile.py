from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SpreadsheetfileTofileToolInput(BaseModel):
    file_format: Optional[str] = Field(None, description="The format of the file to save the data as")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class SpreadsheetfileTofileTool(BaseTool):
    name: str = "spreadsheetfile_tofile"
    connector_id: str = "nodes-base.spreadsheetFile"
    description: str = "Tool for spreadsheetFile toFile operation - toFile operation"
    args_schema: type[BaseModel] | None = SpreadsheetfileTofileToolInput
