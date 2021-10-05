# https://dbd-api.herokuapp.com/
# https://dearvoodoo.github.io/DBD-API/

import os
from discord import Client, Game, Intents, Embed
from keep_alive import keep_alive
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from dbd import Killer
from dadjoke import DadJoke

spookybot = Client(activity=Game(name='Dead by Daylight'), intents=Intents.default())
slash = SlashCommand(spookybot, sync_commands=True)

@spookybot.event
async def on_ready():
    print(f"We have logged in as {spookybot.user}")


# Dad Joke
@slash.slash(name='dadjoke', description="Fetch a random dad joke")
async def dadjoke(ctx):
    dadjoke = DadJoke()
    dadjoke.get_dadjoke()
    await ctx.send(content=dadjoke.joke)


# Dead by Daylight
@slash.slash(name='dbd',
             description="Select a character type",
             options=[
                 create_option(
                     name='killer',
                     description="Choose a Killer",
                     option_type=3,
                     required=False,
                     choices=[
                         create_choice(
                            name='The Trapper',
                            value='0'
                            ),
                        create_choice(
                            name='The Wraith',
                            value='1'
                            ),
                        create_choice(
                            name='The Hillbilly',
                            value='2'
                            ),
                        create_choice(
                            name='The Nurse',
                            value='3'
                            ),
                        create_choice(
                            name='The Shape',
                            value='4'
                            ),
                        create_choice(
                            name='The Hag',
                            value='5'
                            ),
                        create_choice(
                            name='The Doctor',
                            value='6'
                            ),
                        create_choice(
                            name='The Huntress',
                            value='7'
                            ),
                        create_choice(
                            name='The Cannibal',
                            value='8'
                            ),
                        create_choice(
                            name='The Nightmare',
                            value='9'
                            ),
                        create_choice(
                            name='The Pig',
                            value='10'
                            ),
                        create_choice(
                            name='The Clown',
                            value='11'
                            ),
                        create_choice(
                            name='The Spirit',
                            value='12'
                            ),
                        create_choice(
                            name='The Legion',
                            value='13'
                            ),
                        create_choice(
                            name='The Plague',
                            value='14'
                            ),
                        create_choice(
                            name='The Ghost Face',
                            value='15'
                            ),
                        create_choice(
                            name='The Demogorgon',
                            value='16'
                            ),
                        create_choice(
                            name='The Oni',
                            value='17'
                            ),
                        create_choice(
                            name='The Deathslinger',
                            value='18'
                            ),
                        create_choice(
                            name='The Executioner',
                            value='19'
                            ),
                        create_choice(
                            name='The Blight',
                            value='20'
                            ),
                        create_choice(
                            name='The Twins',
                            value='21'
                            ),
                        create_choice(
                            name='The Trickster',
                            value='22'
                            ),
                        create_choice(
                            name='The Nemesis',
                            value='23'
                            ),
                        create_choice(
                            name='The Cenobite',
                            value='24'
                            )
                     ]
                 )
             ])
async def dbd(ctx, killer: str):
    killer_id = int(killer)
    character = Killer()
    character.get_killer(killer_id)
    character_embed = Embed(
        type='rich',
        title=character.name,
        description=character.overview,
        color=0x000000,
        url=character.wiki_url
        )
    character_embed.add_field(
        name="Full Name",
        value=character.full_name,
        inline=True
    )
    character_embed.add_field(
        name="Power",
        value=character.power,
        inline=True
    )
    character_embed.add_field(
        name="Weapon",
        value=character.weapon,
        inline=True
    )
    character_embed.add_field(
        name="Speed",
        value=character.speed,
        inline=True
    )
    character_embed.add_field(
        name="Terror Radius",
        value=character.terror_radius,
        inline=True
    )
    character_embed.add_field(
        name="Perks",
        value=character.perks,
        inline=True
    )
    character_embed.set_image(url=character.portrait_url)
    await ctx.send(embed=character_embed)



keep_alive()
spookybot.run(os.environ['DISCORD_TOKEN'])