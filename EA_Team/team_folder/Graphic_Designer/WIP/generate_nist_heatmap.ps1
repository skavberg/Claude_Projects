
# NIST CSF Coverage Heatmap Generator
# Uses Azure OpenAI GPT Image 1.5 to generate a professional corporate heatmap

$ErrorActionPreference = "Stop"

# Configuration
$apiKey = [System.Environment]::GetEnvironmentVariable('AZURE_OPENAI_API_KEY','User')
$endpoint = "https://aif-eus2-clops-prd-01.cognitiveservices.azure.com"
$deployment = "gpt-image-1.5"
$apiVersion = "2025-04-01-preview"

$baseDir = "C:\Users\skavbr\Documents\Claude_Projects\EA_Team\team_folder"
$wipDir = "$baseDir\Graphic_Designer\WIP"
$draftDir = "$baseDir\Graphic_Designer\Draft"
$sourceDir = "$baseDir\Source_Data"

# Detailed image generation prompt
$prompt = @"
Create a professional corporate executive presentation slide image showing a NIST Cybersecurity Framework Coverage Heatmap for Cenovus Energy.

LAYOUT AND DESIGN:
- White background, clean corporate style suitable for C-suite executive presentation
- Title at top: "Cenovus Energy - NIST CSF Security Coverage Assessment" in dark slate color (#244C5A), bold, large font
- Subtitle below: "63 Security Applications | February 2026" in lighter gray, smaller font
- A thin horizontal line separator in slate (#244C5A) below the subtitle

MAIN HEATMAP SECTION (center of image):
Show 5 large rectangular tiles arranged horizontally in a row, evenly spaced. Each tile is a rounded rectangle with clear borders. The tiles represent the 5 NIST CSF Functions in this exact order from left to right:

1. IDENTIFY (ID) tile:
   - Background color: AMBER/LEMON yellow (#F1BE48)
   - Large bold text: "IDENTIFY"
   - Smaller text: "ID"
   - Number: "8" (large, prominent)
   - Percentage: "12.7%"
   - Rating label: "ADEQUATE"
   - Dark text color for readability

2. PROTECT (PR) tile:
   - Background color: GREEN (#78BE21 Apple green)
   - Large bold text: "PROTECT"
   - Smaller text: "PR"
   - Number: "38" (large, prominent)
   - Percentage: "60.3%"
   - Rating label: "STRONG"
   - White text for contrast

3. DETECT (DE) tile:
   - Background color: GREEN (#009B77 Jade green)
   - Large bold text: "DETECT"
   - Smaller text: "DE"
   - Number: "15" (large, prominent)
   - Percentage: "23.8%"
   - Rating label: "STRONG"
   - White text for contrast

4. RESPOND (RS) tile:
   - Background color: AMBER/LEMON yellow (#F1BE48)
   - Large bold text: "RESPOND"
   - Smaller text: "RS"
   - Number: "7" (large, prominent)
   - Percentage: "11.1%"
   - Rating label: "MODERATE"
   - Dark text color for readability

5. RECOVER (RC) tile:
   - Background color: RED/SIENNA (#CF4520)
   - Large bold text: "RECOVER"
   - Smaller text: "RC"
   - Number: "4" (large, prominent)
   - Percentage: "6.3%"
   - Rating label: "CRITICAL GAP"
   - White text for contrast

LEGEND (bottom of image):
A horizontal legend bar showing the coverage rating scale:
- Green square: "Strong Coverage (>20%)"
- Amber/Yellow square: "Adequate/Moderate (10-20%)"
- Red square: "Critical Gap (<10%)"

FOOTER:
Small text: "Source: EA Cybersecurity Assessment | NIST Cybersecurity Framework v2.0" in gray

STYLE REQUIREMENTS:
- Use Cenovus corporate color palette: Slate #244C5A, Sienna #CF4520, Sky #6BA4B8, Jade #009B77, Apple #78BE21, Lemon #F1BE48
- Professional, clean, minimal design - NO decorative elements, NO icons, NO clip art
- The numbers (8, 38, 15, 7, 4) should be very large and prominent in each tile
- Each tile should have a subtle drop shadow for depth
- Tiles should have rounded corners
- Overall layout should feel like a PowerPoint executive dashboard slide
- Text should be crisp, clear, and perfectly readable
- This is a data visualization, not an infographic - keep it clean and professional
"@

Write-Output "Generating NIST CSF Heatmap image via Azure OpenAI GPT Image 1.5..."
Write-Output "Endpoint: $endpoint"
Write-Output "Deployment: $deployment"

# Build the request body
$body = @{
    prompt = $prompt
    size = "1536x1024"
    quality = "high"
    n = 1
    output_format = "b64_json"
} | ConvertTo-Json -Depth 5

$url = "$endpoint/openai/deployments/$deployment/images/generations?api-version=$apiVersion"

Write-Output "Calling API at: $url"
Write-Output "Request body length: $($body.Length) characters"

# Make the API call
try {
    $headers = @{
        "api-key" = $apiKey
        "Content-Type" = "application/json"
    }

    $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body -TimeoutSec 120

    Write-Output "API call successful!"
    Write-Output "Response type: $($response.GetType().Name)"

    # Save the full response as JSON for reference
    $response | ConvertTo-Json -Depth 10 | Out-File "$sourceDir\nist_heatmap_response.json" -Encoding UTF8
    Write-Output "Response saved to: $sourceDir\nist_heatmap_response.json"

    # Extract and decode the base64 image
    $b64Data = $response.data[0].b64_json
    Write-Output "Base64 data length: $($b64Data.Length) characters"

    $imageBytes = [Convert]::FromBase64String($b64Data)
    Write-Output "Decoded image size: $($imageBytes.Length) bytes ($([math]::Round($imageBytes.Length / 1024)) KB)"

    # Save to WIP folder
    $wipPath = "$wipDir\nist_csf_heatmap.png"
    [IO.File]::WriteAllBytes($wipPath, $imageBytes)
    Write-Output "Image saved to WIP: $wipPath"

    # Copy to Draft folder with date stamp
    $draftPath = "$draftDir\DRAFT_nist_csf_heatmap_2026-02-09.png"
    Copy-Item $wipPath $draftPath -Force
    Write-Output "Image copied to Draft: $draftPath"

    Write-Output ""
    Write-Output "=== SUCCESS ==="
    Write-Output "NIST CSF Coverage Heatmap generated successfully!"
    Write-Output "WIP file: $wipPath"
    Write-Output "Draft file: $draftPath"

} catch {
    Write-Output "ERROR: API call failed!"
    Write-Output "Status: $($_.Exception.Response.StatusCode)"
    Write-Output "Error: $($_.Exception.Message)"

    # Try to get more detail from the response
    if ($_.Exception.Response) {
        try {
            $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
            $errorBody = $reader.ReadToEnd()
            Write-Output "Error details: $errorBody"
        } catch {
            Write-Output "Could not read error response body"
        }
    }

    exit 1
}
