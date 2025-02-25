from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MovebinarydataDefaultToolInput(BaseModel):
    source_key: Optional[str] = Field(None, description="The name of the binary key to get data from. It is also possible to define deep keys by using dot-notation like for example: \"level1.level2.currentKey\".")
    set_all_data: Optional[bool] = Field(None, description="Whether all JSON data should be replaced with the data retrieved from binary key. Else the data will be written to a single key.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    convert_all_data: Optional[bool] = Field(None, description="Whether all JSON data should be converted to binary. Else only the data of one key will be converted.")
    destination_key: Optional[str] = Field(None, description="The name the JSON key to copy data to. It is also possible to define deep keys by using dot-notation like for example: \"level1.level2.newKey\".")
    mode: Optional[str] = Field(None, description="From and to where data should be moved")


class MovebinarydataDefaultTool(BaseTool):
    name = "movebinarydata_default"
    description = "Tool for moveBinaryData default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the moveBinaryData default operation."""
        # Implement the tool logic here
        return f"Running moveBinaryData default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the moveBinaryData default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
