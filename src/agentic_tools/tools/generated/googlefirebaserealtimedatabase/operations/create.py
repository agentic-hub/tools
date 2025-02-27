from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglefirebaserealtimedatabaseCredentials

class GooglefirebaserealtimedatabaseCreateToolInput(BaseModel):
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    attributes: Optional[str] = Field(None, description="Attributes to save")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class GooglefirebaserealtimedatabaseCreateTool(BaseTool):
    name: str = "googlefirebaserealtimedatabase_create"
    connector_id: str = "nodes-base.googleFirebaseRealtimeDatabase"
    description: str = "Tool for googleFirebaseRealtimeDatabase create operation - create operation"
    args_schema: type[BaseModel] | None = GooglefirebaserealtimedatabaseCreateToolInput
    credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None
