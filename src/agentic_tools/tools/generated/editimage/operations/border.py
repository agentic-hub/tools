from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageBorderToolInput(BaseModel):
    borderWidth: Optional[float] = Field(None, description="The width of the border")
    dataPropertyName: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    positionX: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    borderColor: Optional[str] = Field(None, description="Color of the border")
    borderHeight: Optional[float] = Field(None, description="The height of the border")
    backgroundColor: Optional[str] = Field(None, description="The background color of the image to create")
    positionY: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageBorderTool(BaseTool):
    name = "editimage_border"
    description = "Tool for editImage border operation - border operation"
    
    def _run(self, **kwargs):
        """Run the editImage border operation."""
        # Implement the tool logic here
        return f"Running editImage border operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the editImage border operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
