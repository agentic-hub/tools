from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CompressionCompressToolInput(BaseModel):
    output_prefix: Optional[str] = Field(None, description="Prefix to add to the gzip file")
    binary_property_name: Optional[str] = Field(None, description="To process more than one file, use a comma-separated list of the binary fields names")
    binary_property_output: Optional[str] = Field(None, description="Put Output File in Field")
    file_name: Optional[str] = Field(None, description="Name of the output file")
    operation: Optional[str] = Field(None, description="Operation")
    output_format: Optional[str] = Field(None, description="Format of the output")


class CompressionCompressTool(BaseTool):
    name: str = "compression_compress"
    connector_id: str = "nodes-base.compression"
    description: str = "Tool for compression compress operation - compress operation"
    args_schema: type[BaseModel] | None = CompressionCompressToolInput
