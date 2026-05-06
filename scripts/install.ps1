param(
  [string]$Destination = "$HOME\.codex\skills\movie-companion"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

if (Test-Path $Destination) {
  throw "Destination already exists: $Destination"
}

New-Item -ItemType Directory -Force (Split-Path $Destination) | Out-Null
New-Item -ItemType Directory -Force $Destination | Out-Null

$items = @("SKILL.md", "agents", "references", "scripts", "examples", "README.md", "LICENSE")
foreach ($item in $items) {
  $source = Join-Path $RepoRoot $item
  if (Test-Path $source) {
    Copy-Item -Recurse -Force $source (Join-Path $Destination $item)
  }
}

Write-Host "Installed movie-companion to $Destination"
Write-Host "Restart Codex to pick up new skills."
