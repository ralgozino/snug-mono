cask "font-snug-mono-nerd-font-mono" do
  version "2.001.20260930.e87273a"
  sha256 "548240670276c1c89c982b941cdb270a1268d6a67c4ca4e8bc00bbc2fc667cb8"

  url "https://github.com/ralgozino/snug-mono/releases/download/v#{version}/SnugMono-NerdFontMono.zip"
  name "Snug Mono Nerd Font Mono"
  desc "Snug Mono patched with the Nerd Fonts icons, each icon in one cell"
  homepage "https://github.com/ralgozino/snug-mono"

  livecheck do
    url :url
    strategy :github_latest
  end

  font "SnugMonoNerdFontMono-Regular.ttf"
  font "SnugMonoNerdFontMono-Bold.ttf"
  font "SnugMonoNerdFontMono-Italic.ttf"
  font "SnugMonoNerdFontMono-BoldItalic.ttf"
end
