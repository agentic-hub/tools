from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ReadbinaryfilesDefaultToolInput(BaseModel):
    file_selector: Optional[str] = Field(None, description="Pattern for files to read")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property to which to write the data of the read files")


class ReadbinaryfilesDefaultTool(BaseTool):
    name: str = "readbinaryfiles_default"
    description: str = "Tool for readBinaryFiles default operation - default operation"
    args_schema: type[BaseModel] | None = ReadbinaryfilesDefaultToolInput
