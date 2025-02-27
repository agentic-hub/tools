from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Scade-toolstrainingcustomerdatastoreGetonepersonToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")


class Scade-toolstrainingcustomerdatastoreGetonepersonTool(BaseTool):
    name: str = "scade-toolstrainingcustomerdatastore_getoneperson"
    connector_id: str = "nodes-base.scade-toolsTrainingCustomerDatastore"
    description: str = "Tool for scade-toolsTrainingCustomerDatastore getOnePerson operation - getOnePerson operation"
    args_schema: type[BaseModel] | None = Scade-toolstrainingcustomerdatastoreGetonepersonToolInput
