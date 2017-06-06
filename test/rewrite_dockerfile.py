import os
import sys

IMAGE_ID = os.environ.get('IMAGE_ID')
if not IMAGE_ID:
    print('Unable to find IMAGE_ID variable.')
    sys.exit(1)

dockerfile = os.path.join(os.path.split(__file__)[0], 'Dockerfile')

if not os.path.isfile(dockerfile):
    print('Dockerfile at {} does not exist.'.format(dockerfile))
    sys.exit(1)

with open(dockerfile, 'rb') as f:
    buf = f.read()

s = buf.decode()
s = s.format(IMAGE_ID=IMAGE_ID)

print('Writing Dockerfile:')
print('-' * 80)
print(s)
print('-' * 80)

with open(dockerfile, 'wb') as f:
    f.write(s.encode())

print('Done replacing test dockerfile.')

sys.exit(0)
