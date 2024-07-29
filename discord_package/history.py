class MessageHistory:
    def __init__(self, max_messages=100):
        self.messages = []
        self.max_messages = max_messages

    def add_message(self, author, username, content):
        message = {
            "author": str(author),
            "username": username,
            "content": content,
           # "timestamp": timestamp
        }
        self.messages.append(message)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def read(self, quant):
        messages_to_read = self.messages[-quant:]
        formatted_messages = []
        for msg in messages_to_read:
            formatted_msg = f"{msg['username']}: {msg['content']}"
            formatted_messages.append(formatted_msg)
        return "\n".join(formatted_messages)

