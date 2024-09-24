import discord
from discord.ext import commands
from bot_token import token
from database import init_db, close_db, add_task_to_db, get_all_tasks,delete_task_from_db, complete_task_db

description = ''' '''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    init_db('tasks.db')
    print(f'{bot.user} giriş yaptı.')
    print('------')


@bot.event
async def on_close():
    close_db()
    print("Database connection is closed.")


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi {ctx.author}! :wave:')

@bot.command(name="add_task")
async def add_task(ctx, *, description):
    author_id = str(ctx.author.id)
    add_task_to_db(author_id,description)

    await ctx.send(f"Task added! To list all tasks use !show_tasks")
  
@bot.command(name="delete_task")
async def delete_task(ctx, task_id: int):
    author_id = str(ctx.author.id)
    response = delete_task_from_db(task_id, author_id)

    if response:
        await ctx.send(f"Task {task_id} deleted.")
    else:
        await ctx.send(f"Either you can't delete this task because you're not the owner or there is no task with ID {task_id}")

@bot.command(name="show_tasks")
async def show_tasks(ctx):
    tasks = get_all_tasks()

    if tasks:
        await ctx.send("Here is the list of tasks.")
        for task in tasks:
          await ctx.send(f"{task[0]}: {task[2]} (Completed: {':negative_squared_cross_mark:' if task[3]== 0 else ':white_check_mark:' })")
    else:
        await ctx.send("You have no tasks.")


@bot.command(name="complete_task")
async def complete_task(ctx, task_id: int):
    author_id = str(ctx.author.id)
    response = complete_task_db(task_id,author_id)

    if response:
        await ctx.send(f"Task {task_id} marked as completed.")
    else:
        await ctx.send(f"There is no task with ID {task_id}.")


bot.run(token)