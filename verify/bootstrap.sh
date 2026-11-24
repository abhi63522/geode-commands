#!/bin/sh
# runs inside each distro container: install tools, then record real results
if command -v apt-get >/dev/null 2>&1; then
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -qq
  apt-get install -y -qq --no-install-recommends python3 grep tmux ca-certificates
  apt-get install -y -qq --no-install-recommends kitty || echo "KITTY INSTALL FAILED"
elif command -v dnf >/dev/null 2>&1; then
  dnf install -y -q python3 grep tmux
  dnf install -y -q kitty || echo "KITTY INSTALL FAILED"
elif command -v pacman >/dev/null 2>&1; then
  pacman -Sy --noconfirm --needed python grep tmux
  pacman -S --noconfirm --needed kitty || echo "KITTY INSTALL FAILED"
fi
mkdir -p out
python3 verify/run.py "$NAME"
