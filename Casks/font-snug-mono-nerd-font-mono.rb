cask "font-snug-mono-nerd-font-mono" do
  version "2.001.20260917"
  sha256 "4a6905bf2eea05d882a5dbb0fd42cd13f5bb66b523700d32f6c350c6d5d3abbd"

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
