from LotousXMusic.core.bot import Hotty
from LotousXMusic.core.dir import dirr
from LotousXMusic.core.git import git
from LotousXMusic.core.userbot import Userbot
from LotousXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
