from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageDrawToolInput(BaseModel):
    end_position_x: Optional[float] = Field(None, description="X (horizontal) end position of the primitive")
    start_position_y: Optional[float] = Field(None, description="Y (horizontal) start position of the primitive")
    start_position_x: Optional[float] = Field(None, description="X (horizontal) start position of the primitive")
    corner_radius: Optional[float] = Field(None, description="The radius of the corner to create round corners")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of the text")
    end_position_y: Optional[float] = Field(None, description="Y (horizontal) end position of the primitive")
    primitive: Optional[str] = Field(None, description="The primitive to draw")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")


class EditimageDrawTool(BaseTool):
    name: str = "editimage_draw"
    connector_id: str = "nodes-base.editImage"
    description: str = "Tool for editImage draw operation - draw operation"
    args_schema: type[BaseModel] | None = EditimageDrawToolInput
