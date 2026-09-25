cask "font-snug-mono" do
  version "2.001.20260925.8367e61"
  sha256 "abbab6d669ede454fa0fc62fdaba7c6a2fe442c1c967633f37b81dcf605f23b8"

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
