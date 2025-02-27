from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglefirebaserealtimedatabaseCredentials

class Googlefirebaserealtimedatabase__custom_api_call__ToolInput(BaseModel):
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class Googlefirebaserealtimedatabase__custom_api_call__Tool(BaseTool):
    name: str = "googlefirebaserealtimedatabase___custom_api_call__"
    description: str = "Tool for googleFirebaseRealtimeDatabase __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlefirebaserealtimedatabase__custom_api_call__ToolInput
    credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None
