cask "font-snug-mono-nerd-font-mono" do
  version "2.001.20260925.8367e61"
  sha256 "a57def3ec5919ae45ceaa4d1a0fea26f05be689dace5e9ce9d3879684581eabf"

  url "https://github.com/ralgozino/snug-mono/releases/download/v#{version}/SnugMono-NerdFontMono.zip"
  name "Snug Mono Nerd Font Mono"
  desc "Snug Mono patched with the Nerd Fonts icons, each icon in one cell"
  homepage "https://github.com/ralgozino/snug-mono"

  livecheck do
    url :url
    strategy :github_latest
  end

  font "SnugMonoNerdFontMono-Regular.ttf"
  font "SnugMonoNerdFontMono-Bold.ttf"
  font "SnugMonoNerdFontMono-Italic.ttf"
  font "SnugMonoNerdFontMono-BoldItalic.ttf"
end
