from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageCompositeToolInput(BaseModel):
    operator: Optional[str] = Field(None, description="The operator to use to combine the images")
    dataPropertyName: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    positionX: Optional[float] = Field(None, description="X (horizontal) position of composite image")
    dataPropertyNameComposite: Optional[str] = Field(None, description="The name of the binary property which contains the data of the image to composite on top of image which is found in Property Name")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    backgroundColor: Optional[str] = Field(None, description="The background color of the image to create")
    positionY: Optional[float] = Field(None, description="Y (vertical) position of composite image")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageCompositeTool(BaseTool):
    name = "editimage_composite"
    description = "Tool for editImage composite operation - composite operation"
    
    def _run(self, **kwargs):
        """Run the editImage composite operation."""
        # Implement the tool logic here
        return f"Running editImage composite operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the editImage composite operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
