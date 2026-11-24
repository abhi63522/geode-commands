# Verify report

generated 2026-11-24 07:53 UTC

## Versions

| tool | arch-latest | debian-stable | fedora-latest | ubuntu-22.04 | ubuntu-24.04 |
|---|---|---|---|---|---|
| grep | grep (GNU grep) 3.12-modified | grep (GNU grep) 3.11 | grep (GNU grep) 3.12 | grep (GNU grep) 3.7 | grep (GNU grep) 3.11 |
| kitty | kitty 0.51.1 created by Kovid Goyal | kitty 0.41.1 created by Kovid Goyal | kitty 0.48.2 created by Kovid Goyal | kitty 0.21.2 created by Kovid Goyal | kitty 0.32.2 created by Kovid Goyal |
| tmux | tmux 3.8 | tmux 3.5a | tmux 3.8 | tmux 3.2a | tmux 3.4 |

## Flag check

- grep documented but not in --help: none
- grep real flags not covered yet: --basic-regexp --before-context --binary --binary-files --byte-offset --color --colour --context --dereference-recursive --devices --directories --exclude --exclude-dir --exclude-from --file --files-without-match --fixed-strings --group-separator --help --include --initial-tab --label --line-buffered --line-regexp --max-count --no-filename --no-group-separator --no-ignore-case --no-messages --null --null-data --perl-regexp --quiet --regexp --silent --text --version --with-filename -B -C -D -F -G -H -I -L -NUM -P -R -T -U -V -Z -a -b -d -e -f -h -m -q -s -x -z

## Entries

### OK grep -i `grep-i` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
Banana
```

### OK grep -n `grep-n` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
1:apple
4:apple pie
```

### OK grep -v `grep-v` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
Banana
cherry
app
```

### OK grep -c `grep-c` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
2
```

### OK grep -w `grep-w` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
app
```

### OK grep -E `grep-E` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
Banana
cherry
```

### OK grep -o `grep-o` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
pp
pp
pp
```

### OK grep -r `grep-r` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
d/a.txt:cherry
d/b.txt:cherry
```

### OK grep -l `grep-l` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
d/a.txt
d/b.txt
```

### OK grep -A `grep-A` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
cherry
apple pie
```

### OK kitty: new window `kitty-new-window` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK kitty: new tab `kitty-new-tab` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK kitty: next tab `kitty-next-tab` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK kitty: next window `kitty-next-window` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK kitty: close window `kitty-close-window` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK tmux: new window `tmux-new-window` (tested)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
2
```

### CHECK tmux: split left/right `tmux-split-h` (tested)
- binding: arch-latest=missing, debian-stable=missing, fedora-latest=missing, ubuntu-22.04=ok, ubuntu-24.04=missing
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
0:40
1:39
```

### OK tmux: next window `tmux-next-window` (tested)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
1
```

### OK tmux: detach `tmux-detach` (mapped)
- binding: arch-latest=ok, debian-stable=ok, fedora-latest=ok, ubuntu-22.04=ok, ubuntu-24.04=ok

### OK tmux capture-pane -p `tmux-capture-pane` (tested)
- output same on all 5 distros

on arch-latest, debian-stable, fedora-latest, ubuntu-22.04, ubuntu-24.04:
```
1
```
