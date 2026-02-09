$sqlContent = Get-Content 'C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\map_upstream.sql' -Raw
$sqlMatches = [regex]::Matches($sqlContent, 'VALUES \((\d+),')
$sqlIds = @{}
foreach ($m in $sqlMatches) {
    $sqlIds[$m.Groups[1].Value] = 1
}

$csv = Import-Csv 'C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder\Source_Data\map_upstream.csv'
Write-Host "Total CSV rows: $($csv.Count)"
Write-Host "Total unique SQL app IDs: $($sqlIds.Count)"

foreach ($row in $csv) {
    if (-not $sqlIds.ContainsKey($row.id)) {
        Write-Host "MISSING: $($row.id) - $($row.name)"
    }
}
