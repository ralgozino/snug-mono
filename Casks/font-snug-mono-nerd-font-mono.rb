cask "font-snug-mono-nerd-font-mono" do
  version "2.001.20260917"
  sha256 "449d433d93de0ed0f91793ca36db949e2e07f6a64cfe427c9939968e63c559c2"

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
