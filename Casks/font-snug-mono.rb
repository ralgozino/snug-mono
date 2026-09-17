cask "font-snug-mono" do
  version "2.001.20260917.4e21edf"
  sha256 "a9d254045eb1340b20d680b83ceda500227ea01c658583966baf889eab65a6ad"

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
