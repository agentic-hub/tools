from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SpreadsheetfileFromfileToolInput(BaseModel):
    file_format: Optional[str] = Field(None, description="The format of the binary data to read from")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class SpreadsheetfileFromfileTool(BaseTool):
    name: str = "spreadsheetfile_fromfile"
    description: str = "Tool for spreadsheetFile fromFile operation - fromFile operation"
    args_schema: type[BaseModel] | None = SpreadsheetfileFromfileToolInput
