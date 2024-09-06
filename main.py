import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import flip_coin_f
from bot_logic import gen_emojis
from settings import settings

prefix = settings["Prefix"]
commands_list = ["cmds", "hello", "bye", "random_password", "random_emoji", "flip_coin", "joined_server", "joined_discord", "help_environment"]
commands_desc = {
    "cmds" : "Sends all the available commands.",
    "hello" : "Responds with: Hi.",
    "bye" : "Responds with: Bye.",
    "random_password" : "Generates a random password.",
    "random_emoji" : "Generates a random emoji.",
    "flip_coin" : "Flips a coin.",
    "joined_server" : "Tells the date the user joined this server.",
    "joined_discord" : "Tells the date the user joined Discord.",
    "help_environment" : "Tells you some tips to help the environment. (In Spanish)"
}
testing_commands_list = ["test"]
testing_commands_desc = {
    "test" : "Testing stuff."
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cmds(ctx):
        send = ""
        for i in commands_list:
            send += f"```css\n[{i}]: {commands_desc[i]}\n```"

        embed = discord.Embed(
            title = "Command list",
            description = "",
            color = int("84b6f4", 16)
        )
        embed.add_field(
            name = "",
            value = "```yaml\n Prefix: " + prefix + "\n```\n" + send,
            inline = False
        )
        embed.add_field(
            name = "",
            value = "",
            inline = True
        )
        embed.set_footer(
            text = "This includes all the available commands."
        )
        # embed.set_image(
            # url = ""
        # )

        button = discord.ui.Button(style=discord.ButtonStyle.secondary, label='Testing')

        view = discord.ui.View()
        view.add_item(button)

        message = await ctx.send(embed = embed, view = view)

        @bot.event
        async def on_interaction(interaction):
            if interaction.type == discord.InteractionType.component:
                if interaction.data.get('component_type') == 2:
                    button.disabled = True
                    send2 = ""
                    for i in testing_commands_list:
                        send2 += f"```css\n[{i}]: {testing_commands_desc[i]}\n```"
                    message = await interaction.channel.fetch_message(interaction.message.id)
                    embed = message.embeds[0]
                    embed.title = "[Testing] Command list"
                    embed.set_field_at(0, name = "", value = "```yaml\n Prefix: " + prefix + "\n```\n" + send2, inline = False)
                    await interaction.response.edit_message(embed=embed, view=view)


@bot.command()
async def hello(ctx):
    await ctx.send(f'<:yes:1273791797797326949> Hello {ctx.author.mention}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'<:yes:1273791797797326949> Bye {ctx.author.mention}!')

@bot.command()
async def random_password(ctx, length: int = 20):
    await ctx.send(gen_pass(length))

@bot.command()
async def random_emoji(ctx):
    await ctx.send(gen_emojis())

@bot.command()
async def flip_coin(ctx):
    await ctx.send(flip_coin_f())

@bot.command()
async def joined_server(ctx, member: discord.Member):
    await ctx.send(f'{ctx.author.mention} joined this server on {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def joined_discord(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} joined Discord on {discord.utils.format_dt(member.created_at)}')

@bot.command()
async def help_environment(ctx, num=None):
    categorías = {
    1 : ["Reducir cantidad de residuos.", "Formas sencillas de disminuir residuos.", "Reducir cantidad de residuos eficientemente.", "1. **Usa botellas y vasos reutilizables**: Lleva contigo una botella de agua reutilizable y un vaso para café. Esto reduce el uso de botellas y vasos desechables. \n2. **Bolsas de compras reutilizables**: Siempre lleva contigo bolsas reutilizables cuando vayas de compras. Esto ayuda a disminuir el uso de bolsas plásticas de un solo uso. \n3. **Compra a granel**: Opta por comprar productos a granel para reducir el uso de empaques innecesarios."],
    2 : ["Opciones de reciclaje.", "Qué cosas reciclar.", "Cosas que se pueden reciclar.", "Puedes reciclar: \n**Papel y Cartón (Contenedor Azul)**: Asegúrate de que estén limpios y secos. No incluyas papel plastificado o sucio. \n**Plástico y Latas (Contenedor Amarillo)**: Limpia los envases antes de reciclar para evitar la contaminación. \n**Vidrio (Contenedor Verde)**: Retira las tapas y enjuaga los envases. No incluyas cristales rotos o espejos. \n**Orgánicos (Contenedor Marrón)**: Usa una compostera si tienes espacio, o deposítalos en el contenedor de orgánicos."],
    3 : ["Recomendaciones.", "Recomendaciones en general.", "Recomendaciones para disminuir residuos y reciclar.", "Compra a granel y evita productos con mucho empaque. \nUsa productos reutilizables como botellas y bolsas. \nPlanifica tus comidas para evitar el desperdicio de alimentos. \nRepara y reutiliza objetos antes de desecharlos. \nDona lo que no uses en lugar de tirarlo. \nSepara tus residuos en papel, plástico, vidrio y orgánicos. \nLimpia los envases antes de reciclarlos. \nComposta tus residuos orgánicos si tienes espacio."],
}
    if num is None:
        embed = discord.Embed(title = '¡Formas de cuidar al medio ambiente!', description = '¿Quieres aprender a cuidar el medio ambiente? Ingresa un número para seleccionar una categoría:\n1. Reducir cantidad de residuos\n2. Opciones de reciclaje\n3. Recomendaciones', color=0x32CD32)
        embed.set_footer(text = 'Ej: !help_environment 1')
        await ctx.send(embed = embed)
    elif num.isdigit() and 1 <= int(num) <= 3:
        num = int(num)
        embed = discord.Embed(title = categorías[num][2], description = categorías[num][3], color = 0x32CD32)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = '¡Formas de cuidar al medio ambiente!', description = '¿Quieres aprender a cuidar el medio ambiente? Ingresa un número para seleccionar una categoría:\n1. Reducir cantidad de residuos\n2. Opciones de reciclaje\n3. Recomendaciones', color=0x32CD32)
        embed.set_footer(text = 'Ej: !help_environment 1')
        await ctx.send(embed = embed)
        await ctx.send('Ingrese un número válido (1, 2 o 3)')

@bot.command()
async def test(ctx):
    await ctx.send("nothing to test rn")

    

bot.run(settings["Token"])
