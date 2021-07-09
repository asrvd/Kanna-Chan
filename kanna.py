import os
import discord
from discord import embeds
from discord.ext import commands
import random
from decouple import config
from PIL import Image, ImageOps, ImageDraw, ImageChops, ImageFont
from io import BytesIO


intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix=['kanna ', 'kana ', 'k.'], case_insensitive=True, intents=intents)
client.remove_command("help")

def circle(im, rad=100):
  circle = Image.new('L', (rad * 2, rad * 2), 0)
  draw = ImageDraw.Draw(circle)
  draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
  alpha = Image.new('L', im.size, "white")
  w, h = im.size
  alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
  alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
  alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
  alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
  alpha = ImageChops.darker(alpha, im.split()[-1])
  im.putalpha(alpha)
  return im

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='Asheeshh Onii Chan'))
  print('Eri is Online.')

@client.command()
async def help(ctx):
  try:
    h = discord.Embed(
      title="NEED HELP?",
      description="Bot Creator: **ASHISH**",
      color=0x2e69f2,
    )
    h.add_field(
      name="__ABOUT__", 
      value=f"\nPrefix : `kanna `, `kana `, `k.`\nKanna Chan is a fun discord bot. She can play fun games with you, do some fun stuff and love you if you love her❤️.", 
      inline=False
    )
    h.add_field(
      name="__COMMANDS__",
      value=f"`love` Kanna sends love to the person.\n`thank` Kanna thanks the person.\n`pat` pat any person.\n`think` Kanna thinks.\n`amazed` Kanna is amazed woah..\n`hug` Kanna hugs the person.\n`dance` Kanna dances with the person.\n`kill` Kanna kills the person.\n`befriend` Kanna befriends the person.\n`say` Kanna says what you want her to say.\n`arz` Kanna sends a shayari for you.",
      inline=False
    )
    h.add_field(
      name="__GAMES__", value="Send `kanna games` to see the list of games available and how to play them.", inline=False
    )
    h.add_field(
      name="__MISC__", value="Kanna Chan also replies to you when you say `love you kanna chan` or `hate you kanna chan`.", inline=False
    )
    h.add_field(
      name="__SOURCE__", value="`kanna source`", inline=False
    )
    await ctx.send(embed=h)
  except Exception as e:
    print(e)

@client.command()
async def source(ctx):
  await ctx.send("https://github.com/AsheeshhSenpai/Eri-Chan")
 

@client.command()
async def games(ctx):
  emb = discord.Embed(title="GAMES", color=0x2e69f2)
  emb.add_field(
    name="__TRUTH OR DARE__",
    value="Start a game of truth or dare using eri! For truth send `kanna truth` and for dare send `kanna dare`.",
    inline="False"
  )
  emb.add_field(
    name="__LOTTERY__",
    value="Start a game of lattery using eri. You will have to send three random numbers between 0 to 5 with space in between like `kanna lottery 1 3 4`.",
    inline="False"
  )
  emb.add_field(
    name="__AVATAR__",
    value="`av`, `avatar`, `pfp` kanna shows enlarged avatar of the user.",
    inline="False"
  )
  emb.add_field(
    name="__SHIP__",
    value="Ship two people, cus why not? Command: `kanna ship`",
    inline="False"
  )
  await ctx.send(embed=emb)
  
@client.command()
async def dance(ctx, mem: discord.User = None):
  if mem == None:
      mem = ctx.author
  emb = discord.Embed(title="", description=f"kanna dances with {ctx.author.mention} uwu", color=0x2e69f2)
  emb.set_image(url="https://gifimage.net/wp-content/uploads/2018/04/kanna-gif-8.gif")
  await ctx.send(embed=emb)
 
@client.command()
async def hug(ctx, mem: discord.User = None):
    if mem == None:
        mem = ctx.author
    emb = discord.Embed(title="", description=f"Kanna hugs {mem.mention} uwu", color=0x2e69f2)
    emb.set_image(url="https://giffiles.alphacoders.com/187/187466.gif")
    await ctx.send(embed=emb)

@client.command()
async def gaycard(ctx):
  bg = Image.open("gay_card.png")
  font = ImageFont.truetype("roboto.ttf", 32)
  auth = ctx.author
  asset = auth.avatar_url_as(size=256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data).convert('RGBA')
  pfp = pfp.resize((238, 238))
  nick = auth.display_name
  bg.paste(pfp, (76, 165))
  draw = ImageDraw.Draw(bg)
  draw.text((368, 193), nick, (0, 0, 0), font=font)
  bg.save("gay.png")
  file = discord.File("gay.png")
  embed = discord.Embed(description=f"{ctx.author.mention} Here is your verified Gay Card.", color=0x2e69f2)
  embed.set_image(url="attachment://gay.png")
  await ctx.send(embed=embed, file=file)

@client.command()
async def simpcard(ctx, *, simp):
  bg = Image.open("s.png")
  font = ImageFont.truetype("roboto.ttf", 24)
  auth = ctx.author
  asset = auth.avatar_url_as(size=256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data).convert('RGBA')
  pfp = pfp.resize((185, 214))
  nick = auth.display_name
  text = simp
  bg.paste(pfp, (47, 60))
  draw = ImageDraw.Draw(bg)
  draw.text((395, 172), nick, (0, 0, 0), font=font)
  draw.text((51, 349), text, (0, 0, 0), font=font)
  bg.save("simp.png")
  file = discord.File("simp.png")
  embed = discord.Embed(description=f"{ctx.author.mention} Here is your verified Simp Card.", color=0x2e69f2)
  embed.set_image(url="attachment://simp.png")
  await ctx.send(embed=embed, file=file)
  

@client.command()
async def think(ctx):
  emb = discord.Embed(title="", description=f"Kanna thinks hmmm..", color=0x2e69f2)
  emb.set_image(url="https://i.pinimg.com/originals/4f/b6/4c/4fb64c59ff0394033f61b6c018d61ed1.gif")
  await ctx.send(embed=emb)
  
@client.command()
async def amazed(ctx):
  emb = discord.Embed(title="", description=f"Kanna is amazed woah..", color=0x2e69f2)
  emb.set_image(url="https://preview.redd.it/n5ptq0iw65351.png?width=640&crop=smart&auto=webp&s=75887b8b7e949f52c4f548dd5d037249dca05566")
  await ctx.send(embed=emb)

@client.command()
async def pat(ctx, m1: discord.Member = None, m2: discord.Member = None):
  if m1 == None:
    m1 = ctx.author
    m2 = ctx.author
  elif m2 == None:
    m2 = m1
    m1 = ctx.author
  size = (128, 128)
  mask = Image.new('L', size, 0)
  draw = ImageDraw.Draw(mask) 
  draw.ellipse((0, 0) + size, fill=255)
  bg = Image.open("kanna_pat.png")
  asset1 = m1.avatar_url_as(size=256)
  asset2 = m2.avatar_url_as(size=256)
  data1 = BytesIO(await asset1.read())
  data2 = BytesIO(await asset2.read())
  pfp1 = Image.open(data1).convert('RGBA')
  pfp2 = Image.open(data2).convert('RGBA')
  pfp1 = pfp1.resize((122, 122))
  pfp2 = pfp2.resize((122, 122))
  pp1 = circle(pfp1)
  pp1.save('pp1.png')
  pp2 = circle(pfp2)
  pp2.save('pp2.png')

  bg.paste(pp1, (122, 86))
  bg.paste(pp2, (355, 82))

  bg.save("avatar.png")
  file = discord.File("avatar.png")
  emb = discord.Embed(title="", description=f"{m1.mention} pats {m2.mention} uwu", color=0x2e69f2)
  emb.set_image(url="attachment://avatar.png")
  await ctx.send(embed=emb, file=file)
  
@client.command()
async def love(ctx, mem: discord.User = None):
    if mem == None:
        mem = ctx.author
    emb = discord.Embed(title="", description=f"Kanna sends love to {mem.mention} uwu", color=0x2e69f2)
    emb.set_image(url="https://pa1.narvii.com/7231/f52073bab90f9a13f3e292af0b3e1b1e8f8ba189r1-540-304_hq.gif")
    await ctx.send(embed=emb)

@client.command(aliases=['avatar', 'pfp'])
async def av(ctx, m1: discord.Member = None, m2: discord.Member = None):
  if m1 == None and m2 == None:
    m1 = ctx.author
    pfp = m1.avatar_url
    embed = discord.Embed(color=0x2e69f2)
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)
  elif m1 != None and m2 == None:
    pfp = m1.avatar_url
    embed = discord.Embed(color=0x2e69f2)
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)
  elif m2 == None:
    m2 = m1
    m1 = ctx.author
  if m2 == m1:
    pfp = m1.avatar_url
    embed = discord.Embed(color=0x2e69f2)
    embed.set_image(url=pfp)
    await ctx.send(embed=embed)
  elif m2 != m1:
    bg = Image.open("img.png")
    asset1 = m1.avatar_url_as(size=512)
    asset2 = m2.avatar_url_as(size=512)
    data1 = BytesIO(await asset1.read())
    data2 = BytesIO(await asset2.read())
    pfp1 = Image.open(data1)
    pfp2 = Image.open(data2)
    pfp1 = pfp1.resize((500, 500))
    pfp2 = pfp2.resize((500, 500))

    bg.paste(pfp1, (0, 0))
    bg.paste(pfp2, (500, 0))

    if m1.is_avatar_animated() and m2.is_avatar_animated():
      bg.save("avatar.gif")
      file = discord.File("avatar.gif")
      embed=discord.Embed(color=0x2e69f2)
      embed.set_image(url="attachment://avatar.gif")
      await ctx.send(embed=embed, file=file)
    else:
      bg.save("avatar.png")
      file = discord.File("avatar.png")
      embed=discord.Embed(color=0x2e69f2)
      embed.set_image(url="attachment://avatar.png")
      await ctx.send(embed=embed, file=file)

@client.command()
async def thank(ctx, mem: discord.User = None):
    if mem == None:
      mem = ctx.author.id
    emb = discord.Embed(title="", description=f"Arigatou {mem.mention} :)", color=0x2e69f2)
    emb.set_image(url="https://i.ytimg.com/vi/ALEFgAbDE8U/maxresdefault.jpg")
    await ctx.send(embed=emb)


@client.command()
async def befriend(ctx, mem: discord.User = None):
  if mem == None:
    mem = ctx.author
  emb = discord.Embed(title="", description=f"Kanna is your friend now uwu {mem.mention} :)", color=0x2e69f2)
  emb.set_image(url="https://i.pinimg.com/originals/d9/ff/de/d9ffde3f3d3114ca7012f6c6c153ec55.jpg")
  await ctx.send(embed=emb)

@client.command()
async def truth(ctx):
  truth = [
  "When was the last time you lied?",
  "When was the last time you cried?",
  "What's your biggest fear?",
  "What's your biggest fantasy?",
  "Do you have any fetishes?",
  "What's something you're glad your mum doesn't know about you?",
  "Have you ever cheated on someone?",
  "What's the worst thing you've ever done?",
  "What's a secret you've never told anyone?",
  "Do you have a hidden talent?",
  "Who was your first celebrity crush?",
  "What are your thoughts on politicians?",
  "What's the worst intimate experience you've ever had?",
  "Have you ever cheated in an exam?",
  "What's the most drunk you've ever been?",
  "Have you ever broken the law?",
  "What's the most embarrassing thing you've ever done?",
  "What's your biggest insecurity?",
  "What's the biggest mistake you've ever made?",
  "What's the most disgusting thing you've ever done?",
  "Who would you like to kiss in this server?",
  "What's the worst thing anyone's ever done to you?",
  "Have you ever had a run in with the law?",
  "What's your worst habit?",
  "What's the worst thing you've ever said to anyone?",
  "Have you ever peed in the shower?",
  "What's the strangest dream you've had?",
  "Have you ever been caught doing something you shouldn't have?",
  "What's the worst date you've been on?",
  "What's your biggest regret?",
  "What's the biggest misconception about you?",
  "Are you virgin?",
  "Why did your last relationship break down?",
  "Have you ever lied to get out of a bad date?",
  "What's the most trouble you've been in?"
]
  await ctx.send(f"Truth: {random.choice(truth)}")

@client.command()
async def dare(ctx):
  dare = [
  "Show the most embarrassing photo on your phone",
  "Show the last five people you texted and what the messages said",
  "Let the rest of the group DM someone from your Instagram account",
  "Eat a raw piece of garlic",
  "Do 100 squats",
  "Keep three ice cubes in your mouth until they melt",
  "Say something dirty to the person on your left",
  "Give a foot massage to the person on your right",
  "Put 10 different available liquids into a cup and drink it",
  "Yell out the first word that comes to your mind",
  "Give a lap dance to someone of your choice",
  "Remove four items of clothing",
  "Like the first 15 posts on your Facebook newsfeed",
  "Eat a spoonful of mustard",
  "Keep your eyes closed until it's your go again",
  "Send a text to the last person in your phonebook",
  "Show off your orgasm face",
  "Seductively eat a banana",
  "Empty out your wallet/purse and show everyone what's inside",
  "Do your best sexy crawl",
  "Pretend to be the person to your right for 10 minutes",
  "Eat a snack without using your hands",
  "Say two honest things about everyone else in the group",
  "Twerk for a minute",
  "Try and make the group laugh as quickly as possible",
  "Try to put your whole fist in your mouth",
  "Tell everyone an embarrassing story about yourself",
  "Try to lick your elbow",
  "Post the oldest selfie on your phone on Instagram Stories",
  "Tell the saddest story you know",
  "Howl like a wolf for two minutes",
  "Dance without music for two minutes",
  "Pole dance with an imaginary pole",
  "Let someone else tickle you and try not to laugh",
  "Put as many snacks into your mouth at once as you can"
]
  await ctx.send(f"Dare: {random.choice(dare)}")

@client.command(aliases=['lotto'])
async def lottery(ctx, *, guesses):
  '''Enter the lottery and see if you win!'''
  numbers = []
  for x in range(3):
    numbers.append(random.randint(0, 9))

  split = guesses.split(' ')
  if len(split) != 3:
    return await ctx.send('Please separate your numbers with a space, and make sure there are 3 numbers between 0 and 9.')
  string_numbers = [str(i) for i in numbers]
  if split[0] == string_numbers[0] and split[1] == string_numbers[1] and split[2] == string_numbers[2]:
    await ctx.send(f'{ctx.author.mention} You won! Congratulations on winning the lottery!')
  else:
    await ctx.send(f"{ctx.author.mention} Better luck next time... You were one of the 124/125 who lost the lottery...\nThe numbers were `{', '.join(string_numbers)}`")

@client.command()
async def arz(ctx):
  shayari=[
      "*samundar ke kinare abadi nahi hoti, jisse pyar ho usse shadi nhi hoti..\n~SENSEI*",
      "*Ladki ka hasna adda hai, jo use pyaar samjhe vo gadha hai..\n~SENSEI*",
      "*tera bhi katega..\n~SENSEI*",
      "*kadu kata hai mere dost intejaar kar sabme batega,\nishq hua hai? intejaar kar tera bhi katega..\n~SENSEI*",
      "*ab na tere aana ki khushi rhi na tere jaane ka gam,\nvo jamana beet gya jab tere diwane the hum..\n~SENSEI*",
      "*Wo tumhen DP dikhaakar gumraah karegi,\nMagar Tum Aadhaar card par adde rehna..\n~KAKASHI*",
      "*yeh waqt bhi guzar jayega..\n~KAKASHI*",
      "*na reply chahiye\nna tera sath\nnikal meri zindagi se\nnahi karni tujhse koi baat..\n~SENSEI*",
      "*insaan ka dil bara hona chaiye, chota to mera dongle bhi he..\n~SAIYAN*",
      "*age is just a number, jail is just a room..\n~DA 8 YEAR OLD*"
    ]
  emb = discord.Embed(title="arz kiya hai..", description=f"{random.choice(shayari)}", color=0x2e69f2)
  await ctx.send(embed=emb)

@client.command()
async def say(ctx, *, message):
  emb = discord.Embed(title=message, description=f"by {ctx.author.mention}", color=0x2e69f2)
  await ctx.send(embed=emb)

@client.command()
async def ship(ctx, m1: discord.User = None, m2: discord.User = None):
  if m1 == None:
    m1 = ctx.author
    m2 = ctx.author
  elif m2 == None:
    m2 = m1
    m1 = ctx.author

  ship_list=[
    "Possible..",
    "Not in this life..",
    "Maybe..",
    "Best couple!",
    "Looks impossible..",
    "Fated partners..",
    "Should already be in this relationship.."
  ]

  await ctx.send(f"{m1.mention} X {m2.mention}\n{random.choice(ship_list)}")


@client.event
async def on_message(message):
  await client.process_commands(message)

  love_words=[
    "i love you kanna chan",
    "love you kanna chan",
    "kanna chan i love you",
    "i love kanna chan",
    "kanna chan is love",
    "i love you kanna",
    "love you kanna"
  ]

  hate_words=[
    "i hate you kanna chan",
    "hate you kanna chan",
    "kanna chan i hate you",
    "kanna chan hate",
    "i hate you kanna",
    "hate you kanna"
  ]

  love_emb = discord.Embed(title="", description=f"Kanna loves you too {message.author.mention} uwu", color=0x2e69f2)
  love_emb.set_image(url="https://pa1.narvii.com/7231/f52073bab90f9a13f3e292af0b3e1b1e8f8ba189r1-540-304_hq.gif")
  
  hate_emb = discord.Embed(title="", description=f"Kanna is sad :( {message.author.mention} Kanna loves you :(", color=0x2e69f2)
  hate_emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/349/853/60b.gif")

  if message.content.lower() in love_words:
    if message.author.id == 784363251940458516:
      await message.channel.send(f"{message.author.mention}\nKanna loves asheesh too uwu..❤")
      await message.add_reaction('❤')
    else: 
      await message.channel.send(embed=love_emb)
      await message.add_reaction('❤')
  elif message.content.lower() in hate_words:
    if message.author.id == 784363251940458516:
      await message.channel.send(f"{message.author.mention}\nBut Kanna loves asheesh..❤")
      await message.add_reaction('❤')
    else: 
      await message.channel.send(embed=hate_emb)
      await message.add_reaction('❤')

token = config("TOKEN")
client.run(token)

