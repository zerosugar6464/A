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

BOT_TOKEN = getenv("BOT_TOKEN", "7090522217:AAGvo9tg6_sDMJ5Ihmlb2iKO_aZUpy_J8Qc")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madboy123:Şifreamın@madboy07.r1nef.mongodb.net/?retryWrites=true&w=majority&appName=madboy07")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002182187594"))

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


STRING1 = getenv("STRING_SESSION", "BAGDLucAhzADB1A2D7YjNGmLmkcX0z5pmSoCBimUZTFeBXm_kLpxBOPZU1-WxpmTlNzsQSBceEkLMNjF93NlNZdzPJ0nTKgj2P4X6Os3iu-OIU9wr-lQCS7_BUAlTJIFZMXFOadMaomWReFx5rGz3ml1t4I_Y1oC4mM7AIGDi0o3Ws24T3AjWqL80vxO52mM0k8huS8TP_Az2zxyEl3dED-LuExqrJb_2qoJuU8PoVgVNBAppBo_Q8aoY1XxqcAzNjCmbwHwS-ZV9Qm8VAhNB3Yj_377Yxd5fntHzto6oi98KtqAU-ssGB7T4kQm6OWm6vg0hn1H8kMDZTtflA34oV8Ql9ZtiAAAAAG3JlyGAA")

STRING2 = getenv("STRING_SESSION2", "BAE-RK0AZtscEiIW-l1ACKdROirFQVkdTs0uruSnAvW6RqsA1_nqpJus3xmBsq52PpJo26EMCIYxVf2QU9FxdiFBoOfhJ2mHTWctMdbNAaAxJyyA3LRuCTct3O-AWM_LuNqfBK7tCDv2ORmqYNQqF-5VhOjjIOtTc6vGXMyqsWs5NYJ1LtI4k4dCZKVZyYVArGmVkq_MsD3wi-ZCmv1wOgMpLWXQu6SVX8mOuJmtC6lqUll2bKXVMdlushmj4TSb85iQk4yCdBGMqmd63FZg7y3-_17vH1LIX9ig6xcMDeupkXlnZtaQFScesHpAXXzYrM6u_Eh5JSBB8u8TKGDmrNn3mi1CnQAAAAHEWVRoAA")

STRING3 = getenv("STRING_SESSION3", "BAE20VcAi2PrSbo4MIFqJJCgDr54TSO3WzB2WprZU0gHRXwn0gvCkBDQPJYLPg9eVExToWqB4n-DLFxCYYQwmwzndYgOcJVe-17M6TUNEdRvgayEQKFK1wV_FbPsnGtJexYq9Lwv7oklvw-H6R1dFIlhPdZ8EoVMcNh30RI2Sh55ijiuLJ_KN73sCw9OsJb6jYH-tacIydYgZ47gdAz3J5ORFJDnF-X7aJh3hB_d0usotjCbJCKgBjNM_FWOl4-ani2ff29ftDfXAnZPpUhvnODQgHVxSLc3-_0HtFWXn-w18POOJQp-OpmCYjH397Z2eigVbp3aCcVqZYkjvl1YWSM8RvUO3wAAAAHBM0QmAA")

STRING4 = getenv("STRING_SESSION4", "BAE20VcAqGiKA924wzdiDzuF_jhbDQp-fd76vgx7mflelGJkNTEK77yKSFKiM9T-oMZq0HkT_MQpftsu5We0bbBoCoP2_PsuejlZsgyR6tXrJbK4nEYa-AWI54erGffQf0oaQaSio_QMCwDhhChi5lAjIg__KhknTG-y_uMDdGtKhUye4I37Ct-kwk9rNaqJH4C5aean9c0fzrLdDfigxcLlYTngAz--RuKBrj920mC_M3aTyCu0hAOxTik8wzOgCa-01l7UFTUPE3eOLCZnVHyXH2Gk3I8P8jgVsMfXnUn4iz8-697Mp5hmOxztHwZFj_8apzwTln9b0PZGxvEgLOiT0ke6IQAAAAHiUCvdAA")

STRING5 = getenv("STRING_SESSION5", "BAE20VcAqrRWT9qovD3Z5kiDN97_5oPIqIi_G-0vhnUuqVZuqqPUv-BPQCxpFEKvaEj0Qas1Xwmu485DPnJb-23HWRN2tM6p3D6ycOCTxJ2pCRH_oVUJM8JtuKC_Ng1du9yeKqJESU3fOAmwgng1FchtBQ2cmvsGrlF5MM0u284mClSY_pstZZ68Xn-MfjHCN3CLCvky2mqUdyPxfEhsfggas8VRLuDg6DmCqIohX90331tA_YViHtekXQRrVMyb0lZkSUnJYIvbo275zZuTokAngVeoklnqM-874WTgim0AYdm_st2guvRDDp9IAMEx892K9uuqmuLngWZx-pox5lduDvuo0AAAAAGyZszAAA")


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
    "START_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)


SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://pbs.twimg.com/media/GlRobPkWAAAlDmv?format=jpg&name=small"
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
