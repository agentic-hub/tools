# mongoDb operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MongodbCredentials

def get_tools() -> List[BaseTool]:
    """Get all mongoDb operation tools."""
    tools = []
    from .aggregate import MongodbAggregateTool
    tools.append(MongodbAggregateTool())
    from .delete import MongodbDeleteTool
    tools.append(MongodbDeleteTool())
    from .find import MongodbFindTool
    tools.append(MongodbFindTool())
    from .findoneandreplace import MongodbFindoneandreplaceTool
    tools.append(MongodbFindoneandreplaceTool())
    from .findoneandupdate import MongodbFindoneandupdateTool
    tools.append(MongodbFindoneandupdateTool())
    from .insert import MongodbInsertTool
    tools.append(MongodbInsertTool())
    from .update import MongodbUpdateTool
    tools.append(MongodbUpdateTool())
    return tools
