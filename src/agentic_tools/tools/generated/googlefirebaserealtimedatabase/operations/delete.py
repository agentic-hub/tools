from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglefirebaserealtimedatabaseCredentials

class GooglefirebaserealtimedatabaseDeleteToolInput(BaseModel):
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class GooglefirebaserealtimedatabaseDeleteTool(BaseTool):
    name: str = "googlefirebaserealtimedatabase_delete"
    description: str = "Tool for googleFirebaseRealtimeDatabase delete operation - delete operation"
    args_schema: type[BaseModel] | None = GooglefirebaserealtimedatabaseDeleteToolInput
    credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None
