cask "font-snug-mono-nerd-font" do
  version "2.001.20260917"
  sha256 "4a6905bf2eea05d882a5dbb0fd42cd13f5bb66b523700d32f6c350c6d5d3abbd"

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
