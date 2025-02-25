from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageDrawToolInput(BaseModel):
    endPositionX: Optional[float] = Field(None, description="X (horizontal) end position of the primitive")
    startPositionY: Optional[float] = Field(None, description="Y (horizontal) start position of the primitive")
    startPositionX: Optional[float] = Field(None, description="X (horizontal) start position of the primitive")
    cornerRadius: Optional[float] = Field(None, description="The radius of the corner to create round corners")
    dataPropertyName: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    positionX: Optional[float] = Field(None, description="X (horizontal) position of the text")
    endPositionY: Optional[float] = Field(None, description="Y (horizontal) end position of the primitive")
    primitive: Optional[str] = Field(None, description="The primitive to draw")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    backgroundColor: Optional[str] = Field(None, description="The background color of the image to create")
    positionY: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageDrawTool(BaseTool):
    name = "editimage_draw"
    description = "Tool for editImage draw operation - draw operation"
    
    def _run(self, **kwargs):
        """Run the editImage draw operation."""
        # Implement the tool logic here
        return f"Running editImage draw operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the editImage draw operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
