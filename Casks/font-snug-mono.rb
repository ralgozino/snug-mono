cask "font-snug-mono" do
  version "2.001.20260917"
  sha256 "4e52f498240eb7c778e0ed7fe1f2b41f9c3e32c5ab578fd4a088c5cf601ff56d"

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
