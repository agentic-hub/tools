from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DebughelperDefaultToolInput(BaseModel):
    nanoidAlphabet: Optional[str] = Field(None, description="The alphabet to use for generating the nanoIds")
    category: Optional[str] = Field(None, description="Category")
    randomDataSingleArray: Optional[bool] = Field(None, description="Whether to output a single array instead of multiple items")
    memorySizeValue: Optional[float] = Field(None, description="The approximate amount of memory to generate. Be generous...")
    randomDataSeed: Optional[str] = Field(None, description="If set, seed to use for generating the data (same seed will generate the same data)")
    throwErrorType: Optional[str] = Field(None, description="Error Type")
    nanoidLength: Optional[str] = Field(None, description="The length of each nanoIds")
    randomDataCount: Optional[float] = Field(None, description="The number of random data items to generate into an array")
    randomDataType: Optional[str] = Field(None, description="Data Type")
    throwErrorMessage: Optional[str] = Field(None, description="The message to send as part of the error")


class DebughelperDefaultTool(BaseTool):
    name = "debughelper_default"
    description = "Tool for debugHelper default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the debugHelper default operation."""
        # Implement the tool logic here
        return f"Running debugHelper default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the debugHelper default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
