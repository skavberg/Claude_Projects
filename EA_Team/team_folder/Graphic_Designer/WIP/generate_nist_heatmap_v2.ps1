
# NIST CSF Coverage Heatmap Generator v2
# Uses Azure OpenAI GPT Image 1.5 - debugging API version

$ErrorActionPreference = "Stop"

$apiKey = [System.Environment]::GetEnvironmentVariable('AZURE_OPENAI_API_KEY','User')
$endpoint = "https://aif-eus2-clops-prd-01.cognitiveservices.azure.com"
$deployment = "gpt-image-1.5"

$baseDir = "C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder"
$wipDir = "$baseDir\Graphic_Designer\WIP"
$draftDir = "$baseDir\Graphic_Designer\Draft"
$sourceDir = "$baseDir\Source_Data"

# Detailed image generation prompt
$prompt = @"
Create a professional corporate executive presentation slide showing a NIST Cybersecurity Framework Coverage Heatmap for Cenovus Energy.

White background. Title at top: Cenovus Energy - NIST CSF Security Coverage Assessment in dark slate color #244C5A. Subtitle: 63 Security Applications February 2026 in gray.

Show 5 large rounded rectangle tiles arranged in a horizontal row in the center. Each tile shows a NIST CSF function with its application count, percentage, and coverage rating. The tiles from left to right are:

1. IDENTIFY tile - amber yellow #F1BE48 background - shows ID, number 8, 12.7%, ADEQUATE rating
2. PROTECT tile - apple green #78BE21 background - shows PR, number 38, 60.3%, STRONG rating
3. DETECT tile - jade green #009B77 background - shows DE, number 15, 23.8%, STRONG rating
4. RESPOND tile - amber yellow #F1BE48 background - shows RS, number 7, 11.1%, MODERATE rating
5. RECOVER tile - sienna red #CF4520 background - shows RC, number 4, 6.3%, CRITICAL GAP rating

The numbers 8, 38, 15, 7, 4 should be very large and prominent in each tile. Use white text on dark backgrounds and dark text on yellow backgrounds.

Include a legend at bottom showing: Green = Strong Coverage, Amber = Adequate/Moderate, Red = Critical Gap.

Footer text: Source EA Cybersecurity Assessment NIST CSF v2.0

Clean professional corporate dashboard style. No decorative elements. Subtle drop shadows on tiles. Suitable for C-suite executive presentation.
"@

# Try multiple API versions
$apiVersions = @("2025-04-01-preview", "2024-12-01-preview", "2024-10-01-preview", "2024-06-01", "2024-02-01", "2024-02-15-preview")

foreach ($apiVersion in $apiVersions) {
    Write-Output ""
    Write-Output "=== Trying API version: $apiVersion ==="

    # Try with response_format
    $body = @{
        prompt = $prompt
        size = "1536x1024"
        quality = "high"
        n = 1
        response_format = "b64_json"
    } | ConvertTo-Json -Depth 5

    $url = "$endpoint/openai/deployments/$deployment/images/generations?api-version=$apiVersion"

    try {
        $headers = @{
            "api-key" = $apiKey
            "Content-Type" = "application/json"
        }

        Write-Output "Attempting with response_format=b64_json..."
        $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body -TimeoutSec 180

        Write-Output "SUCCESS with API version: $apiVersion"

        # Save full response
        $response | ConvertTo-Json -Depth 10 | Out-File "$sourceDir\nist_heatmap_response.json" -Encoding UTF8

        # Check response structure
        if ($response.data) {
            Write-Output "Response has 'data' field with $($response.data.Count) items"

            if ($response.data[0].b64_json) {
                $b64Data = $response.data[0].b64_json
                Write-Output "Found b64_json data, length: $($b64Data.Length)"

                $imageBytes = [Convert]::FromBase64String($b64Data)
                $wipPath = "$wipDir\nist_csf_heatmap.png"
                [IO.File]::WriteAllBytes($wipPath, $imageBytes)
                Write-Output "Image saved: $wipPath ($([math]::Round($imageBytes.Length / 1024)) KB)"

                $draftPath = "$draftDir\DRAFT_nist_csf_heatmap_2026-02-09.png"
                Copy-Item $wipPath $draftPath -Force
                Write-Output "Draft saved: $draftPath"
                Write-Output "=== GENERATION COMPLETE ==="
                exit 0

            } elseif ($response.data[0].url) {
                Write-Output "Found URL-based response: $($response.data[0].url)"
                $imgUrl = $response.data[0].url
                $wipPath = "$wipDir\nist_csf_heatmap.png"
                Invoke-WebRequest -Uri $imgUrl -OutFile $wipPath -TimeoutSec 60
                Write-Output "Image downloaded: $wipPath"

                $draftPath = "$draftDir\DRAFT_nist_csf_heatmap_2026-02-09.png"
                Copy-Item $wipPath $draftPath -Force
                Write-Output "Draft saved: $draftPath"
                Write-Output "=== GENERATION COMPLETE ==="
                exit 0
            } else {
                Write-Output "Data item keys: $($response.data[0].PSObject.Properties.Name -join ', ')"
            }
        } else {
            Write-Output "Response keys: $($response.PSObject.Properties.Name -join ', ')"
            # Save raw response for debugging
            $response | ConvertTo-Json -Depth 10 | Write-Output
        }
        break

    } catch {
        $statusCode = ""
        $errorBody = ""
        if ($_.Exception.Response) {
            $statusCode = $_.Exception.Response.StatusCode
            try {
                $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
                $errorBody = $reader.ReadToEnd()
            } catch {}
        }
        Write-Output "FAILED - Status: $statusCode - $($_.Exception.Message)"
        if ($errorBody) {
            Write-Output "Error body: $errorBody"
        }
    }
}

# If we got here without success via response_format, try without it
Write-Output ""
Write-Output "=== Trying without response_format parameter ==="

foreach ($apiVersion in $apiVersions) {
    Write-Output ""
    Write-Output "--- Trying API version: $apiVersion (no response_format) ---"

    $body = @{
        prompt = $prompt
        size = "1536x1024"
        quality = "high"
        n = 1
    } | ConvertTo-Json -Depth 5

    $url = "$endpoint/openai/deployments/$deployment/images/generations?api-version=$apiVersion"

    try {
        $headers = @{
            "api-key" = $apiKey
            "Content-Type" = "application/json"
        }

        $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body -TimeoutSec 180

        Write-Output "SUCCESS with API version: $apiVersion (no response_format)"

        $response | ConvertTo-Json -Depth 10 | Out-File "$sourceDir\nist_heatmap_response.json" -Encoding UTF8

        if ($response.data) {
            if ($response.data[0].b64_json) {
                $b64Data = $response.data[0].b64_json
                $imageBytes = [Convert]::FromBase64String($b64Data)
                $wipPath = "$wipDir\nist_csf_heatmap.png"
                [IO.File]::WriteAllBytes($wipPath, $imageBytes)
                Write-Output "Image saved: $wipPath ($([math]::Round($imageBytes.Length / 1024)) KB)"

                $draftPath = "$draftDir\DRAFT_nist_csf_heatmap_2026-02-09.png"
                Copy-Item $wipPath $draftPath -Force
                Write-Output "Draft saved: $draftPath"
                Write-Output "=== GENERATION COMPLETE ==="
                exit 0

            } elseif ($response.data[0].url) {
                $imgUrl = $response.data[0].url
                $wipPath = "$wipDir\nist_csf_heatmap.png"
                Invoke-WebRequest -Uri $imgUrl -OutFile $wipPath -TimeoutSec 60
                Write-Output "Image downloaded: $wipPath"

                $draftPath = "$draftDir\DRAFT_nist_csf_heatmap_2026-02-09.png"
                Copy-Item $wipPath $draftPath -Force
                Write-Output "Draft saved: $draftPath"
                Write-Output "=== GENERATION COMPLETE ==="
                exit 0
            } else {
                Write-Output "Data item keys: $($response.data[0].PSObject.Properties.Name -join ', ')"
            }
        } else {
            Write-Output "Response keys: $($response.PSObject.Properties.Name -join ', ')"
        }
        break

    } catch {
        $statusCode = ""
        $errorBody = ""
        if ($_.Exception.Response) {
            $statusCode = $_.Exception.Response.StatusCode
            try {
                $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
                $errorBody = $reader.ReadToEnd()
            } catch {}
        }
        Write-Output "FAILED - Status: $statusCode - $($_.Exception.Message)"
        if ($errorBody) {
            Write-Output "Error body: $errorBody"
        }
    }
}

Write-Output ""
Write-Output "=== All attempts exhausted ==="
exit 1
