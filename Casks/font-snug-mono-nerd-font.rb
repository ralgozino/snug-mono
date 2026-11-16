cask "font-snug-mono-nerd-font" do
  version "2.001.20261116.aa45a27"
  sha256 "53c3635c41b7ff5ca2a7fc4df222ed69d1b3d874004e93c38abebee56a8a02e3"

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
