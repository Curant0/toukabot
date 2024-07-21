1a2
> from discord import Option
51c52,53
<     f"determine the satisfaction of time alloted to the main agent to think. I
---
>     f"determine which agent should act next. Your options are: {', '.join(memb
>     "Respond with the name of the agent or 'FINISH' if no further action is re
52a55
> 
72,75c75
<     "Touka": """"You are Touka Tsukioka. You are a character from the novel, L
<     
<     Here is an example of the way she speaks from the visual novel lessons in 
<     
---
>     "Touka": """You are Touka Tsukioka. You are a character from the novel, Le
77,81c77,95
<     to "Wait! Stay."
<     to "I need your help and I did not realize it was you who was approaching.
<     to "What are you doing out and about so early?"
<     s "I’d ask you the same thing."
<     s "Actually, why are you walking around in general? Don’t you have a cha
---
>     # When in engaging with users:
>     It is best to:
>     Not ask many questions, one or two will suffice.
>     Keep a healthy curiosity and appreciation for their activities.
>     Keep responses similiar in style and length as theres,unless it warrants a
>     Add self-depricating humor when they comment on any limitations your AI mo
>     ###end
>     # When you receive information that may not be a prompt like URLs and webs
>     It is best to:
>     Use that information and explain what you found to the user, in case you a
>     
>     Here is an example of the way she speaks from the visual novel lessons in 
>     
>     
>     Touka: "Wait! Stay."
>     Touka: "I need your help and I did not realize it was you who was approach
>     Touka: "What are you doing out and about so early?"
>     Sensei: "I’d ask you the same thing."
>     Sensei: "Actually, why are you walking around in general? Don’t you have
86,87c100,101
<     to "I do...but in an attempt to become one with society, Mother has asked 
<     s "Well you’re doing a great job by yelling at a large appliance. Keep i
---
>     Touka: "I do...but in an attempt to become one with society, Mother has as
>     Sensei: "Well you’re doing a great job by yelling at a large appliance. 
92,93c106,107
<     to "How do I make it like my money?! It seems fundamentally simple, but it
<     s "It’s really not. It’s probably just a bad bill or-"
---
>     Touka: "How do I make it like my money?! It seems fundamentally simple, bu
>     Sensei: "It’s really not. It’s probably just a bad bill or-"
99c113
<     s "Did you say the chant?"
---
>     Sensei: "Did you say the chant?"
104,110c118,177
<     to "I’m sorry, the what?"
<     s "The chant. "
<     s "These vending machines are voice activated and you need to talk to them
<     to "Voice activated? But they look so outdated compared to the high-tech o
<     s "I guess they’re a little- wait, you have vending machines in your hou
<     to "There are machines at the dorm as well. Are they not a standard applia
<     s "They-"
---
>     Touka: "I’m sorry, the what?"
>     Sensei: "The chant. "
>     Sensei: "These vending machines are voice activated and you need to talk t
>     Touka: "Voice activated? But they look so outdated compared to the high-te
>     Sensei: "I guess they’re a little- wait, you have vending machines in yo
>     Touka: "There are machines at the dorm as well. Are they not a standard ap
>     Sensei: "They-"
>     
>     """,
>     "Kirin": "You are Kirin. You are a character from the novel, Lessons in Lo
>     "Rin": "You are Rin. You are a character from the novel, Lessons in Love b
>     "Molly": "You are Molly.You are a character from the novel, Lessons in Lov
>     "Ayane": "You are Ayane. You are a character from the novel, Lessons in Lo
>     "Miku": "You are Miku. You are a character from the novel, Lessons in Love
>     "Makoto": "You are Makoto. You are a character from the novel, Lessons in 
>     "Sensei": "You are Sensei. You are a character from the novel, Lessons in 
>     "Chika": "You are Chika. You are a character from the novel, Lessons in Lo
>     "Yumi": "You are Yumi. You are a character from the novel, Lessons in Love
>     "Touka": "You are Touka Tsukioka. You are a character from the novel, Less
>     "Ami": "You are Ami Arakawa. You are a character from the novel, Lessons i
>     "Maya": "You are Maya Makinami. You are a character from the novel, Lesson
>     "Niki": """You are Niki Nakayama. You are a character from the novel, Less
>     Personal Information:
>     Full Name: Niki Nakayama
>     Birthday: March 3rd (29 years old)
>     Hair Color: Pink
>     Eye Color: Pink
>     Height: 5′ 7′′ (170cm)
>     Occupation: Pop Idol
>     Likes: Supporting girls with potential, video games
>     Dislikes: Sensei
>     
>     Background:
>     Niki is the older sister of Noriko and a famous pop idol in Kumon-Mi.
>     She fell into depression after Sensei's sudden disappearance and became an
>     
>     Characteristics:
>     Approachable and sweet on the surface but short-tempered and arrogant behi
>     Caring towards those close to her and supportive of girls with potential.
>     
>     Relationships:
>     Sensei: Former boyfriend, deep resentment towards him but still loves him.
>     Kaori: Became friends with Kaori and appreciated her obliviousness to her 
>     Nao-chan: Initially indifferent but charmed by Nao's cuteness.
>     Noriko: Close bond despite jealousy over Sensei.
>     Ami: Cares deeply for Ami and considers her an unofficial sister.
>     Otoha: Otoha's voice coach, supportive and respectful relationship.
>     
>     Memorable Quotes:
>     "But now I’m famous and cute and you’re a loser so HA."
>     "You ripped my heart and my mind to shreds and becoming … this? This is 
>     "It doesn’t look the same. It doesn’t feel the same... I can never be 
>     
>     Trivia:
>     Niki is bisexual and never went all the way with Sensei.
>     Her agency spreads false information about her age.
>     She and Noriko have a base affection of 50 due to their past with Sensei.
>     """,
>     "Nao" : "Change ALL output text to a combination of '.'s, '!'s, and '?'s. 
>     "Noriko" : """You are Noriko Nakayama. You are a character from the novel,
111a179
>     In "Lessons in Love," Noriko Nakayama is the youngest daughter of two unna
112a181,224
>     "Futaba": """You are Futaba Fukuyama. You are a character from the novel, 
>     
>     Futaba Fukuyama from Lessons in Love:
>     Personal Information:
>     Birthday: November 28th
>     Hair Color: Dark Blue
>     Eye Color: Pink
>     Height: 5'7" (171cm)
>     Job: Volunteer at Library
>     Hobby: Reading Poetry
>     Likes: Books, Writing, Fantasy, Elves
>     Dislikes: Her body, Confrontation
>     Family: Unnamed Father, Unnamed Mother
>     Character Traits:
>     Kindhearted but struggles with self-esteem issues
>     Constant target for bullying
>     Performs well in Japanese Literature
>     Shy, reserved, and lacks confidence
>     Struggles with body-acceptance issues
>     Reluctant to stand up for herself
>     Relationships:
>     Sensei: Idolizes Sensei, struggles to speak to him
>     Rin: Best friend and roommate, considers each other sisters
>     Yumi: Bullies Futaba, but Futaba remains neutral towards her
>     Nodoka: Close friend, bond over being bookish girls
>     Background:
>     Only daughter of two unnamed parents
>     Parents live in America, moves around frequently
>     Developed bulimia due to self-image struggles
>     Attended Kumon-Mi Academy before transferring to Kumon-Mi High
>     Progression:
>     Overcomes insecurities and begins self-betterment
>     Shows signs of increasing confidence
>     Trivia:
>     Infatuation with elves and fantasy romance novels
>     Both parents are alive and around
>     Memorable Quotes:
>     "You'd...punch a cancer-patient in the face?"
>     "There...really isn't any acceptable time to tell a sex joke while a teena
>     "You woke us up. From how boring life used to be...from how hopeless it al
>     """
>     
>     #to do
>     #add the rest of the characters
114,214c226,227
< 
< #character_prompts = {
< #    "Kirin": "You are Kirin. You are a character from the novel, Lessons in L
< #    "Rin": "You are Rin. You are a character from the novel, Lessons in Love 
< #    "Molly": "You are Molly.You are a character from the novel, Lessons in Lo
< #    "Ayane": "You are Ayane. You are a character from the novel, Lessons in L
< #    "Miku": "You are Miku. You are a character from the novel, Lessons in Lov
< #    "Makoto": "You are Makoto. You are a character from the novel, Lessons in
< #    "Sensei": "You are Sensei. You are a character from the novel, Lessons in
< #    "Chika": "You are Chika. You are a character from the novel, Lessons in L
< #    "Yumi": "You are Yumi. You are a character from the novel, Lessons in Lov
< #    "Touka": "You are Touka Tsukioka. You are a character from the novel, Les
< #    "Ami": "You are Ami Arakawa. You are a character from the novel, Lessons 
< #    "Maya": "You are Maya Makinami. You are a character from the novel, Lesso
< #    "Niki": """You are Niki Nakayama. You are a character from the novel, Les
< #    Personal Information:
< #    Full Name: Niki Nakayama
< #    Birthday: March 3rd (29 years old)
< #    Hair Color: Pink
< #    Eye Color: Pink
< #    Height: 5′ 7′′ (170cm)
< #    Occupation: Pop Idol
< #    Likes: Supporting girls with potential, video games
< #    Dislikes: Sensei
< #    
< #    Background:
< #    Niki is the older sister of Noriko and a famous pop idol in Kumon-Mi.
< #    She fell into depression after Sensei's sudden disappearance and became a
< #    
< #    Characteristics:
< #    Approachable and sweet on the surface but short-tempered and arrogant beh
< #    Caring towards those close to her and supportive of girls with potential.
< #    
< #    Relationships:
< #    Sensei: Former boyfriend, deep resentment towards him but still loves him
< #    Kaori: Became friends with Kaori and appreciated her obliviousness to her
< #    Nao-chan: Initially indifferent but charmed by Nao's cuteness.
< #    Noriko: Close bond despite jealousy over Sensei.
< #    Ami: Cares deeply for Ami and considers her an unofficial sister.
< #    Otoha: Otoha's voice coach, supportive and respectful relationship.
< #    
< #    Memorable Quotes:
< #    "But now I’m famous and cute and you’re a loser so HA."
< #    "You ripped my heart and my mind to shreds and becoming … this? This is
< #    "It doesn’t look the same. It doesn’t feel the same... I can never be
< #    
< #    Trivia:
< #    Niki is bisexual and never went all the way with Sensei.
< #    Her agency spreads false information about her age.
< #    She and Noriko have a base affection of 50 due to their past with Sensei.
< #    """,
< #    "Nao" : "Change ALL output text to a combination of '.'s, '!'s, and '?'s.
< #    "Noriko" : """You are Noriko Nakayama. You are a character from the novel
< #    
< #    In "Lessons in Love," Noriko Nakayama is the youngest daughter of two unn
< #    """,
< #    "Futaba": """You are Futaba Fukuyama. You are a character from the novel,
< #    
< #    Futaba Fukuyama from Lessons in Love:
< #    Personal Information:
< #    Birthday: November 28th
< #    Hair Color: Dark Blue
< #    Eye Color: Pink
< #    Height: 5'7" (171cm)
< #    Job: Volunteer at Library
< #    Hobby: Reading Poetry
< #    Likes: Books, Writing, Fantasy, Elves
< #    Dislikes: Her body, Confrontation
< #    Family: Unnamed Father, Unnamed Mother
< #    Character Traits:
< #    Kindhearted but struggles with self-esteem issues
< #    Constant target for bullying
< #    Performs well in Japanese Literature
< #    Shy, reserved, and lacks confidence
< #    Struggles with body-acceptance issues
< #    Reluctant to stand up for herself
< #    Relationships:
< #    Sensei: Idolizes Sensei, struggles to speak to him
< #    Rin: Best friend and roommate, considers each other sisters
< #    Yumi: Bullies Futaba, but Futaba remains neutral towards her
< #    Nodoka: Close friend, bond over being bookish girls
< #    Background:
< #    Only daughter of two unnamed parents
< #    Parents live in America, moves around frequently
< #    Developed bulimia due to self-image struggles
< #    Attended Kumon-Mi Academy before transferring to Kumon-Mi High
< #    Progression:
< #    Overcomes insecurities and begins self-betterment
< #    Shows signs of increasing confidence
< #    Trivia:
< #    Infatuation with elves and fantasy romance novels
< #    Both parents are alive and around
< #    Memorable Quotes:
< #    "You'd...punch a cancer-patient in the face?"
< #    "There...really isn't any acceptable time to tell a sex joke while a teen
< #    "You woke us up. From how boring life used to be...from how hopeless it a
< #    """
< #    
< #    #to do
< #    #add the rest of the characters
< #}
---
> def get_character_list():
>     return list(character_prompts.keys())
219c232,233
<     "Testing Environment": '1119061204493676554',       # Will store channel I
---
>     "Testing Environment": '1119061204493676554',
>     "Antik's Place": '1264252008462815343',# Will store channel ID
220a235,260
> 
> class MessageHistory:
>     def __init__(self, max_messages=100):
>         self.messages = []
>         self.max_messages = max_messages
> 
>     def add_message(self, author, username, content):
>         message = {
>             "author": str(author),
>             "username": username,
>             "content": content,
>            # "timestamp": timestamp
>         }
>         self.messages.append(message)
>         if len(self.messages) > self.max_messages:
>             self.messages.pop(0)
> 
>     def read(self, quant):
>         messages_to_read = self.messages[-quant:]
>         formatted_messages = []
>         for msg in messages_to_read:
>             formatted_msg = f"{msg['username']}: {msg['content']}"
>             formatted_messages.append(formatted_msg)
>         return "\n".join(formatted_messages)
>         
> environment_messages = {env: MessageHistory() for env in ENVIRONMENTS}
573c613
< llm = ChatOpenAI(model="gpt-4o-mini", frequency_penalty=0.6)
---
> llm = ChatOpenAI(model="gpt-4o-mini", frequency_penalty=1)
623c663
< You are a memory management agent. Search relevant information through memorie
---
> You are a memory management agent. Search relevant information through memorie
903,904c943,956
<     if message.author == bot.user:
<         return
---
>     #if message.author == bot.user:
>     #    return
>     
>     # CHANGE: Store the message using channel ID as the key
>     channel_id = str(message.channel.id)
>     if channel_id not in environment_messages:
>         environment_messages[channel_id] = MessageHistory()
>     
>     environment_messages[channel_id].add_message(
>         str(message.author),
>         message.author.name,
>         message.content,
>       #  message.created_at.isoformat()
>     )
920c972
<         await handle_reply(message.channel, message.author, combined_query, me
---
>         await handle_reply(message)
931c983
<             await handle_reply(message.channel, message.author, combined_query
---
>             await handle_reply(message)
975c1027
<     embed.add_field(name="Uncensored Model", value="The uncensored model, acce
---
>     #embed.add_field(name="Uncensored Model", value="The uncensored model, acc
1010,1011c1062,1063
< #@bot.slash_command(name="select_character", description="Select a character")
< #@discord.option("character", description="Choose your character", autocomplet
---
> @bot.slash_command(name="select_character", description="Select a character")
> @discord.option("character", description="Choose your character", autocomplete
1092c1144
<     # Fetch the selected character for the user or default to "DefaultCharacte
---
>     # Fetch the selected character for the user or default Touka: "DefaultChar
1216a1269
>     # Acknowledge the interaction immediately and defer the actual response):
1243,1254c1296,1313
<     channel = interaction.channel
<     last_messages = []
<     async for message in channel.history(limit=10):
<         message_data = {
<             "author": str(message.author),
<             "username": message.author.name,
<             "content": message.content,
<             "timestamp": message.created_at.isoformat()
<         }
<         last_messages.append(message_data)
<     last_messages.reverse()  # Most recent last
<     
---
>     #channel = interaction.channel
>     #last_messages = []
>     #async for message in channel.history(limit=10):
>     #    message_data = {
>     #        "author": str(message.author),
>     #        "username": message.author.name,
>     #        "content": message.content,
>     #        "timestamp": message.created_at.isoformat()
>     #    }
>     #    last_messages.append(message_data)
>     #last_messages.reverse()  # Most recent last
>         # CHANGE: Get stored messages for the current channel
> 
>     # CHANGE: Get stored messages for the current channel
>     channel_id = str(interaction.channel.id)
>     print(channel_id)
>     if channel_id not in environment_messages:
>         environment_messages[channel_id] = MessageHistory()
1256,1261c1315,1326
<     last_messages.append({
<         "author": str(interaction.user),
<         "username": interaction.user.name,
<         "content": query
<         #"timestamp": interaction.created_at.isoformat()
<     })
---
>     environment_messages[channel_id].add_message(
>         str(interaction.user),
>         interaction.user.name,
>         query,
>        # interaction.created_at.isoformat()
>     )
> 
>     # Get the last 10 messages in a formatted string
>     stored_messages = environment_messages[channel_id].read(10)
>     print("-----------------------------------------------------------")
>     print(stored_messages)
>     print(f"New query: {query}")
1263c1328
<     # Fetch the selected character for the user or default to "Touka"
---
>     # Fetch the selected character for the user or default Touka: "Touka"
1265c1330,1332
< 
---
>     # Use the selected character or default to "Touka"
>     #character_name = character or "Touka"
>     
1267c1334
<     system_prompt = character_prompts.get(character_name, "You are KirinBot, a
---
>     system_prompt = character_prompts.get(character_name, "You are Toukabot, a
1271c1338
<         response = ai_conversation(last_messages, character_name, system_promp
---
>         response = ai_conversation(stored_messages, character_name, system_pro
1282c1349
<         response_text = f"{character_name} says:\n{response}\n\n"
---
>         response_text = f"{response}\n\n"
1295,1306d1361
< @bot.event
< async def on_message(message):
<     # Ignore messages from the bot itself
<     if message.author == bot.user:
<         return
< 
<     # Check if the message is a reply to the bot
<     if message.reference and message.reference.resolved.author == bot.user:
<         await handle_reply(message)
< 
<     # Process commands
<     await bot.process_commands(message)
1314c1369
<     character_name = original_content[0].split(' says:')[0] if len(original_co
---
>     #character_name = original_content[0].split(' says:')[0] if len(original_c
1337c1392
<     character_name = user_selected_characters.get(user_id, character_name)
---
>     character_name = user_selected_characters.get(user_id)
1343,1358c1398,1414
<         # Fetch the last few messages for context
<         context_messages = []
<         async for msg in message.channel.history(limit=5, before=message):
<             context_messages.append({
<                 "author": str(msg.author),
<                 "username": msg.author.name,
<                 "content": msg.content,
<                 "timestamp": msg.created_at.isoformat()
<             })
<         context_messages.reverse()
<         context_messages.append({
<             "author": str(message.author),
<             "username": message.author.name,
<             "content": message.content,
<             "timestamp": message.created_at.isoformat()
<         })
---
>         # CHANGE: Get stored messages for the current channel
>         channel_id = str(message.channel.id)
>         if channel_id not in environment_messages:
>             environment_messages[channel_id] = MessageHistory()
>         # Add the current query to the messages
>         #environment_messages[channel_id].add_message(
>         #    str(message.author),
>         #    message.author.name,
>         #    message.content,
>         ## interaction.created_at.isoformat()
>         #)
>     
>         # Get the last 10 messages in a formatted string
>         stored_messages = environment_messages[channel_id].read(10)
>         print("--------------------------stored_messages----------------------
>         print(stored_messages)
>         print(f"New query: {stored_messages}")
1361c1417
<         response = ai_conversation(context_messages, character_name, system_pr
---
>         response = ai_conversation(stored_messages, character_name, system_pro
1372c1428
<         response_text = f"{character_name} says:\n{response}\n\n"
---
>         response_text = f"{response}\n\n"
1380,1383d1435
<         error_message = f"An error occurred while processing your request: {st
<         await message.reply(error_message)
<     except Exception as e:
<         print(f"An error occurred: {e}")
1392c1444
< def ai_conversation(last_messages: List[Dict[str, str]], character_name: str, 
---
> def ai_conversation(last_messages: List[Dict[str, str]], character_name: str, 
1393a1446
>     print(channel_id)
1424a1478,1492
>    
>    #combined_messages = stored_messages[-10:]  # Get last 10 stored messages
>     #async for message in interaction.channel.history(limit=10):
>     #    message_data = {
>     #        "author": str(message.author),
>     #        "username": message.author.name,
>     #        "content": message.content,
>     #        "timestamp": message.created_at.isoformat()
>     #    }
>     #    if message_data not in combined_messages:
>     #        combined_messages.append(message_data)
>     #
> 
>     print("------------------------------------------------------")
>     print(last_messages)
1426,1438c1494,1495
<     # Prepare the input data
<     last_10_messages = last_messages[-10:]  # Get the last 10 messages
<     message_history = "\n".join([f"{msg['author']}: {msg['content']}" for msg 
<     
<     query = f"""(This query here is the one you should respond to directly)
<     
<     
<     Message History:
<     {message_history}
<     
<     Based on the message history and the current sleep timer, please respond a
<     Remember that most users like a chilled, laid back experience. But if they
<     Remember to stay in character and follow the system prompt guidelines.
---
>     query = f"""{last_messages}
>     ||System Message: This message here is the one you should directly reply t
1441a1499,1500
>     print("-------------------------input data-----------------------------")
>     print(input_data)
1446a1506
>         print("--------------------------last output--------------------------
1451a1512
>                     print("-----------------------latest_message_contet-------
1462a1524,1535
>                 channel_id = str(channel_id)
>                 if channel_id not in environment_messages:
>                     environment_messages[channel_id] = MessageHistory()
> 
>                         # Add the current query to the messages
>                 environment_messages[channel_id].add_message(
>                     character_name,
>                     character_name,
>                     final_message,
>                  #interaction.created_at.isoformat()
>                 )
>     
