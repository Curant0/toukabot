# The support message with the 'Buy Me a Coffee' link
import discord

support_message = (
    "Looking to power up? Your support accelerates our journey into the future of AI. "
    "Top up your token balance and keep the code compiling by buying me a coffee! "
    "For each dollar, you'll receive an equal amount in tokens to continue interacting with the bot. "
    "Click here to support and energize our progress: https://www.buymeacoffee.com/womp_womp_ "
    "Your contribution is the caffeine in our coding coffee. Thank you for brewing success with us!"
)


class CharacterSelectView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Assuming character_prompts is a dictionary with all character options
        # Ensure the number of options is within Discord's limits
        options = [
            discord.SelectOption(label=character, description=f"Select {character}")
            for character in list(character_prompts.keys())[:25]  # Limit to 25 options
        ]

        # Add the Select component with the limited number of options
        self.add_item(discord.ui.Select(placeholder="Select your character...", options=options))

    @discord.ui.select()
    async def select_character(self, select: discord.ui.Select, interaction: discord.Interaction):
        # Your existing logic for handling character selection...
        selected_character = select.values[0]
        # Store the user's selected character
        user_selected_characters[interaction.user.id] = selected_character
        await interaction.response.send_message(f"You have selected {selected_character}!", ephemeral=True)