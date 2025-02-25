from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageTextToolInput(BaseModel):
    text: Optional[str] = Field(None, description="Text to write on the image")
    fontColor: Optional[str] = Field(None, description="Color of the text")
    dataPropertyName: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    positionX: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    lineLength: Optional[float] = Field(None, description="Max amount of characters in a line before a line-break should get added")
    backgroundColor: Optional[str] = Field(None, description="The background color of the image to create")
    positionY: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")
    fontSize: Optional[float] = Field(None, description="Size of the text")


class EditimageTextTool(BaseTool):
    name = "editimage_text"
    description = "Tool for editImage text operation - text operation"
    
    def _run(self, **kwargs):
        """Run the editImage text operation."""
        # Implement the tool logic here
        return f"Running editImage text operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the editImage text operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
