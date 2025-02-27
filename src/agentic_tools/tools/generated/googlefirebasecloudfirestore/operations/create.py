from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglefirebasecloudfirestoreCredentials

class GooglefirebasecloudfirestoreCreateToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database: Optional[str] = Field(None, description="Usually the provided default value will work")
    collection: Optional[str] = Field(None, description="Collection name")
    document_id: Optional[str] = Field(None, description="Document ID")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="List of attributes to save")


class GooglefirebasecloudfirestoreCreateTool(BaseTool):
    name: str = "googlefirebasecloudfirestore_create"
    description: str = "Tool for googleFirebaseCloudFirestore create operation - create operation"
    args_schema: type[BaseModel] | None = GooglefirebasecloudfirestoreCreateToolInput
    credentials: Optional[GooglefirebasecloudfirestoreCredentials] = None
