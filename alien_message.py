# Reverse Cipher
import time
enterGalaticMessage = '''This is the message to all the earthlings out there. The temperature of the Earth
is continuously rising. You must take a decisive action if you are to save the planet Earth. We
are ready to provide you with whatever help you may require. Just contact one of us that is roaming
the Earth in a human body. Thank you. Best of luck for your endeavour.'''

alienMessage = ''

i = len(enterGalaticMessage) - 1

while i >= 0:
	alienMessage = alienMessage + enterGalaticMessage[i]
	i = i - 1

print('Alien Message....\n')
time.sleep(3)

print(alienMessage)
print('\n')


converted = ''

i = len(alienMessage) - 1

while i >= 0:
	converted = converted + alienMessage[i]
	i = i - 1

print('Message converting into Human Readibility..\n')
time.sleep(2)
print(converted)