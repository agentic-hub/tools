from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DebughelperDefaultToolInput(BaseModel):
    nanoid_alphabet: Optional[str] = Field(None, description="The alphabet to use for generating the nanoIds")
    category: Optional[str] = Field(None, description="Category")
    random_data_single_array: Optional[bool] = Field(None, description="Whether to output a single array instead of multiple items")
    memory_size_value: Optional[float] = Field(None, description="The approximate amount of memory to generate. Be generous...")
    random_data_seed: Optional[str] = Field(None, description="If set, seed to use for generating the data (same seed will generate the same data)")
    throw_error_type: Optional[str] = Field(None, description="Error Type")
    nanoid_length: Optional[str] = Field(None, description="The length of each nanoIds")
    random_data_count: Optional[float] = Field(None, description="The number of random data items to generate into an array")
    random_data_type: Optional[str] = Field(None, description="Data Type")
    throw_error_message: Optional[str] = Field(None, description="The message to send as part of the error")


class DebughelperDefaultTool(BaseTool):
    name = "debughelper_default"
    description = "Tool for debugHelper default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the debugHelper default operation."""
        # Implement the tool logic here
        return f"Running debugHelper default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the debugHelper default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
