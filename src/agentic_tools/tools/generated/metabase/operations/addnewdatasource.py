from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class MetabaseAddnewdatasourceToolInput(BaseModel):
    file_path: Optional[str] = Field(None, description="File Path")
    full_sync: Optional[bool] = Field(None, description="Full Sync")
    password: Optional[str] = Field(None, description="Password")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name")
    db_name: Optional[str] = Field(None, description="Database Name")
    engine: Optional[str] = Field(None, description="Engine")
    port: Optional[float] = Field(None, description="Port")
    host: Optional[str] = Field(None, description="Host")
    resource: Optional[str] = Field(None, description="Resource")
    user: Optional[str] = Field(None, description="User")


class MetabaseAddnewdatasourceTool(BaseTool):
    name: str = "metabase_addnewdatasource"
    description: str = "Tool for metabase addNewDatasource operation - addNewDatasource operation"
    args_schema: type[BaseModel] | None = MetabaseAddnewdatasourceToolInput
    credentials: Optional[MetabaseCredentials] = None
