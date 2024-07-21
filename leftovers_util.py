"""
# Function to load .txt documents from a directory
def load_text_documents(directory):
    documents = []
    for filepath in glob.glob(f"{directory}/*.txt"):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            # Ensure each document is an instance of the Document class with page_content set
            documents.append(Document(page_content=content))
    return documents
"""

"""
#stuff gets long, need to truncate.
def truncate_messages(messages, max_tokens=MAX_TOKENS):
    total_tokens = 0
    truncated_messages = []
    for message in messages:
        message_tokens = count_tokens(message.content)
        if total_tokens + message_tokens <= max_tokens:
            truncated_messages.append(message)
            total_tokens += message_tokens
        else:
            # Truncate this message
            remaining_tokens = max_tokens - total_tokens
            words = message.content.split()
            truncated_content = ' '.join(words[:remaining_tokens])
            truncated_messages.append(HumanMessage(content=truncated_content))
            break  # No more messages can be added
    return truncated_messages
"""

"""
def AI_truncate_messages(messages, max_tokens=16000):
    total_tokens = 0
    truncated_messages = []

    for message in messages:
        message_tokens = count_tokens(message.content)
        if total_tokens + message_tokens > max_tokens:
            # Calculate how many tokens we can include in this message
            remaining_tokens = max_tokens - total_tokens
            if remaining_tokens > 0:
                # Truncate the message content to fit the remaining token count
                words = message.content.split()
                truncated_content = ' '.join(words[:remaining_tokens])
                truncated_message = HumanMessage(content=truncated_content)
                truncated_messages.append(truncated_message)
            break  # Stop processing further messages
        else:
            truncated_messages.append(message)
            total_tokens += message_tokens

    return truncated_messages
"""


