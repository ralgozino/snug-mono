cask "font-snug-mono" do
  version "2.001.20260917"
  sha256 "6f0fab7ff3cce76116cb016353ad3342836486f52cec38e3263ea8ee79d4bce5"

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
