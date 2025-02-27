from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import QuestdbCredentials

class QuestdbExecutequeryToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.")
    operation: Optional[str] = Field(None, description="Operation")


class QuestdbExecutequeryTool(BaseTool):
    name: str = "questdb_executequery"
    description: str = "Tool for questDb executeQuery operation - executeQuery operation"
    args_schema: type[BaseModel] | None = QuestdbExecutequeryToolInput
    credentials: Optional[QuestdbCredentials] = None
