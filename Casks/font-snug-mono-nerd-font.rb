cask "font-snug-mono-nerd-font" do
  version "2.001.20260917"
  sha256 "5c23dbe022ff79f8cea2f234e77f335147d9207fe1cd10246d69220eeb95d951"

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
