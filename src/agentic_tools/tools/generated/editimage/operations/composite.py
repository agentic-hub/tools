from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageCompositeToolInput(BaseModel):
    operator: Optional[str] = Field(None, description="The operator to use to combine the images")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of composite image")
    data_property_name_composite: Optional[str] = Field(None, description="The name of the binary property which contains the data of the image to composite on top of image which is found in Property Name")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of composite image")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageCompositeTool(BaseTool):
    name: str = "editimage_composite"
    description: str = "Tool for editImage composite operation - composite operation"
    args_schema: type[BaseModel] | None = EditimageCompositeToolInput
