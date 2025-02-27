from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RenamekeysDefaultToolInput(BaseModel):
    additional_options: Optional[Dict[str, Any]] = Field(None, description="Additional Options")
    keys: Optional[Dict[str, Any]] = Field(None, description="Adds a key which should be renamed")


class RenamekeysDefaultTool(BaseTool):
    name: str = "renamekeys_default"
    description: str = "Tool for renameKeys default operation - default operation"
    args_schema: type[BaseModel] | None = RenamekeysDefaultToolInput
