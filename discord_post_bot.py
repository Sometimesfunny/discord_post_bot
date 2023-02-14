import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import configparser


# create discord bot class
class DiscordBot(discord.Client):
    # constructor
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents ,*args, **kwargs)
        self.synced = False
    # on ready function
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        if not self.synced:
            await tree.sync()
            self.synced = True
    # on message function
    async def on_message(self, message):
        if message.author.bot:
            return

config = configparser.ConfigParser()
config.read('post_bot_config.ini')
token = config['AUTH']['bot_token']

# run bot
bot = DiscordBot(command_prefix='!')

tree = app_commands.CommandTree(bot)

GUILD_ID = 1006200270176407582
GUILD = bot.get_guild(GUILD_ID)

# create command create_embed to create and send embed
@tree.command(name='create_embed', description='Create and send an embed', guild=GUILD)
async def create_embed(interaction : discord.Interaction, topic : str):
    if not interaction.user.guild_permissions.administrator:
        return
    if topic == 'rules':
        embed = discord.Embed(
            title='📃RULES',
            description="Правила нашего сообщества, которые следует соблюдать каждому участнику во избежание недопониманий и конфликтных ситуаций.",
            color=0x0055e8
        )
        embed.add_field(
            name='1. Оскорбления🤬',
            value='Вы не можете оскорблять пользователей сообщества. Все члены нашего сообщества равны, поэтому, вы должны относиться друг к другу с уважением и пониманием. Это касается взаимодействия как внутри сообщества, так и за его рамками.',
            inline=False
        )
        embed.add_field(
            name='2. Обсуждение политики и религии🕍',
            value='У всех свои взгляды на эти темы, в связи с чем лучше в целом не обсуждать их.',
            inline=False
        )
        embed.add_field(
            name='3. Партнёрства🤝',
            value='Если мы сотрудничаем с каким-либо проектом, вам не стоит распространять информацию об этом. Не нужно писать об этом в их чате, в своём паблике и прочих ресурсах.\nПримечание: если мы не сказали о том, что партнёрство является открытым.',
            inline=False
        )
        embed.add_field(
            name='4. Упоминания DBS DAO👀',
            value='Упоминая, используя в описании профиля в соц сетях, или иным способом затрагивая DBS DAO, вы должны понимать, что берёте на себя прямую ответственность за репутацию нашего сообщества. Если ваши действия потенциально или прямо накладывают негативный отпечаток на репутацию DBS DAO, то, в зависимости от степени тяжести проблемы, мы можем принимать определённые меры, вплоть до исключения.',
            inline=False
        )
        embed.add_field(
            name='⭐️',
            value='Мы сами вправе выбирать наказание для вас, начиная от каких-то небольших ограничений или замечания, заканчивая киком из DAO.\nПо мере обнаружения каких-либо нарушений, сообщение будет обновляться.',
            inline=False
        )
        embed.set_footer(text=f'DBS DAO is a way to be in the black.')
    elif topic == 'buy_access':
        embed = discord.Embed(
            title='BUY ACCESS',
            url='https://www.dbsdao.com/',
            description="Choose the most comfortable option and let's build together!",
            color=0x0055e8
            )
        embed.add_field(name='30 DAYS', value='70$', inline=False)
        embed.add_field(name='90 DAYS', value='190$', inline=False)
        embed.add_field(name='180 DAYS', value='340$', inline=False)
        embed.add_field(name='365 DAYS', value='590$', inline=False)
        embed.set_footer(text=f'DBS DAO is a way to be in the black.')
    elif topic == 'roles_faq':
        embed = discord.Embed(
            title='ROLES FAQ',
            url='https://www.dbsdao.com/',
            description="Here you can find all the information you need to know about the roles.",
            color=0x0055e8
            )
        embed.add_field(name='1. FOUNDER', value='<@&1010546967320993833> Основатель DBS DAO', inline=False)
        embed.add_field(name='2. HEAD', value='<@&1009835688843288757> Ключевые участники команды DBS DAO', inline=False)
        embed.add_field(name='3. TEAM', value='<@&1009828332994580491> Команда DBS DAO', inline=False)
        embed.add_field(name='4. INFLUENCER', value='<@&1009853932094365696> Администратор канала, принимающий участие в партнерских программах DBS DAO', inline=False)        
        embed.add_field(name='5. DAO OG', value='<@&1009853732424527992> Роль, которую могут получить активные участники DAO, дает множество привелегий ', inline=False)
        embed.add_field(name='6. DAO MEMBER', value='<@&1010588528767418470> Участник закрытого сообщества DBS DAO', inline=False)
        embed.add_field(name='7. DBS OG', value='<@&1013031125632954511> OG роль, дающая право на вступление в закрытое сообщество DBS DAO на 2 недели.', inline=False)                
        embed.add_field(name='8. DBS MEMBER', value='<@&1010587178574827550> Участник сообщества DBS DAO', inline=False)
        embed.set_footer(text=f'DBS DAO is a way to be in the black.')
    elif topic == 'resources':
        embed = discord.Embed(
            title='RESOURCES',
            url='https://www.dbsdao.com/',
            color=0x0055e8
            )
        embed.add_field(name='1. DBS DAO WEBSITE', value='[dbsdao.com](https://www.dbsdao.com/)', inline=False)
        embed.add_field(name='2. DBS DAO TWITTER', value='[@DBSdao](https://twitter.com/DBSdao)', inline=False)
        embed.add_field(name='3. DBS DAO TG ANNOUNCEMENTS', value='[Telegram](https://t.me/+qu3BWoSBBNFjYjky)', inline=False)
        embed.add_field(name='4. DBS TG MAIN CHANNEL', value='[DBS](https://t.me/bomzhuem)', inline=False)
        embed.add_field(name='5. MAIL', value='dbscorporative@outlook.com', inline=False)
        embed.set_footer(text=f'DBS DAO is a way to be in the black.')
    elif topic == 'navigation':
        embed = discord.Embed(
            title='NAVIGATION',
            url='https://www.dbsdao.com/',
            description="Тут вы найдете всю актуальную информацию по нашим категориям и каналам внутри них:)\n***",
            color=0x0055e8
            )
        embed.add_field(
            name='💼IMPORTANT', 
            value='В данной категории вы найдете всю самую важную информацию о DBS DAO и мануал по нашему функционалу\n<#1006200270956531734> - приветственный канал для новых мемберов\n<#1009534135896903720> - правила пользования сервером DBS DAO\n<#1009526807621554196>  - ответы на самые важные вопросы\n<#1013076436204142642> - экскурс по значению и функционалу ролей\n<#1009808501213777951> - навигация по нашему серверу\n<#1009835062684041326> - сетка наших инф. ресурсов (подпишись чтобы ничего не пропустить!)\n<#1010571432272613458> - отчетность по доходам и наградам DBS DAO среди пользователей (WIP - будет доступен позже)\n<#1009813075727224945> - отзывы пользователей о работе DBS DAO\n<#1009855324364210266> - канал c мануалом по приобретению и обновлению подписки DBS DAO (WIP - будет доступен позже)\n***', 
            inline=False
            )
        embed.add_field(
            name='🏦HALL',
            value='В данной категории вы найдете общие анонсы и активности DBS DAO (как для <@&1010587178574827550> , так и для членов <@&1010588528767418470>)\n<#1009854337268330548> - Общие и самые важные анонсы DBS DAO\n<#1009854464477384735> - общий чат (как для <@&1010587178574827550> , так и для <@&1010588528767418470>\n<#1009856089254264922> - общий музыкальный чат\n<#1009937600238321745> общий чат 18+ (серьезно, 18+, фотка паспорта приветствуется)\n<#1009817627146846288> - канал с репостами наших анонсов из Твиттера (чтобы вы ничего не пропускали, нам это важно)\n<#1009854533461102593> - общая открытая трибуна (для больших собраний)\n<#1009854418960777246> - общий открытый войс\n<#1009856135836209212> - общий открытый войс №2 (чтобы вы не мешали друг-другу)\n***',
            inline=False
            )
        embed.add_field(
            name='🦾BOTS',
            value='В данной категории находится весь функционал для отслеживания собственного прогресса на сервере DBS DAO\n<#1011650872364765225> - отслеживание уровня прогресса общения в дискорде\n<#1011650910889447434> - команды для наших ботов\n<#1015701224642846910> - информация о комиссиях в сети Ethereum (обновляется каждые 5 минут)\n***',
            inline=False
            )
        embed.add_field(
            name='ДАЛЕЕ КАНАЛЫ ДОСТУПНЫ ТОЛЬКО ДЛЯ <@&1010588528767418470>',
            value='***',
            inline=False
        )
        embed.add_field(
            name='📣ANNOUNCEMENTS',
            value='В данной категории вы найдете все необходимые новости для <@&1010588528767418470> и актуальное расписание созвонов\n<#1009834334884220988> - анонсы для <@&1010588528767418470>\n<#1009835330700070995> - расписание DBS DAO COMMUNITY CALLS (расписание может обновляться, мы об этом оповестим)\n<#1009835520374865940> - записи DBS DAO COMMUNITY CALLS (только для <@&1010588528767418470>)\n***',
            inline=False
            )
        embed.add_field(
            name='💬CHATS',
            value='В данной категории вы найдете все тематические чаты для <@&1010588528767418470>\n<#1009814411562721320> - главный чат DBS DAO, подходит для всех обсуждений и флуда\n<#1009814536406188122> - чат для амбассадоров\n<#1009814602969780305> - чат для NFT-дегенов, простых флипперов и стронг-холдеров\n<#1009816645012828180> - чат по мультиаккингу и абузу\n<#1009814623278612500> - чат по нодам и валидаторству\n<#1009814783979171910> - чат по тестнетам\n<#1013055738744143953> - чат для обсуждения профитов <@&1010588528767418470> (не завидуем)\n<#1013055785724555354> - чат для обсуждения ректов  <@&1010588528767418470> (не плачем)\n<#1014512875005546567> - канал для взаимных подписок, кидайте свои линки!\n***',
            inline=False
            )
        embed.add_field(
            name='🔊VOICE CHANNELS',
            value='В данной категории расположены все войс-чаты для <@&1010588528767418470>\n<#1006200270956531735> - первый войс\n<#1009819821363449856> - второй войс (ну вы и сами догадались)\n<#1009860178478370926> - студийка, для прослушивания четкой музыки и не менее четкого ворка😎\n***',
            inline=False
            )
        embed.add_field(
            name='🎤Entertainment',
            value='В данной категории вы найдете сможете почиллить и расслабиться с остальными <@&1010588528767418470>\n<#1009820038729039974> - делимся лучшим дриллом, но и просто любители хороших треков у нас тоже имеются\n<#1009820058828165170> - собираем себе сквад и вместе проходим Sandbox (а можно и просто поиграть во что угодно)\n<#1009820178642649158> - делимся мемами, мы тоже будем делиться своими:)\n***',
            inline=False
            )
        embed.add_field(
            name='📷NFT',
            value='В данном разделе вы найдете всю актуальную информацию по NFT-направлению, популярным и не очень чейнам\n<#1009807794972676196> - Early-проекты на ETH, качественные коллы, дегенство и флипы, ничего лишнего\n<#1013029710055358526> - ресерч проектов на ETH от <@&1010588528767418470>\n<#1009807879164919859> - Early-проекты на SOL, качественные коллы, дегенство и флипы, ничего лишнего\n<#1013029762333155408> - ресерч проектов на SOL от <@&1010588528767418470>\n<#1009832920711692379> - здесь мы проводим розыгрыши вайтлистов для <@&1010588528767418470>\n***',
            inline=False
            )
        embed.add_field(
            name='🚀NFT-LAUNCHPADS',
            value='В данном разделе представлены все NFT-лаунчпады что мы отобрали на сопровождение (список может меняться в зависимости от их доходности) \n<#1013028508802490438> - актуальные проекты на Premint\n<#1013028817775886386> - актуальные проекты на Superful\n<#1013029477732843560> - актуальные сейлы на Binance NFT \n<#1013029432988020736> - актуальные проекты на лаунчпаде ME\n<#1013036081714843700> - актуальные сейлы на Coinbase\n<#1013036166469128212> - актуальные сейлы на Bybit\n***',
            inline=False
            )
        embed.add_field(
            name='💰ACTIVITIES',
            value='В данном разделе будут все активности, которые не вписываются в какую-то отдельную категорию\n<#1009839352911761469> - все активности в одном месте\n<#1021922715566878780> - трейдинг стратегии и коллы как правильно слить свой баланс\n***',
            inline=False
            )
        # embed.add_field(
        #     name='⚒DBS-WORKSPACE',
        #     value='В данном разделе мы создали рабочий уголок, в котором вы найдете все необходимые для работы тулзы\n<#1010568358049108078> - Notion воркспейс для <@&1010588528767418470> \n<#1010569252039823443> - Боты от наших прогеров для <@&1010588528767418470>\n***',
        #     inline=False
        #     )
        embed.add_field(
            name='📚EDUCATION',
            value='В данном разделе собраны все авторские мануалы для обучения полезным навыкам и скилам\n<#1012058286788452382> - авторские статьи от <@&1009828332994580491> DBS DAO\n<#1012058325724168243> - авторские статьи от <@&1010588528767418470>, делитесь своими трудами и находками!\n<#1012058404220567604> - cтатьи от <@&1009828332994580491> DBS DAO по ментальному здоровью и его поддержанию\n***',
            inline=False
            )
        embed.add_field(
            name='👨⚕THERAPIST',
            value='В данном разделе вам окажут психологическую помощь и поддержку\n<#1012058404220567604> - cтатьи от <@&1009828332994580491> DBS DAO по ментальному здоровью и его поддержанию\n***',
            inline=False
        )
        embed.add_field(
            name='🤑IDO-ICO',
            value='В данном разделе вы найдете всю актуальную информацию и ресерч метрик по токенсейлам на выбранных лаунчпадах (список может обновляться в зависимости от их доходности)\n***',
            inline=False
            )
    elif topic == 'navigation_2':
        embed = discord.Embed(
            title='NAVIGATION 2',
            url='https://www.dbsdao.com/',
            description="Тут вы найдете всю актуальную информацию по нашим категориям и каналам внутри них:)\n***",
            color=0x0055e8
            )
        embed.add_field(
            name='🥇AMBASSADOR T1',
            value='В данном разделе вы найдете всю актуальную информацию по участию в Tier1-амбассадорках, а также их список (cписок может меняться)\n***',
            inline=False
            )
        embed.add_field(
            name='🥈AMBASSADOR T2',
            value='В данном разделе вы найдете всю актуальную информацию по участию в Tier2-амбассадорках, а так же их список (список может меняться)\n***',
            inline=False
            )
        embed.add_field(
            name='🥉AMBASSADOR T3',
            value='В данном разделе вы найдете всю актуальную информацию по участию в Tier3-амбассадорках, а так же их список (список может меняться)\n***',
            inline=False
            )
        embed.add_field(
            name='🤖TESTNETS',
            value='Актуальные и перспективные (по нашему сугубо личному мнению) тестнеты с лонг-терм перспективой, а также мануалы и их разбор\n***',
            inline=False
            )
        embed.add_field(
            name='🎰NODES',
            value='Актуальные ноды с мануалом по установке и их поддержанию (список может меняться)\n***',
            inline=False
            )
        embed.add_field(
            name='💻MULTIACCING',
            value='Актуальные и перспективные (по нашему сугубо личному мнению) проекты и темы, которые можно абузить, а также мануалы по ним\n***',
            inline=False
            )
        embed.add_field(
            name='🎮PLAY TO EARN',
            value='Самые интересные и (потенциально) доходные игры из мира WEB3\n***',
            inline=False
        )
        embed.add_field(
            name='🌐WEB3 QUESTS',
            value='Новый быстроразвивающийся тренд квестов в мире WEB3. Рассказываем о самых доходных квестах, как их оптимально абузить и выполнять\n***',
            inline=False
        )
        embed.add_field(
            name='😤OG PLACE',
            value='Отдельная категория для самых активных контрибьюторов DBS DAO - <@&1009853732424527992>\nВ данной ветке можно найти эксклюзивные раффлы и предложения для самых активных пользователей, инструкцию по получению данной роли можно найти в разделе <#1013076436204142642>\n***',
            inline=False
            )
    embed.set_author(name='DBS DAO', url='https://www.dbsdao.com/', icon_url='https://pbs.twimg.com/profile_images/1528813629788790785/9nJ95kjl_400x400.jpg')
    embed.set_footer(text=f'DBS DAO is a way to be in the black.')
    await interaction.response.send_message(embed=embed)

@tree.command(name='delete_history', description='Deletes last 100 messages from channel.', guild=GUILD)
async def delete_history(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return
    await interaction.response.defer(thinking=True)
    await interaction.channel.purge(limit=100)

@tree.command(name='switch_off_invites', description='Switch off invites', guild=GUILD)
async def switch_off_invites(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return
    await interaction.response.defer(thinking=True, ephemeral=True)
    dbs_member = interaction.guild.get_role(1010587178574827550)
    dao_member = interaction.guild.get_role(1010588528767418470)
    overwrite = discord.PermissionOverwrite(create_instant_invite = True)
    overwrites = {
        dbs_member : overwrite,
        dao_member : overwrite
    }
    for channel in interaction.guild.channels:
        await channel.edit(target=dbs_member, overwrites=overwrites, reason='Invites are disabled for dbs_member')
        await asyncio.sleep(0.5)
        break
    await interaction.followup.send('Invites are disabled', ephemeral=True)
    
@tree.command(name='switch_on_invites', description='Switch on invites', guild=GUILD)
async def switch_on_invites(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return
    await interaction.response.defer(thinking=True, ephemeral=True)
    dbs_member = interaction.guild.get_role(1010587178574827550)
    dao_member = interaction.guild.get_role(1010588528767418470)
    for channel in interaction.guild.channels:
        await channel.set_permissions(target=dbs_member, create_instant_invite=True, reason='Invites are enabled for dbs_member')
        await channel.set_permissions(target=dao_member, create_instant_invite=True, reason='Invites are enabled for dao_member')
        await asyncio.sleep(0.5)
    await interaction.followup.send('Invites are enabled', ephemeral=True)

@tree.command(name='permissions_only_dao', description='Set permissions in category only for DAO members', guild=GUILD)
async def permissions_only_dao(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return
    await interaction.response.defer(thinking=True, ephemeral=True)
    dbs_member = interaction.guild.get_role(1010587178574827550)
    dao_member = interaction.guild.get_role(1010588528767418470)
    team = interaction.guild.get_role(1009828332994580491)
    category = interaction.channel.category
    overwrite_team = discord.PermissionOverwrite(
        add_reactions = True,
        administrator = False,
        attach_files = True,
        ban_members = False,
        change_nickname = False,
        connect = True,
        create_instant_invite = False,
        create_private_threads = False,
        create_public_threads = False,
        deafen_members = False,
        embed_links = False,
        external_emojis = False,
        external_stickers = False,
        kick_members = True,
        manage_channels = True,
        manage_emojis = False,
        manage_emojis_and_stickers = False,
        manage_events = True,
        manage_guild = False,
        manage_messages = True,
        manage_nicknames = False,
        manage_permissions = False,
        manage_roles = False,
        manage_threads = False,
        manage_webhooks = False,
        mention_everyone = True,
        moderate_members = True,
        move_members = True,
        mute_members = True,
        priority_speaker = True,
        read_message_history = True,
        read_messages = True,
        request_to_speak = True,
        send_messages = True,
        send_messages_in_threads = False,
        send_tts_messages = False,
        speak = True,
        stream = True,
        use_application_commands = False,
        use_embedded_activities = True,
        use_external_emojis = False,
        use_external_stickers = False,
        use_voice_activation = True,
        view_audit_log = False,
        view_channel = True,
        view_guild_insights = False
    )
    overwrite_dao = discord.PermissionOverwrite(
        add_reactions = True,
        administrator = False,
        attach_files = False,
        ban_members = False,
        change_nickname = False,
        connect = True,
        create_instant_invite = False,
        create_private_threads = False,
        create_public_threads = False,
        deafen_members = False,
        embed_links = False,
        external_emojis = False,
        external_stickers = False,
        kick_members = False,
        manage_channels = False,
        manage_emojis = False,
        manage_emojis_and_stickers = False,
        manage_events = False,
        manage_guild = False,
        manage_messages = False,
        manage_nicknames = False,
        manage_permissions = False,
        manage_roles = False,
        manage_threads = False,
        manage_webhooks = False,
        mention_everyone = False,
        moderate_members = False,
        move_members = False,
        mute_members = False,
        priority_speaker = False,
        read_message_history = True,
        read_messages = True,
        request_to_speak = True,
        send_messages = False,
        send_messages_in_threads = False,
        send_tts_messages = False,
        speak = True,
        stream = True,
        use_application_commands = False,
        use_embedded_activities = False,
        use_external_emojis = False,
        use_external_stickers = False,
        use_voice_activation = True,
        view_audit_log = False,
        view_channel = True,
        view_guild_insights = False
        )
    overwrite_dbs = discord.PermissionOverwrite(read_messages = False, view_channel = False)
    overwrites = {
        interaction.guild.default_role : overwrite_dbs,
        dbs_member : overwrite_dbs,
        dao_member : overwrite_dao,
        team : overwrite_team
    }
    await category.edit(overwrites=overwrites, reason='Permissions are set only for DAO members')
    for channel in category.channels:
        await channel.edit(overwrites=overwrites, reason='Only DAO members can see this channel')
        await asyncio.sleep(0.5)
    await interaction.followup.send('Permissions are set only for DAO members', ephemeral=True)


bot.run(token)
