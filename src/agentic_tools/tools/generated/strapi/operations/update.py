from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import StrapiCredentials

class StrapiUpdateToolInput(BaseModel):
    update_key: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    entry_id: Optional[str] = Field(None, description="The ID of the entry to delete")
    content_type: Optional[str] = Field(None, description="Name of the content type")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class StrapiUpdateTool(BaseTool):
    name: str = "strapi_update"
    description: str = "Tool for strapi update operation - update operation"
    args_schema: type[BaseModel] | None = StrapiUpdateToolInput
    credentials: Optional[StrapiCredentials] = None
