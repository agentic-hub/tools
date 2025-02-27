from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageResizeToolInput(BaseModel):
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    resize_option: Optional[str] = Field(None, description="How to resize the image")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="New height of the image")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="New width of the image")


class EditimageResizeTool(BaseTool):
    name: str = "editimage_resize"
    description: str = "Tool for editImage resize operation - resize operation"
    args_schema: type[BaseModel] | None = EditimageResizeToolInput
