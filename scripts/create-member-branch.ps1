param(
    [Parameter(Mandatory = $true)]
    [string]$MemberName
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$sanitizedName = $MemberName.Trim().ToLower() -replace "[^a-z0-9-]", "-"
$branchName = "team/$sanitizedName"

git checkout main
git checkout -b $branchName

Write-Host "Created branch $branchName"
Write-Host "Publish it with: git push -u origin $branchName"
