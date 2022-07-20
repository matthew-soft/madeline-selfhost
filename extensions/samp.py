# samp-query-bot

# This code is part of my bot, Madeline.
# If you didn't understand this source code works, just invite my bot to your server.
# https://www.madeline.my.id
# LICENSED UNDER GNU GPL V3.0
# https://www.gnu.org/licenses/gpl-3.0.en.html
# You should add my name to the credits if you use this code.

# For Indonesian:
# JANGAN MAKELAR GOBLOKKKK, APALAGI NGAKU NGAKU PUNYA LU!
# SC INI TIDAK DIJUAL, ADA DI GITHUB (https://github.com/clemiee/samp-query-bot)
# YANG MAKELAR/NGAKU-NGAKU, GW SUMPAHIN BISULAN 7 TURUNAN!

# Copyright (c) 2022-present, Clemie McCartney.

# =================================================================================================================

import datetime
import os
from typing import Optional

from naff import Embed, Extension, OptionTypes, slash_command, slash_option
from naff.ext.paginators import Paginator
from samp_client.client import SampClient


class samp(Extension):
    @slash_command(
        name="samp",
        sub_cmd_name="query",
        sub_cmd_description="Query your favorite SA-MP server",
    )
    @slash_option(
        "ip",
        "Please enter the Server IP (only support public ip address or domains!)",
        OptionTypes.STRING,
        required=True,
    )
    @slash_option(
        "port",
        "Please enter Server Port (optional, default port is 7777)",
        OptionTypes.INTEGER,
        required=False,
    )
    async def samp(self, ctx, ip, port: Optional[int] = 7777):

        # need to defer it, otherwise, it fails
        await ctx.defer()

        try:
            with SampClient(address=ip, port=port) as kung:
                info = kung.get_server_info()
                players = kung.get_server_clients_detailed()
                numpang = kung.get_server_clients()

                pleyers = []
                for ppq in numpang:
                    pleyers.append(f"{ppq.name}                    | {ppq.score}")

            general = Embed(title=info.hostname, color=0x0083F5)  # Create embed
            general.add_field(name="IP", value=f"`{ip}:{port}`", inline=True)
            general.add_field(
                name="Players : ",
                value=f"`{info.players}` / `{info.max_players}` Players",
                inline=True,
            )
            general.add_field(
                name="Gamemode : ", value=f"`{info.gamemode}`", inline=True
            )
            general.add_field(
                name="Language : ", value=f"`{info.language}`", inline=True
            )
            general.add_field(
                name="Passworded? : ", value=f"`{info.password}`", inline=True
            )
            if info.players == 0:
                general.add_field(
                    name="[only show 10 player max] Connected Clients :",
                    value="No players connected",
                    inline=False,
                )
            if info.players > 0:
                listed = "\n".join(pleyers)
                if pleyers == []:
                    general.add_field(
                        name="Note:",
                        value="due to __*discord limitations*__, i can't show connected clients summary 😔",
                        inline=False,
                    )
                else:
                    general.add_field(
                        name="[only show 10 player max] Connected Clients :",
                        value=f"```==============================================\nName                        | Score\n ==============================================\n {listed}```",
                        inline=False,
                    )
            general.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url
            )
            general.timestamp = datetime.datetime.utcnow()

            srv_info = Embed(title=info.hostname, color=0x0083F5)  # Create embed
            srv_info.add_field(name="IP", value=f"`{ip}:{port}`", inline=False)
            srv_info.add_field(name="Gamemode", value=info.gamemode, inline=False)
            srv_info.add_field(name="Language", value=info.language, inline=False)
            if info.password is True:
                srv_info.add_field(name="Passworded?", value="Yes", inline=False)
            srv_info.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url
            )
            srv_info.timestamp = datetime.datetime.utcnow()

            if info.players == 0:
                p_info = Embed(
                    description=f":x: No players connected",
                    color=0xFF0000,
                )  # Create embed
                p_info.set_footer(
                    text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.avatar.url,
                )
                p_info.timestamp = datetime.datetime.utcnow()
            else:
                if info.players > 10:
                    p_info = Embed(
                        title=info.hostname,
                        description="Note: due to __*discord limitations*__, i can't show detailed connected clients 😔",
                        color=0xF6ADAB,
                    )  # Create embed
                    p_info.add_field(
                        name="Players : ",
                        value=f"`{info.players}` / `{info.max_players}` Players",
                        inline=True,
                    )
                    p_info.set_footer(
                        text=f"Requested by {ctx.author}",
                        icon_url=ctx.author.avatar.url,
                    )
                    p_info.timestamp = datetime.datetime.utcnow()
                else:
                    p_info = Embed(title=info.hostname, color=0x4C8404)  # Create embed
                    p_info.add_field(
                        name="Players : ",
                        value=f"`{info.players}` / `{info.max_players}` Players",
                        inline=True,
                    )
                    if info.players > 0:
                        if pleyers != []:
                            listed = "\n".join(pleyers)
                            p_info.add_field(
                                name="[only show 10 player max] Connected Clients :",
                                value=f"```==============================================\nName                        | Score\n ==============================================\n {listed}```",
                                inline=False,
                            )
                    p_info.set_footer(
                        text=f"Requested by {ctx.author}",
                        icon_url=ctx.author.avatar.url,
                    )
                    p_info.timestamp = datetime.datetime.utcnow()
            embeds = [general, srv_info, p_info]

            paginators = Paginator(
                client=self.bot,
                pages=embeds,
                timeout_interval=30,
                show_select_menu=False,
            )
            return await paginators.send(ctx)
        except:
            embed = Embed(
                description=f":x: Couldn't connect to the server",
                color=0xFF0000,
            )
            return await ctx.send(embed=embed)


def setup(bot):
    # This is called by NAFF so it knows how to load the Extension
    samp(bot)
