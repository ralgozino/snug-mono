cask "font-snug-mono-nerd-font-mono" do
  version "2.001.20260930.4c0e719"
  sha256 "e35fbcf5b9b6fd88d9cf4d17cd2cb141e5ec2bbb38f692f533e487f7fc5aea81"

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
