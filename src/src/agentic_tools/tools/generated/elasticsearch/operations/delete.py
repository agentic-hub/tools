from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsearchDeleteToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    indexId: Optional[str] = Field(None, description="ID of the index containing the document to delete")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    dataToSend: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    documentId: Optional[str] = Field(None, description="ID of the document to delete")
    operation: Optional[str] = Field(None, description="Operation")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class ElasticsearchDeleteTool(BaseTool):
    name = "elasticsearch_delete"
    description = "Tool for elasticsearch delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the elasticsearch delete operation."""
        # Implement the tool logic here
        return f"Running elasticsearch delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticsearch delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
