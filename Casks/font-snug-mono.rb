cask "font-snug-mono" do
  version "2.001.20261116.aa45a27"
  sha256 "2a45d84fc3138ce11234db41fa76a363e7181067571993405c9addebc02bf6ee"

  url "https://github.com/ralgozino/snug-mono/releases/download/v#{version}/SnugMono.zip"
  name "Snug Mono"
  desc "Atkinson Hyperlegible Mono with a narrower character cell"
  homepage "https://github.com/ralgozino/snug-mono"

  livecheck do
    url :url
    strategy :github_latest
  end

  font "SnugMono[wght].ttf"
  font "SnugMono-Italic[wght].ttf"
end
