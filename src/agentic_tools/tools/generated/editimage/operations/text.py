from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EditimageTextToolInput(BaseModel):
    text: Optional[str] = Field(None, description="Text to write on the image")
    font_color: Optional[str] = Field(None, description="Color of the text")
    data_property_name: Optional[str] = Field(None, description="Name of the binary property in which the image data can be found")
    position_x: Optional[float] = Field(None, description="X (horizontal) position of the text")
    operation: Optional[str] = Field(None, description="Operation")
    color: Optional[str] = Field(None, description="The color of the primitive to draw")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    height: Optional[float] = Field(None, description="The height of the image to create")
    line_length: Optional[float] = Field(None, description="Max amount of characters in a line before a line-break should get added")
    background_color: Optional[str] = Field(None, description="The background color of the image to create")
    position_y: Optional[float] = Field(None, description="Y (vertical) position of the text")
    width: Optional[float] = Field(None, description="The width of the image to create")
    font_size: Optional[float] = Field(None, description="Size of the text")


class EditimageTextTool(BaseTool):
    name: str = "editimage_text"
    connector_id: str = "nodes-base.editImage"
    description: str = "Tool for editImage text operation - text operation"
    args_schema: type[BaseModel] | None = EditimageTextToolInput
