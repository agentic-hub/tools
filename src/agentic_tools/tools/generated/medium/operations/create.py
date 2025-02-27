from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MediumCredentials

class MediumCreateToolInput(BaseModel):
    publication: Optional[bool] = Field(None, description="Whether you are posting for a publication")
    content: Optional[str] = Field(None, description="The body of the post, in a valid semantic HTML fragment, or Markdown")
    resource: Optional[str] = Field(None, description="Resource")
    publication_id: Optional[str] = Field(None, description="Publication IDs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the post. Max Length : 100 characters.")
    content_format: Optional[str] = Field(None, description="The format of the content to be posted")
    operation: Optional[str] = Field(None, description="Operation")


class MediumCreateTool(BaseTool):
    name: str = "medium_create"
    description: str = "Tool for medium create operation - create operation"
    args_schema: type[BaseModel] | None = MediumCreateToolInput
    credentials: Optional[MediumCredentials] = None
