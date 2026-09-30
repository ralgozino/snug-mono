cask "font-snug-mono" do
  version "2.001.20260930.4c0e719"
  sha256 "276428e646b0505790a00d23ca2c501a3e9b0e97c01d0f64c3dba564f51df465"

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
