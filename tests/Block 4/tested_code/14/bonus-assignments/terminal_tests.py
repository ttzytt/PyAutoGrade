import subprocess

message = 'Hey, I just met you. And this is crazy!!! So here\'s my number... Now call me maybe :)'
words = message.split(' ')
for word in words:
    subprocess.run(['mkdir', word], stdout=subprocess.PIPE, cwd = 'spam')

