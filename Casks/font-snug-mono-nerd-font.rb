cask "font-snug-mono-nerd-font" do
  version "2.001.20260930.4c0e719"
  sha256 "95a545af130ec9dd84d24750389ef1240f0ac59d8075ac7154a7d4334e80a7cb"

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
