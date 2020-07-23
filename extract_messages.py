# extract messages for preprocessing
# started as same script I wrote for fb_message_identifier

import json
import pickle


jeremy = "Jeremy Thaller"
sarah = "Sarah Ritzmann"
sarah_json1 = "data/SarahRitzmann_qZoMJVMdAQ/message_1.json"
sarah_json2 = "data/SarahRitzmann_qZoMJVMdAQ/message_2.json"
true = True


# It might work better if you collapse the conversation so it's always back
# and forth. Otherwise you won't get conversational sides. Maybe that doesn't
# actually matter, but its worth exploring.
# return a dict like {person1: str, person2: str, person1: str, ...}
def collapseSentences(name, data):
    conv = []
    message_cache = ''
    for i in range(len(data["messages"])-1):
        prev_name = name
        try:
            if data["messages"][i]["sender_name"] == prev_name:
                if message_cache[-1] not in {'.', '!', '?'}:
                    message_cache += '. ' + data["messages"][i]["content"]
                else:
                    message_cache += ' ' + data["messages"][i]["content"]
            else:  # data["messages"][i]["sender_name"] != prev_name:
                # new person, add the cached message
                conv.append(message_cache)
                message_cache = data["messages"][i]["content"]
                sender = data["messages"][i]["sender_name"]
                prev_name = sender
        except KeyError:
            pass
    return conv


def reverseConversation(conv):
    return conv[::-1]


# we need to create conversation pairs with a target: response
# I might put this in preprocessing instead
# def extractSentence(name, data):
#     qa_pairs = []
#     for block in data["messages"]:
#         try:
#             if block["sender_name"] == name:
#                 # print(block["content"])
#                 inputLine = block["content"]
#         except KeyError:
#             pass
#         try:
#             if block["sender_name"] == name:
#                 targetLine = block["content"]
#         except KeyError:       
#             pass
#         if inputLine and targetLine:
#             qa_pairs.append([inputLine, targetLine])
#     return qa_pairs


# ---- Sarah ----- #
# open file, scrape messages and add to list of lists.
# each list is a string. contains all the messages sent
# consecutively by someone
with open(sarah_json1, "r", encoding="ISO-8859-1") as read_file:
    data = json.load(read_file)
    sentences = collapseSentences(sarah, data)
    sentences = reverseConversation(sentences)
    # print(sentences[:20])

# with open(sarah_json2, "r") as read_file:
#     data = json.load(read_file)
#     extractSentence(sarah, data)

# save it as a pickle
with open('sarah.pickle', 'wb') as handle:
    pickle.dump(sentences, handle, protocol=pickle.HIGHEST_PROTOCOL)


# with open('sarah.pickle', 'rb') as handle:
#     b = pickle.load(handle)

# print(messages_dict == b)


# print(f"Rohan: {messages_dict[rohan][-3:]}")
# print(f"Thomas: {messages_dict[thomas][-3:]}")
# print(f"Mike: {messages_dict[mike][-3:]}")
# print(f"Jeremy: {messages_dict[jeremy][-3:]}")



# Structure. Note, when a picture is sent, it doesn't say "content: str", it says "photos: [{uri: ,creation_timestamp: }]".
# It's a dict in an array. I'm ignoring pictures, anyway, so this makes it easy.
#
# sample_dict = {
#   "participants": [
#     {
#       "name": "Zeran Ji"
#     },
#     {
#       "name": "Jeremy Thaller"
#     }
#   ],
#   "messages": [
#     {
#       "sender_name": "Jeremy Thaller",
#       "timestamp_ms": 1587763611349,
#       "content": "Lolol",
#       "type": "Generic"
#     },
#     {
#       "sender_name": "Zeran Ji",
#       "timestamp_ms": 1587763579045,
#       "photos": [
#         {
#           "uri": "messages/inbox/ZeranJi_XXnwiz4w7g/photos/90541292_539096823676084_7598840419950002176_n_1226093940931953.png",
#           "creation_timestamp": 1587763578
#         }
#       ],
#       "type": "Generic"
#     }
#       ],
#   "title": "Zeran Ji",
#   "is_still_participant": true,
#   "thread_type": "Regular",
#   "thread_path": "inbox/ZeranJi_XXnwiz4w7g"
# }

# # print(sample_dict["messages"][0]["content"])
# for block in sample_dict["messages"]:
#     if block["sender_name"] == 'Jeremy Thaller':
#         print(block["content"])
