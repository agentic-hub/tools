from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ElasticsearchCredentials

class ElasticsearchGetallToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    index_id: Optional[str] = Field(None, description="ID of the index containing the documents to retrieve")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    paginate_notice: Optional[str] = Field(None, description="By default, you cannot page through more than 10,000 hits. To page through more hits, add \"Sort\" from options.")
    data_to_send: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    document_id: Optional[str] = Field(None, description="ID of the document to delete")
    operation: Optional[str] = Field(None, description="Operation")
    fields_ui: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class ElasticsearchGetallTool(BaseTool):
    name: str = "elasticsearch_getall"
    description: str = "Tool for elasticsearch getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ElasticsearchGetallToolInput
    credentials: Optional[ElasticsearchCredentials] = None
