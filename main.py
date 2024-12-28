import emoji

# text with emoji
text_with_emoji = "I love Python! 😊🐍"

# convert emoji in text
emoji_to_text = emoji.demojize(text_with_emoji)

print("Original text: ", text_with_emoji)
print("Text converted: ", emoji_to_text)

