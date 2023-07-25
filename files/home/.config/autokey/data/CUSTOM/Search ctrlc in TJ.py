#keyboard.send_keys("<ctrl>+<shift>+<f1>") # Disable IME, set this shortcut in Fcitx 5

import os; exec(open(os.getenv('HOME') + '/bin/autokey-ctrl-c.py').read())

#system.exec_command('echo a; if ! pidof tagainijisho; then tagainijisho & sleep 1; fi') # Doesn't return
if system.exec_command('echo -n a; pidof tagainijisho || true') == 'a':
    import subprocess; subprocess.run("tagainijisho & sleep 1", shell=True)

system.exec_command("""echo a
xdotool windowactivate --sync $(wmctrl -lp|grep 'Tagaini Jisho$' |
awk '$3 > 100 { print $1 }') || exit 1; sleep .1
""")
# $3 < 100 for firejail instance, $3 > 100 for non-firejail instance

keyboard.send_keys("<ctrl>+l")
keyboard.send_keys("<ctrl>+r")
keyboard.send_keys("<ctrl>+v")
keyboard.send_keys("<ctrl>+o")
time.sleep(.2)

system.exec_command('echo a; xsel -b < /tmp/autokey-ctrl-c-clipboard-save')

system.exec_command('echo a; wmctrl -k on; wmctrl -k off')
