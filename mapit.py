import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '1950', 'Charleston', 'Rd.']

# check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '1950', 'Charleston', 'Rd.'] -> '1950 Charleston Rd.'
    address = ' '.join(sys.argv[1:])
else:
    address  = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
