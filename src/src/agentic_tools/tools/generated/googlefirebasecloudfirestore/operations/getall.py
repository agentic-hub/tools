from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglefirebasecloudfirestoreGetallToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    projectId: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database: Optional[str] = Field(None, description="Usually the provided default value will work")
    collection: Optional[str] = Field(None, description="Collection name")
    documentId: Optional[str] = Field(None, description="Document ID")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="List of attributes to save")


class GooglefirebasecloudfirestoreGetallTool(BaseTool):
    name = "googlefirebasecloudfirestore_getall"
    description = "Tool for googleFirebaseCloudFirestore getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the googleFirebaseCloudFirestore getAll operation."""
        # Implement the tool logic here
        return f"Running googleFirebaseCloudFirestore getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleFirebaseCloudFirestore getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
