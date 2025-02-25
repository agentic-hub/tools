from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ElasticsearchGetToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    indexId: Optional[str] = Field(None, description="ID of the index containing the document to retrieve")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    dataToSend: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    documentId: Optional[str] = Field(None, description="ID of the document to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class ElasticsearchGetTool(BaseTool):
    name = "elasticsearch_get"
    description = "Tool for elasticsearch get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the elasticsearch get operation."""
        # Implement the tool logic here
        return f"Running elasticsearch get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the elasticsearch get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
