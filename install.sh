#!/bin/sh
# Install Snug Mono for the current user.
set -e
cd "$(dirname "$0")"

case "$(uname -s)" in
  Darwin) dir="$HOME/Library/Fonts" ;;
  Linux)  dir="$HOME/.local/share/fonts" ;;
  *)      echo "Unsupported system: $(uname -s)" >&2; exit 1 ;;
esac

mkdir -p "$dir"
cp fonts/SnugMono*.ttf "$dir"
[ "$(uname -s)" = Linux ] && command -v fc-cache >/dev/null && fc-cache -f "$dir"

echo "Installed Snug Mono in $dir"
echo "Set your terminal or editor font to: Snug Mono"
