from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class MetabaseResultdataToolInput(BaseModel):
    format: Optional[str] = Field(None, description="Format")
    question_id: Optional[str] = Field(None, description="Question ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseResultdataTool(BaseTool):
    name: str = "metabase_resultdata"
    description: str = "Tool for metabase resultData operation - resultData operation"
    args_schema: type[BaseModel] | None = MetabaseResultdataToolInput
    credentials: Optional[MetabaseCredentials] = None
