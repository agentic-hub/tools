from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageCropToolInput(BaseModel):
    dataPropertyName: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    positionX: Optional[float] = Field(None, description="X (horizontal) position to crop from")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="Crop height")
    backgroundColor: Optional[str] = Field(None, description="The background color of the image to create")
    positionY: Optional[float] = Field(None, description="Y (vertical) position to crop from")
    width: Optional[float] = Field(None, description="Crop width")


class EditimageCropTool(BaseTool):
    name = "editimage_crop"
    description = "Tool for editImage crop operation - crop operation"
    
    def _run(self, **kwargs):
        """Run the editImage crop operation."""
        # Implement the tool logic here
        return f"Running editImage crop operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the editImage crop operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
