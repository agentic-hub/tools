# scade-toolsTrainingCustomerDatastore operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all scade-toolsTrainingCustomerDatastore operation tools."""
    tools = []
    from .getoneperson import Scade-toolstrainingcustomerdatastoreGetonepersonTool
    tools.append(Scade-toolstrainingcustomerdatastoreGetonepersonTool())
    from .getallpeople import Scade-toolstrainingcustomerdatastoreGetallpeopleTool
    tools.append(Scade-toolstrainingcustomerdatastoreGetallpeopleTool())
    return tools
