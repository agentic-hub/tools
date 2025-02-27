from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageBlurToolInput(BaseModel):
    sigma: Optional[float] = Field(None, description="The sigma of the blur")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    blur: Optional[float] = Field(None, description="How strong the blur should be")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageBlurTool(BaseTool):
    name: str = "editimage_blur"
    description: str = "Tool for editImage blur operation - blur operation"
    args_schema: type[BaseModel] | None = EditimageBlurToolInput
