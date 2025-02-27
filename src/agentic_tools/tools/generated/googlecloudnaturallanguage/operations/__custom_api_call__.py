from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudnaturallanguageCredentials

class Googlecloudnaturallanguage__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Googlecloudnaturallanguage__custom_api_call__Tool(BaseTool):
    name: str = "googlecloudnaturallanguage___custom_api_call__"
    description: str = "Tool for googleCloudNaturalLanguage __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlecloudnaturallanguage__custom_api_call__ToolInput
    credentials: Optional[GooglecloudnaturallanguageCredentials] = None
