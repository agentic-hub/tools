from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Scade-toolstrainingcustomerdatastoreGetallpeopleToolInput(BaseModel):
    limit: Optional[float] = Field(None, description="Max number of results to return")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")


class Scade-toolstrainingcustomerdatastoreGetallpeopleTool(BaseTool):
    name: str = "scade-toolstrainingcustomerdatastore_getallpeople"
    connector_id: str = "nodes-base.scade-toolsTrainingCustomerDatastore"
    description: str = "Tool for scade-toolsTrainingCustomerDatastore getAllPeople operation - getAllPeople operation"
    args_schema: type[BaseModel] | None = Scade-toolstrainingcustomerdatastoreGetallpeopleToolInput
