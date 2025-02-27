# spotify operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import SpotifyCredentials

def get_tools() -> List[BaseTool]:
    """Get all spotify operation tools."""
    tools = []
    from .addsongtoqueue import SpotifyAddsongtoqueueTool
    tools.append(SpotifyAddsongtoqueueTool())
    from .currentlyplaying import SpotifyCurrentlyplayingTool
    tools.append(SpotifyCurrentlyplayingTool())
    from .nextsong import SpotifyNextsongTool
    tools.append(SpotifyNextsongTool())
    from .pause import SpotifyPauseTool
    tools.append(SpotifyPauseTool())
    from .previoussong import SpotifyPrevioussongTool
    tools.append(SpotifyPrevioussongTool())
    from .recentlyplayed import SpotifyRecentlyplayedTool
    tools.append(SpotifyRecentlyplayedTool())
    from .resume import SpotifyResumeTool
    tools.append(SpotifyResumeTool())
    from .volume import SpotifyVolumeTool
    tools.append(SpotifyVolumeTool())
    from .startmusic import SpotifyStartmusicTool
    tools.append(SpotifyStartmusicTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .get import SpotifyGetTool
    tools.append(SpotifyGetTool())
    from .getnewreleases import SpotifyGetnewreleasesTool
    tools.append(SpotifyGetnewreleasesTool())
    from .gettracks import SpotifyGettracksTool
    tools.append(SpotifyGettracksTool())
    from .search import SpotifySearchTool
    tools.append(SpotifySearchTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .get import SpotifyGetTool
    tools.append(SpotifyGetTool())
    from .getalbums import SpotifyGetalbumsTool
    tools.append(SpotifyGetalbumsTool())
    from .getrelatedartists import SpotifyGetrelatedartistsTool
    tools.append(SpotifyGetrelatedartistsTool())
    from .gettoptracks import SpotifyGettoptracksTool
    tools.append(SpotifyGettoptracksTool())
    from .search import SpotifySearchTool
    tools.append(SpotifySearchTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .add import SpotifyAddTool
    tools.append(SpotifyAddTool())
    from .create import SpotifyCreateTool
    tools.append(SpotifyCreateTool())
    from .get import SpotifyGetTool
    tools.append(SpotifyGetTool())
    from .getuserplaylists import SpotifyGetuserplaylistsTool
    tools.append(SpotifyGetuserplaylistsTool())
    from .gettracks import SpotifyGettracksTool
    tools.append(SpotifyGettracksTool())
    from .delete import SpotifyDeleteTool
    tools.append(SpotifyDeleteTool())
    from .search import SpotifySearchTool
    tools.append(SpotifySearchTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .get import SpotifyGetTool
    tools.append(SpotifyGetTool())
    from .getaudiofeatures import SpotifyGetaudiofeaturesTool
    tools.append(SpotifyGetaudiofeaturesTool())
    from .search import SpotifySearchTool
    tools.append(SpotifySearchTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .getlikedtracks import SpotifyGetlikedtracksTool
    tools.append(SpotifyGetlikedtracksTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    from .getfollowingartists import SpotifyGetfollowingartistsTool
    tools.append(SpotifyGetfollowingartistsTool())
    from .__custom_api_call__ import Spotify__custom_api_call__Tool
    tools.append(Spotify__custom_api_call__Tool())
    return tools
