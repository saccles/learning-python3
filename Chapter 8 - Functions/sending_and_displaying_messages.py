import message_functions

# Lists to pass to imported functions.
messages = ['hey', 'how are you?', 'hi', 'lol', 'haha']
sent_messages = []

message_functions.send_messages(messages, sent_messages)
message_functions.show_sent_messages(sent_messages)



