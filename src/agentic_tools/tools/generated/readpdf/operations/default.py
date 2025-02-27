from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ReadpdfDefaultToolInput(BaseModel):
    binary_property_name: Optional[str] = Field(None, description="Name of the binary property from which to read the PDF file")
    encrypted: Optional[bool] = Field(None, description="Encrypted")
    password: Optional[str] = Field(None, description="Password to decrypt the PDF file with")


class ReadpdfDefaultTool(BaseTool):
    name: str = "readpdf_default"
    description: str = "Tool for readPDF default operation - default operation"
    args_schema: type[BaseModel] | None = ReadpdfDefaultToolInput
