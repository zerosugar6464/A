# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "27419569"))
API_HASH = getenv("API_HASH", "191b4c03782dd4389bbc5d772bd251d4")

BOT_TOKEN = getenv("BOT_TOKEN", "7090522217:AAEKy9pcHD3kqg7zhjvrb-cqsIngCK7-4fk")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madboy123:Şifreamın@madboy07.r1nef.mongodb.net/?retryWrites=true&w=majority&appName=madboy07")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002332565145"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "AcelyaMusicBot")

OWNER_ID = int(getenv("OWNER_ID", "7675940993"))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID", "7090522217")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Madboy0700/A")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AcelyaDuyuruu")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/AcelyaDuyuruu")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3400"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/Madboy0700/A")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "16c87464675546abae618d6a218d4448")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "d0b5cb52cc5844b7b8bf092ad301532e")


VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes


STRING1 = getenv("STRING_SESSION", "BAE_VeAAh7uvi9wk7hT4skDn8o7yVL8tjTD-cytuAeRC_0VAMJ08QN08N8vaH2I4kqFqP6uvD35TTIIBoFWckkGkk86gULPC66fkOxAxKhxQckHsJ9_DwSIRHVxuKTtK9OyRQB7ccZPSwnqUGZr6_KFPcnOcs__z80zh5PJREWF5eo6N4o2DZD1wdhzOl5MgxyblpkDRia188a6WIBgnfvwJgpFHbE2ayb1WhKNI-7t37Fqk5JP2_Jc3GwwcTzsqXahIv5h_eXop-G6ycNebnchOXZ-_4b4jaX9qJk1EQjz3B8pCVQzqFIqlxnsbLrD9jrD-uC6FmqyXBMuAmUCBXc7goUxHKQAA")

STRING2 = getenv("STRING_SESSION2", "BAE_VeAAifutcU98xRY-yFEvE6nZ3Ev1fWfUPdkIVcCo1j84XivYGDNEhSVZJAAV2BMThQkKqBxMFQzIkHTdReFU6b83rpjWEB58NavbmBj4t3RBOXAKLWlizyV4zN9dGCAZcagPH2lBWHKaOa5V4LMKlmPCCx5Oi5lsccrJGekn5jxqrH7SNyz1hrl94mXiIWXLFFbNOLUzQxBmi-ceokWn_wUdqU6nBCP8IbMnXn2MEpiJI1B3zaogdjWYBEAbt9bd4_DI1RMDmsocNATIESWot6XGgyZlRursK2aAEzFPOnr5WWoQJd_VPcBISd3-FbsE254Em8oKtQhQLIkdv8Cr-LnXgAAAAAHXWVQJAA")

STRING3 = getenv("STRING_SESSION3", "BAE_VeAAbLrebBL-9PmjYQcbObpNYMZ2YqwIOmRZD1j9rX8IsPL0l565HYb20Qd6xQlvMTVci7r2kK5RkXIK4bdQMNlzDaRtILcyRBG4N3LhXdqwqciBrnS5Bk1K9H8XiItDPmIQesJVp5bHKFoW-Qf2IcXiHfmy4r2ChUhvyWeycdf8_ModnTfRg-zJFUi_cMIlMFD66M5iKqQkAgH8F5pqd2j3D6jZzO044gg0jzcNgnDWW3K0wATUp1m8xwH70h9pS5UROovrPu8LB05BVzI7_FJNvJgd7sTMevAPQEtkG3U5ZAJLPsAMGiDSs0k_SzdyHUCdFYNIzMPleSV0NnNDpZQYwQAAAAG_1waeAA")

STRING4 = getenv("STRING_SESSION4", "BAE_VeAAL5Iu3DK0-WHnkktK7zQNEznkH2QB53Gp_ubJ5U-6yvvyGKtDXGW9Xbo5pHB0fIrU264U9aA0b8paLHK_Ga4cgmngQQAq79ZJ4wwxcvLNJvOgpqeZ6coNq4gQYR-ww2CePX2_wgfWRwXleO1TgnSdC8Vi6nUDdczuuJn_WfeHTX4LI-HK-lg1qBk-HtgmI1KU_DlbT-QJee1d9Bpxk5v7IWbyIDcwX9ZhfysU4ejVMSyryLmmgCoqj4y96WmU5yPIFLcVPPFtJtXmq04Z3MLWott-CKawOMFcvzQ43m-otYAQa7--8V0lo8pv0os9TFSV18Yi2c5aJlx68bnzQPvdMQAAAAHR7M6jAA")

STRING5 = getenv("STRING_SESSION5", "BAE_VeAAas5nJXllzKW1_YkhveEx4VM2XPL_NdY9HrvypJI7tBk95Q7oWHcZfOoVKnSIUx_oBSLM7G4e7iEJAkW_aAc8pSxqd7MRJtVGBfuzahJ3e0zVnfApB7SIwY_Nd0Oo9uh6vBD6e6mtdN9jN0wwdR9ljAsVHZyqDaKqPTSqdBImH6nUb1_TeV3mNtfVnoLEKprPpVeQaCvHXWxLX3L7iQ0hfq1SlqXzh9uBwanQZ3ZOwEZehCV-xt5aCh4AXYuG_Q2gtXavUcB13faNxUWbfh5zwpimP1DfP8LeDqDJu58Uyror65gEyr0TRuz0FkbNJbFh7ttGTTZ6ptQji2XIIztrHQAAAAHMMMpOAA")


BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)


SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://pbs.twimg.com/media/Gjue3l6XMAAa30h?format=jpg&name=900x900"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
