from langchain.tools import tool

@tool("read_last_50_messages", return_direct=False)
def read_last_50_messages(environment: str) -> List[Dict[str, str]]:
    """
    Reads the last 50 messages from a specified Discord environment.

    Args:
    environment (str): The name of the environment to read messages from.
                       Must be either "Development Environment" or "Testing Environment".

    Returns:
    List[Dict[str, str]]: A list of dictionaries, each containing 'author' and 'content' of a message.
    """
    if environment not in ENVIRONMENTS:
        return [{
                    "error": f"Environment '{environment}' not found. Available environments are 'Development Environment' and 'Testing Environment'."}]

    channel_id = ENVIRONMENTS[environment]
    if channel_id is None:
        return [{"error": f"Channel for {environment} has not been set up yet."}]

    channel = bot.get_channel(channel_id)
    if not channel:
        return [{
                    "error": f"Channel for {environment} not found. It might have been deleted or the bot doesn't have access."}]

    messages = []
    for message in reversed(channel.history(limit=50).flatten()):  # Use flatten() to make it synchronous
        messages.append({
            "author": str(message.author),
            "content": message.content
        })

    return messages  # No need to reverse as we're already using reversed() above


# Custom tools for internet search and content processing
@tool("internet_search", return_direct=False)
def internet_search(query: str) -> str:
    """
    Performs an internet search using DuckDuckGo and returns the top 5 results.
    If no results are found, returns a 'No results found.' message.
    """
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=5)]
        return results if results else "No results found."


@tool("process_content", return_direct=False)
def process_content(url: str) -> str:
    """
    Fetches the content of the given URL, extracts text using BeautifulSoup, but only up to 10,000 words.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from paragraphs to avoid scripts, styles, etc.
    texts = soup.stripped_strings
    word_count = 0
    extracted_text = []

    for text in texts:
        words = text.split()
        word_count += len(words)
        if word_count > 6000:
            # If adding this text exceeds the limit, add only the words that fit
            words_needed = 6000 - (word_count - len(words))
            extracted_text.append(' '.join(words[:words_needed]))
            break
        extracted_text.append(text)

    # Join the extracted text with spaces, simulating natural reading
    return ' '.join(extracted_text)


# Global sleep variable
global_sleep = 1000


@tool("set_sleep", return_direct=False)
def set_sleep(duration: int) -> str:
    """
    Sets the global sleep duration.

    Args:
    duration (int): The duration to set the sleep timer to, in seconds.

    Returns:
    str: A confirmation message.
    """
    global global_sleep
    global_sleep = duration
    return f"Sleep timer set to {duration} seconds."


@tool("get_sleep", return_direct=False)
def get_sleep(query: str) -> int:
    """
    Gets the current global sleep duration.

    Returns:
    int: The current sleep duration in seconds.
    """
    return global_sleep


@tool("rag_query", return_direct=False)
def rag_query(query: str, chroma_db) -> str:
    """
    Queries the RAG database (Chroma instance) with the provided query, returning the top relevant documents.
    """
    # Embed the query using JinaAIEmbeddings
    embeddings = JinaAIEmbeddings()
    query_embedding = embeddings.embed_query(query)

    # Query the Chroma database with the embedded query
    search_results = chroma_db.search(query_embedding, k=5)  # Adjust 'k' based on how many results you want

    # Extract and format the results
    results = [doc.page_content for doc in search_results]
    formatted_results = "\n\n".join(results)

    return formatted_results if results else "No relevant documents found."


@tool("add_memory", return_direct=False)
def add_memory(memory: str, user_id=None, metadata: dict = None) -> str:
    '''
    Stores the provided text into long term storage
    '''
    memory_queue.put((m.add, (memory,), {"user_id": user_id, "metadata": metadata}))
    return "Memory addition task queued."


@tool("search_memory", return_direct=False)
def search_memory(query: str, user_id=None) -> str:
    '''
    Queries stored memories with the provided query, returning the relevant memories.
    '''
    # For search, we need to wait for the result
    result = m.search(query=query, user_id=user_id)
    return result


async def async_add_memory(memory: str, user_id=None, metadata: dict = None):
    await asyncio.to_thread(m.add, memory, user_id=user_id, metadata=metadata)


@tool("send_message", return_direct=False)
def send_message(environment: str, message: str) -> str:
    """
    Sends a message to the specified environment's Discord channel synchronously.

    Args:
    environment (str): The name of the environment to send the message to.
                       Must be either "Development Environment" or "Testing Environment".
    message (str): The content of the message to send.

    Returns:
    str: A confirmation message if successful, or an error message if failed.
    """
    if environment not in ENVIRONMENTS:
        return f"Error: Invalid environment '{environment}'. Available environments are 'Development Environment' and 'Testing Environment'."

    channel_id = ENVIRONMENTS[environment]

    # Assuming 'bot' is your Discord bot instance and is accessible here
    channel = bot.get_channel(int(channel_id))

    if not channel:
        return f"Error: Could not find channel for {environment}."

    try:
        # Use bot.loop.create_task to schedule the coroutine
        future = bot.loop.create_task(channel.send(message))
        # Wait for the task to complete
        bot.loop.run_until_complete(future)
        return f"Message sent to {environment} successfully."
    except Exception as e:
        return f"Error sending message to {environment}: {str(e)}"


tools = [internet_search, process_content, add_memory, search_memory, set_sleep, get_sleep]  # , rag_query]
# tools = [internet_search, process_content]