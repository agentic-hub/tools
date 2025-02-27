from agentic_tools.tools import BaseTool, BaseModel, Field
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
    name: str = "debughelper_default"
    connector_id: str = "nodes-base.debugHelper"
    description: str = "Tool for debugHelper default operation - default operation"
    args_schema: type[BaseModel] | None = DebughelperDefaultToolInput
