from __future__ import print_function
try:
  input = raw_input
except NameError:
  pass

def msg_translator(msg):
  msg = msg.upper()
  translatable_words = {"MSG": "message",
                        "LOL": "lots of laughs",
                        "ROTFL": "rolling on the floor laughing"}
  for key in translatable_words:
    if msg.find(key) != -1:
      msg = msg.replace(key,translatable_words[key])
  msg = msg.capitalize()
  return msg


message = input("Please provide a message ")
full_msg = msg_translator(message)
print("Translated message: %s" % full_msg)