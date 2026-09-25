cask "font-snug-mono-nerd-font" do
  version "2.001.20260925.8367e61"
  sha256 "ac0c60f258fcdf457d9e2806c10916e943f00c53d13ea29dc10838822c568292"

  url "https://github.com/ralgozino/snug-mono/releases/download/v#{version}/SnugMono-NerdFont.zip"
  name "Snug Mono Nerd Font"
  desc "Snug Mono patched with the Nerd Fonts icons, at their natural width"
  homepage "https://github.com/ralgozino/snug-mono"

  livecheck do
    url :url
    strategy :github_latest
  end

  font "SnugMonoNerdFont-Regular.ttf"
  font "SnugMonoNerdFont-Bold.ttf"
  font "SnugMonoNerdFont-Italic.ttf"
  font "SnugMonoNerdFont-BoldItalic.ttf"
end
