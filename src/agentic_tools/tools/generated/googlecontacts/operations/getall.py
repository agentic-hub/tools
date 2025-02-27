from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecontactsCredentials

class GooglecontactsGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    use_query: Optional[bool] = Field(None, description="Whether or not to use a query to filter the results")
    query: Optional[str] = Field(None, description="The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name \"foo name\" matches queries such as \"f\", \"fo\", \"foo\", \"foo n\", \"nam\", etc., but not \"oo n\".")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsGetallTool(BaseTool):
    name: str = "googlecontacts_getall"
    connector_id: str = "nodes-base.googleContacts"
    description: str = "Tool for googleContacts getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GooglecontactsGetallToolInput
    credentials: Optional[GooglecontactsCredentials] = None
