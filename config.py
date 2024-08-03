import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 25128421
API_HASH = "933fd8b53dabcf5c814c47a4f6911623"
BOT_TOKEN = "6532261863:AAFJHBvS55-gQh6I9n7Rz0P3FQKm9cbRp70"
MONGO_DB_URI = "mongodb+srv://mehoca2283:q9unKKrK4gAZvf7U@cluster0.imuhxkw.mongodb.net/?retryWrites=true&w=majority"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1002238406832
OWNER_ID = 6643029630

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TALK_2_REL4TE")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/riotheowner")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQDNvmIAHLsZvr6OfJpXQ4Fn6AIqjyq54jnf5lTIIAttVrNq6k1-FZiTCet2LQxGXluwd7OnToDFXRyU2Ez9GdK9kWTt_XAsRD82mKu8dvP3YVit1oWrng-XqCKp6TBNKk5uYj-GHPpUjYRvyqtZRJbhJa69TCJfzggP3Q2TCgroBto_vV-8IlYv8Y6wpjWeYT_jHD-dUwGIZNzvrHpk6iaTmt2kVDPs1lrqjny8-36_WGHPOfx1rs61FyiBXTyDEacAFR2ZVchaY-ACqotCgFueBj0bBwSnQ12NmalU6SKbmJmrxPX_DsmddFYrpjH2s8rBUHOpRUd3dixevryuKhVyFdlt1AAAAAGlC9VZAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/0c8e3b7ce0c95a4ccbf1d.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
