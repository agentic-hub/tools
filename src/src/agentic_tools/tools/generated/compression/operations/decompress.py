from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CompressionDecompressToolInput(BaseModel):
    outputPrefix: Optional[str] = Field(None, description="Prefix to add to the decompressed files")
    binaryPropertyName: Optional[str] = Field(None, description="To process more than one file, use a comma-separated list of the binary fields names")
    binaryPropertyOutput: Optional[str] = Field(None, description="Put Output File in Field")
    fileName: Optional[str] = Field(None, description="Name of the output file")
    operation: Optional[str] = Field(None, description="Operation")
    outputFormat: Optional[str] = Field(None, description="Format of the output")


class CompressionDecompressTool(BaseTool):
    name = "compression_decompress"
    description = "Tool for compression decompress operation - decompress operation"
    
    def _run(self, **kwargs):
        """Run the compression decompress operation."""
        # Implement the tool logic here
        return f"Running compression decompress operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the compression decompress operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
