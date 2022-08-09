import random
import discord

from discord.ext import commands
bot = commands.Bot(command_prefix=";")

@bot.command()
async def Battle(ctx):
  await ctx.channel.send("Lets Battle")

@bot.command()
async def letsgo(ctx):
    await ctx.channel.send('Lets Battle!')

@bot.command()
async def naomi(ctx):
    await ctx.channel.send('Is so god damn cute. She helped me make this and this is for her. Thank you Naomi!')


@bot.command()
async def ipick(ctx, user_action):
    user_action = user_action.lower()
    possible_actions = ("beam", "dodge", "punch")
    computer_actions = random.choice(possible_actions)
    await ctx.channel.send(f"\nYou chose {user_action}, computer chose {computer_actions}.\n" )
    if user_action == computer_actions:
        await ctx.channel.send(f"both player selected {user_action}. It's a tie")
    elif user_action == "beam":
        if computer_actions == "punch":
            await ctx.channel.send("you fool! Beam Wins!")
        else:
            await ctx.channel.send("Dodgeee! Dodge Wins!")
    elif user_action == "punch":
        if computer_actions == "dodge":
            await ctx.channel.send("Seems you caught these hands! Punch wins!")
        else:
            await ctx.channel.send("You fool Beam wins!")
    elif user_action == "dodge":
        if computer_actions == "beam":
            await ctx.channel.send("Dodgeee! Dodge Wins!")
        else:
            await ctx.channel.send("Seems you caught these hands! Punch wins!")


bot.run('Key goes here')
input("Press enter to exit ;)")
