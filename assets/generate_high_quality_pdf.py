"""
High-Quality PDF Generator for Resume
Uses Playwright for professional-grade PDF output with crisp text rendering
"""

import asyncio
from playwright.async_api import async_playwright
import os

async def generate_pdf():
    """Generate high-quality PDF from HTML resume"""
    
    # Get the absolute path to the HTML file
    html_file = os.path.abspath("Ajay_Kumar_Gupta_Resume.html")
    pdf_file = os.path.abspath("Ajay_Kumar_Gupta_Resume.pdf")
    
    print(f"📄 Converting HTML to PDF...")
    print(f"   Input:  {html_file}")
    print(f"   Output: {pdf_file}")
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Load the HTML file
        await page.goto(f"file:///{html_file}")
        
        # Wait for page to fully load
        await page.wait_for_load_state("networkidle")
        
        # Generate PDF with high-quality settings
        await page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={
                "top": "1.5cm",
                "right": "2cm",
                "bottom": "1.5cm",
                "left": "2cm"
            },
            prefer_css_page_size=False,
            scale=1.0,  # No scaling for crisp text
        )
        
        await browser.close()
    
    print(f"\n✅ PDF generated successfully!")
    print(f"📍 Location: {pdf_file}")
    print(f"📊 File size: {os.path.getsize(pdf_file) / 1024:.1f} KB")
    print("\nThe PDF has been created with high-quality text rendering!")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
