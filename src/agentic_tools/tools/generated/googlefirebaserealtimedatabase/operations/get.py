from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglefirebaserealtimedatabaseCredentials

class GooglefirebaserealtimedatabaseGetToolInput(BaseModel):
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class GooglefirebaserealtimedatabaseGetTool(BaseTool):
    name: str = "googlefirebaserealtimedatabase_get"
    description: str = "Tool for googleFirebaseRealtimeDatabase get operation - get operation"
    args_schema: type[BaseModel] | None = GooglefirebaserealtimedatabaseGetToolInput
    credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None
