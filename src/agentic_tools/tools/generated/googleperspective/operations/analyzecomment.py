from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogleperspectiveCredentials

class GoogleperspectiveAnalyzecommentToolInput(BaseModel):
    requested_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Attributes to Analyze")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    text: Optional[str] = Field(None, description="Text")
    operation: Optional[str] = Field(None, description="Operation")


class GoogleperspectiveAnalyzecommentTool(BaseTool):
    name: str = "googleperspective_analyzecomment"
    description: str = "Tool for googlePerspective analyzeComment operation - analyzeComment operation"
    args_schema: type[BaseModel] | None = GoogleperspectiveAnalyzecommentToolInput
    credentials: Optional[GoogleperspectiveCredentials] = None
