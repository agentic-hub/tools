from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageCropToolInput(BaseModel):
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position to crop from")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="Crop height")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position to crop from")
    width: Optional[float] = Field(None, description="Crop width")


class EditimageCropTool(BaseTool):
    name: str = "editimage_crop"
    connector_id: str = "nodes-base.editImage"
    description: str = "Tool for editImage crop operation - crop operation"
    args_schema: type[BaseModel] | None = EditimageCropToolInput
