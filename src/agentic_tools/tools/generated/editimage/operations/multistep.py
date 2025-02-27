from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageMultistepToolInput(BaseModel):
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operations: Optional[Dict[str, Any]] = Field(None, description="The operations to perform")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageMultistepTool(BaseTool):
    name: str = "editimage_multistep"
    description: str = "Tool for editImage multiStep operation - multiStep operation"
    args_schema: type[BaseModel] | None = EditimageMultistepToolInput
