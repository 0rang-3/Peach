import discord
from discord.ext import commands
import asyncio
import random
import time


class RL_IN_Discord(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def rl (self, ctx):
    await ctx.send("This is Rocket League in Discord! First to 1 Goal!")
    await ctx.send(f"{ctx.message.author.mention} Choose a gamemode. Type: `1v1`")
    try:
      msg = await self.client.wait_for('message', timeout=15)
      def check(message):
        return message.content == ""
    except asyncio.TimeoutError:
      await ctx.send(f"{ctx.message.author.mention} You didn't type the gamemode in 15 seconds. Try again and be quicker!")
      return


    if msg.content == "1v1":
      your_kickoff = random.randint(1, 5)
      if your_kickoff == 1:
        #Left Diagonal Kickoff Image
        await ctx.send("https://lh3.googleusercontent.com/VJd5hqkUFDb5AocaFJzQRToJGxZO4vVefjg80hmvY3IpAU_x0Q7gW9nYwhk2UHbz_i4xkKgbMLMQFQUVHjBwt-z-R_v0B7Fa6DLinUze-S281FJ6xKCX2jK_sopfupvDh3I6QB2WEA=w2400")
        await ctx.send(f"{ctx.message.author.mention} You have a Left Diagonal Kickoff!")
      elif your_kickoff == 2:
        #Right Diagonal Kickoff Image
        await ctx.send("https://lh3.googleusercontent.com/fuZ89uhARSVKhsxHVrtnIl6yDWkApKmhD_KSN8vPWtWu-2DZauN5ZwZyqO2DGyw3xZJSWmGS3X3XhdcFPdrRDb2qe6rf-QW-csHmZXsrrQRx3xLTzY-zODtx4BjayhXf4DaPSgQysQ=w2400")
        await ctx.send(f"{ctx.message.author.mention} You have a Right Diagonal Kickoff!")
      elif your_kickoff == 3:
        #Left Semi-Straight Kickoff Image
        await ctx.send("https://lh3.googleusercontent.com/I9DcNsYbKoBNWybK-CCb6U_yAgpbk583CAcgBMZgCJev-LCIDXnVUcY-R1EgZLPshsPUZEe_5_IJ92lMbUcXN4lARHk63bBbhBK2efmqDpw2u0sCs_qPpuJRgyjO0X4oPUVVboPgIA=w2400")
        await ctx.send(f"{ctx.message.author.mention} You have a Left Semi-Straight Kickoff!")
      elif your_kickoff == 4:
        #Right Semi-Straight Kickoff Image
        await ctx.send("https://lh3.googleusercontent.com/JMmj2Q88A_kDRU5npGSVprxgkm-tL5cEmlMaKnDL0IS98MVc1wYrR0v3TejzTJJm-5aUKUVAv02cSCCBzPfosp-S_wSgMsAeuS_TmTKU9XwnaCkzSqPk_K7wiXio_cmwW2NIUTaEgg=w2400")
        await ctx.send(f"{ctx.message.author.mention} You have a Right Semi-Straight Kickoff!")
      else:
        #Straight Kickoff Image
        await ctx.send("https://lh3.googleusercontent.com/DC5Jrz2-34I35nxIdwLa4i8AYmJE0JVrlYYfB24lkwiSmeKzYeShHw0lq7m915tPN836EnYh1at1zfTl6LSgovwSDHc65jPvsKn7uKsYdv_Gz-K4Nu2TPFPU1m3i17wv9n3E_-FBPA=w2400")
        await ctx.send(f"{ctx.message.author.mention} You have a Straight Kickoff!")
      


      time.sleep(1)
      kickoff_percent = random.randint(1, 100)
      #Diagonal
      if your_kickoff == 1 or your_kickoff == 2:
        await ctx.send(f"{ctx.message.author.mention} Do you want to go for the kickoff? [y/n]")
        try:
          msg = await self.client.wait_for('message', timeout=60)
          def check(message):
            return message.content == ""
        except asyncio.TimeoutError:
          await ctx.send("You didn't type the gamemode in 60 seconds. Try again and be quicker!")
        if msg.content == "y":
          if kickoff_percent >= 1 and kickoff_percent <= 85:
            ball_after_kickoff = random.randint(1, 2)
            if ball_after_kickoff == 1:
              await ctx.send(f"{ctx.message.author.mention} The ball went on the opponenets side. Do you want to go and hit the ball? [y/n]")
              try:
                msg = await self.client.wait_for('message', timeout=60)
                def check(message):
                  return message.content == ""
              except asyncio.TimeoutError:
                await ctx.send("You didn't type the gamemode in 60 seconds. Try again and be quicker!")
                return
              if msg.content == "y":
                chance_of_win = random.randint(1, 100)
                if chance_of_win <= 25:
                  await ctx.send(f"{ctx.message.author.mention} You scored a goal and won! YAY!")
                  #Air Strike
                  await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
                  return
                if chance_of_win <= 50:
                  await ctx.send(f"{ctx.message.author.mention} You hit the ball, but missed the goal! It's still on the opponenet's side, but in the opposite corner! You decised to give up possion and head back to goal.")
                  chance_of_win2 = random.randint(1, 2)
                  if chance_of_win2 == 1:
                    await ctx.send("Your opponenet took advantage of you heading back to goal and attemptted to score on you. Luckily, you saved the shot and scored on your opponent!")
                    await ctx.send("You win!")
                    #Air Strike
                    await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                  else:
                    await ctx.send("Your opponenet took advantage of you heading back to goal and attemptted to score on you. They scored on you!")
                    await ctx.send("You lose!")
                    #White Riser
                    await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                else:
                  await ctx.send("The ball bounced back onto your side.")
                  chance_of_win3 = random.randint(1, 2)
                  if chance_of_win3 == 1:
                    await ctx.send(f"{ctx.message.author.mention} Your opponent just missed your goal and you demolished them! You took advantage of the situation and scored!")
                    await ctx.send("You win!")
                    #Air Strike
                    await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                  if chance_of_win3 == 2:
                    await ctx.send(f"{ctx.message.author.mention} You couldn't get back to your goal in time and your opponent scored!")
                    await ctx.send("You lose!")
                    #White Riser
                    await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
              elif msg.content == "n":
                chance_of_goal4 = random.randint(1, 2)
                if chance_of_goal4 == 1:
                  await ctx.send("The ball bounced off a wall and landed straight in your goal!")
                  await ctx.send("You lose!")
                    #White Riser
                  await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
                if chance_of_goal4 == 2:
                  await ctx.send("The ball landed on your side and you scored while your opponenet is recovering from the kickoff!")
                  await ctx.send("You win!")
                  #Air Strike
                  await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
          else:
            chance_of_goal4 = random.randint(1, 2)
            if chance_of_goal4 == 1:
              await ctx.send("You missed the kickoff! The ball bounced off a wall and landed straight in your goal!")
              await ctx.send("You lose!")
              #White Riser
              await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
              time.sleep(1)
              await ctx.send("Game Over!")
            if chance_of_goal4 == 2:
              await ctx.send("You missed the kickoff and the ball landed on your side! You scored while your opponenet is recovering from the kickoff!")
              await ctx.send("You win!")
              #Air Strike
              await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
              time.sleep(1)
              await ctx.send("Game Over!")
        elif msg.content == "n":
          chance_of_goal5 = random.randint(1, 2)
          if chance_of_goal5 == 1:
            await ctx.send("Your opponent saw that you didn't go for the kickoff and scored on you!")
            await ctx.send("You lose!")
            #White Riser
            await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
            time.sleep(1)
            await ctx.send("Game Over!")
          if chance_of_goal5 == 2:
            await ctx.send("Your opponent hit the ball right to you and you hit the ball into their goal!")
            await ctx.send("You win!")
            #Air Strike
            await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
            time.sleep(1)
            await ctx.send("Game Over!")
        else:
          await ctx.send("Error! You didn't type 'y' or 'n'!")
      #Semi-Straight and Straight
      if your_kickoff >= 3 and your_kickoff <= 5:
        await ctx.send(f"{ctx.message.author.mention} Do you want to go for the kickoff? [y/n]")
        try:
          msg = await self.client.wait_for('message', timeout=60)
          def check(message):
            return message.content == ""
        except asyncio.TimeoutError:
          await ctx.send("You didn't type the gamemode in 60 seconds. Try again and be quicker!")
        
        if msg.content == "y":
          if kickoff_percent >= 1 and kickoff_percent <= 95:
            ball_after_kickoff = random.randint(1, 2)
            if ball_after_kickoff == 1:
              await ctx.send(f"{ctx.message.author.mention} The ball went on the opponenets side. Do you want to go and hit the ball? [y/n]")
              try:
                msg = await self.client.wait_for('message', timeout=60)
                def check(message):
                  return message.content == ""
              except asyncio.TimeoutError:
                await ctx.send("You didn't type the gamemode in 60 seconds. Try again and be quicker!")
                return
              if msg.content == "y":
                chance_of_win = random.randint(1, 100)
                if chance_of_win <= 25:
                  await ctx.send(f"{ctx.message.author.mention} You scored a goal and won! YAY!")
                  #Air Strike
                  await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
                  return
                if chance_of_win <= 50:
                  await ctx.send(f"{ctx.message.author.mention} You hit the ball, but missed the goal! It's still on the opponenet's side, but in the opposite corner! You decised to give up possion and head back to goal.")
                  chance_of_win2 = random.randint(1, 2)
                  if chance_of_win2 == 1:
                    await ctx.send("Your opponenet took advantage of you heading back to goal and attemptted to score on you. Luckily, you saved the shot and scored on your opponent!")
                    await ctx.send("You win!")
                    #Air Strike
                    await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                  else:
                    await ctx.send("Your opponenet took advantage of you heading back to goal and attemptted to score on you. They scored on you!")
                    await ctx.send("You lose!")
                    #White Riser
                    await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                else:
                  await ctx.send("The ball bounced back onto your side.")
                  chance_of_win3 = random.randint(1, 2)
                  if chance_of_win3 == 1:
                    await ctx.send(f"{ctx.message.author.mention} Your opponent just missed your goal and you demolished them! You took advantage of the situation and scored!")
                    await ctx.send("You win!")
                    #Air Strike
                    await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
                  if chance_of_win3 == 2:
                    await ctx.send(f"{ctx.message.author.mention} You couldn't get back to your goal in time and your opponent scored!")
                    await ctx.send("You lose!")
                    #White Riser
                    await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                    time.sleep(1)
                    await ctx.send("Game Over!")
                    return
              elif msg.content == "n":
                chance_of_goal4 = random.randint(1, 2)
                if chance_of_goal4 == 1:
                  await ctx.send("The ball bounced off a wall and landed straight in your goal!")
                  await ctx.send("You lose!")
                    #White Riser
                  await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
                if chance_of_goal4 == 2:
                  await ctx.send("The ball landed on your side and you scored while your opponenet is recovering from the kickoff!")
                  await ctx.send("You win!")
                  #Air Strike
                  await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
                  time.sleep(1)
                  await ctx.send("Game Over!")
          else:
            chance_of_goal6 = random.randint(1, 100)
            if chance_of_goal6 <=25:
              await ctx.send("The opponent scored because you missed the kickoff!")
              await ctx.send("You lose!")
              #White Riser
              await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
              time.sleep(1)
              await ctx.send("Game Over!")
            elif chance_of_goal6 <= 50:
              await ctx.send("You missed the kickoff and your opponent hit the ball on your crossbar. Unfortunately for you, they were able to finish the play by scoring!")
              await ctx.send("You lose!")
              #White Riser
              await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
              time.sleep(1)
              await ctx.send("Game Over!")
            else:
              await ctx.send("You missed the kickoff, but luckily, your opponent missed your goal. You quickly recovered from the kickoff and scored on them.")
              await ctx.send("You win!")
              #Air Strike
              await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
              time.sleep(1)
              await ctx.send("Game Over!")

        if msg.content == "n":
          chance_of_goal6 = random.randint(1, 100)
          if chance_of_goal6 <= 25:
            await ctx.send("The opponent scored because you didn't go for the kickoff!")
            await ctx.send("You lose!")
            #White Riser
            await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
            time.sleep(1)
            await ctx.send("Game Over!")
          elif chance_of_goal6 <= 50:
            await ctx.send("You didn't go for the kickoff and your opponent hit the ball on your crossbar. Unfortunately for you, they were able to finish the play by scoring!")
            await ctx.send("You lose!")
            #White Riser
            await ctx.send("https://media.giphy.com/media/WkvFCv7WcNmW6jBCVR/giphy.gif")
            time.sleep(1)
            await ctx.send("Game Over!")
          else:
            await ctx.send("You didn't go for the kickoff, but luckily, your opponent missed your goal. You quickly scored on them.")
            await ctx.send("You win!")
            #Air Strike
            await ctx.send("https://media.giphy.com/media/P0xfyjx3NXJ4hhBoIq/giphy.gif")
            time.sleep(1)
            await ctx.send("Game Over!")
        else:
          await ctx.send("Error! You didn't type 'y' or 'n'!")


  
def setup(client):
  client.add_cog(RL_IN_Discord(client))