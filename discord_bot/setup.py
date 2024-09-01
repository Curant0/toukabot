@bot.event
async def on_ready():
    # Fetch global application commands
    app_info = await bot.application_info()  # Get application info
    global_commands = await bot.http.get_global_commands(app_info.id)
    await load_extensions()    
    print(f'{bot.user} is connected and ready to roll!')
    # The new incantation to ensure the user_preferences table exists
    with sqlite3.connect('token_usage.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_preferences (
                user_id INTEGER PRIMARY KEY,
                ephemeral_preference BOOLEAN DEFAULT FALSE
            );
        """)
        conn.commit()

    print(f'{bot.user} is connected and old commands have been cleared.')

