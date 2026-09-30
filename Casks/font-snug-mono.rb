cask "font-snug-mono" do
  version "2.001.20260930.e87273a"
  sha256 "fa7ac4b9f2ae3527852d1bf22c4ac8cd5f143f015c7677e0851e5b6a65cddd1c"

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
