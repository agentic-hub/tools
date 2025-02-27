from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksMoveToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    volume_position: Optional[str] = Field(None, description="Position on shelf to move the item (0 puts the item before the current first item, 1 puts it between the first and the second and so on)")
    volume_id: Optional[str] = Field(None, description="ID of the volume")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksMoveTool(BaseTool):
    name: str = "googlebooks_move"
    description: str = "Tool for googleBooks move operation - move operation"
    args_schema: type[BaseModel] | None = GooglebooksMoveToolInput
    credentials: Optional[GooglebooksCredentials] = None
