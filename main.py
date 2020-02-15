import re
import textwrap

ital = re.compile(r'<span class="CharOverride-10">([\w\s&,]+)</span>')
data = open('input.html').read()

for line in data.splitlines():
    if line == '':
        continue

    if line.startswith('#'):
        print(line)
        print('')
        continue

    line = line.replace('<span class="CharOverride-7">', '')
    line = line.replace('&amp;', '&')

    if 'CharOverride-10' in line:

        matches = re.findall(ital, line)
        assert matches

        for match in matches:
            orig = '<span class="CharOverride-10">{}</span>'.format(match)
            dest = '*{}*'.format(match)
            line = line.replace(orig, dest)

    line = line.replace('</span></p>', '')
    line = line.replace('</span>', '')
    wrapped = textwrap.wrap(line)
    print('\n'.join(wrapped))
    print('')

