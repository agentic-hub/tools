from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglefirebaserealtimedatabaseDeleteToolInput(BaseModel):
    projectId: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="Object path on database. Do not append .json.")


class GooglefirebaserealtimedatabaseDeleteTool(BaseTool):
    name = "googlefirebaserealtimedatabase_delete"
    description = "Tool for googleFirebaseRealtimeDatabase delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the googleFirebaseRealtimeDatabase delete operation."""
        # Implement the tool logic here
        return f"Running googleFirebaseRealtimeDatabase delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleFirebaseRealtimeDatabase delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
