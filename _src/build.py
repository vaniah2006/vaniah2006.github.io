#!/usr/bin/env python3
"""Builds the static multi-page site. Edit content in pages/*.html, shared bits here."""
import json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://rebornready.com"
EIN = "41-5078149"
PHONE = "(478) 227-4888"
PHONE_TEL = "+14782274888"
EMAIL = "info@rebornreadyhousing.org"
ADDR1 = "111 Lower Elm St, Suite 2207"
ADDR2 = "Macon, GA 31206"
FB = "https://www.facebook.com/profile.php?id=61590810547935"
IG = "https://www.instagram.com/rebornreadycorp"
TT = "https://www.tiktok.com/@rebornready7"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("programs.html", "Our Programs"),
    ("the-need.html", "The Need"),
    ("get-involved.html", "Get Involved"),
    ("news.html", "News"),
]

PAGES = {
    "index.html": ("Reborn Ready Corp | Transitional Housing & Reentry Nonprofit in Macon, GA",
                   "Reborn Ready Corp is a Macon, Georgia 501(c)(3) nonprofit (Charity ID 41-5078149) offering structured transitional housing, paid job training, and reentry support for adults coming home from incarceration, including veterans."),
    "about.html": ("About Us | Reborn Ready Corp, Macon GA Reentry Nonprofit",
                   "Meet founder Chrissy Hunt and learn why Reborn Ready Corp exists, how our nonprofit, housing arm, and handyman partner work together, and our 501(c)(3) details. Charity ID 41-5078149."),
    "programs.html": ("Our Programs | Transitional Housing & Job Training in Macon, GA | Reborn Ready",
                      "Structured shared housing, accountability and life-skills workshops, paid trades training, transportation help, resource navigation, and a veterans track for justice-involved adults in Middle Georgia."),
    "the-need.html": ("The Need | Reentry & Housing Gaps in Georgia | Reborn Ready Corp",
                      "Georgia locks up 881 of every 100,000 residents and has transitional beds for fewer than 15% of people released each year. Here is the reentry gap Reborn Ready Corp is working to close in Macon."),
    "get-involved.html": ("Get Involved | Donate, Partner, Refer or Volunteer | Reborn Ready Corp",
                          "Support Reborn Ready Corp, a 501(c)(3) in Macon, GA (Charity ID 41-5078149). Donate, fund the first house, refer someone, hire a graduate, lease us a property, or teach a workshop."),
    "news.html": ("News & Press | Reborn Ready Corp, Macon GA",
                  "Press releases and updates from Reborn Ready Corporation, the Macon, Georgia transitional housing and reentry nonprofit."),
    "contact.html": ("Contact Us | Reborn Ready Corp, Macon GA | (478) 227-4888",
                     "Call (478) 227-4888 or email info@rebornreadyhousing.org. Reborn Ready Corp, 111 Lower Elm St, Suite 2207, Macon, GA 31206. 501(c)(3) Charity ID 41-5078149."),
    "404.html": ("Page not found | Reborn Ready Corp", "That page doesn't exist. Head back to Reborn Ready Corp's homepage."),
}

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "NGO",
    "@id": DOMAIN + "/#org",
    "name": "Reborn Ready Corporation",
    "alternateName": "Reborn Ready Corp",
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/img/reborn-ready-logo.jpg",
    "image": DOMAIN + "/img/og-image.jpg",
    "slogan": "Structured Support for New Beginnings.",
    "description": PAGES["index.html"][1],
    "taxID": EIN,
    "nonprofitStatus": "Nonprofit501c3",
    "foundingDate": "2026",
    "foundingLocation": "Macon, Georgia",
    "founder": {"@type": "Person", "name": "Crystal \"Chrissy\" Hunt", "jobTitle": "Founder & Director"},
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Macon",
                "addressRegion": "GA", "postalCode": "31206", "addressCountry": "US"},
    "areaServed": [{"@type": "AdministrativeArea", "name": "Macon-Bibb County, Georgia"},
                   {"@type": "AdministrativeArea", "name": "Middle Georgia"}],
    "sameAs": [FB, IG, TT],
}


def head(page):
    title, desc = PAGES[page]
    path = "" if page == "index.html" else page
    canonical = f"{DOMAIN}/{path}"
    ld = ""
    if page == "index.html":
        ld = f'<script type="application/ld+json">{json.dumps(ORG_LD)}</script>'
    robots = '<meta name="robots" content="noindex">' if page == "404.html" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Reborn Ready Corporation">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1A2456">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(page):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == page else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    cur = ' aria-current="page"' if page == "contact.html" else ""
    items.append(f'<li class="nav-cta"><a href="contact.html"{cur}>Contact Us</a></li>')
    return f"""<div class="topbar"><div class="wrap">
  <span>501(c)(3) nonprofit &middot; <strong>Charity ID (EIN): {EIN}</strong> &middot; Macon, Georgia</span>
  <span class="tb-phone"><a href="tel:{PHONE_TEL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="Reborn Ready Corporation home">
    <img src="img/reborn-ready-mark.jpg" alt="Reborn Ready Corporation logo: a phoenix rising over a house, held by two hands" width="54" height="42">
    <span class="brand-name">Reborn Ready<small>Corporation</small></span>
  </a>
  <button class="menu-btn" aria-expanded="false" aria-controls="site-nav"><span class="bars"><span></span></span>Menu</button>
  <nav class="nav" id="site-nav" aria-label="Main">
    <ul>{''.join(items)}</ul>
  </nav>
</div></header>
<main id="main">
"""


def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV[1:]) + '<li><a href="contact.html">Contact Us</a></li>'
    return f"""</main>
<footer class="site-footer">
  <div class="wrap footer-top">
    <div>
      <img class="footer-logo" src="img/reborn-ready-logo.jpg" alt="Reborn Ready Corporation: Structured Support for New Beginnings" width="150" height="183" loading="lazy">
      <p>Structured transitional housing, paid job training, and real-world support for adults coming home to Middle Georgia.</p>
      <span class="footer-id">Charity ID (EIN): {EIN}</span>
    </div>
    <div>
      <h4>Pages</h4>
      <ul>{links}</ul>
    </div>
    <div>
      <h4>Reach us</h4>
      <ul>
        <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ADDR1}<br>{ADDR2}</li>
      </ul>
    </div>
    <div>
      <h4>Follow along</h4>
      <ul>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="{TT}" target="_blank" rel="noopener">TikTok</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">
    <span>&copy; <span id="year">2026</span> Reborn Ready Corporation. All rights reserved.</span>
    <span>Reborn Ready Corporation is a 501(c)(3) tax-exempt nonprofit. Charity ID (EIN) {EIN}. Gifts are tax-deductible to the extent allowed by law.</span>
  </div></div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def build():
    for page in PAGES:
        body = (ROOT / "_src" / "pages" / page).read_text()
        body = (body.replace("{{EIN}}", EIN).replace("{{PHONE}}", PHONE).replace("{{PHONE_TEL}}", PHONE_TEL)
                .replace("{{EMAIL}}", EMAIL).replace("{{ADDR1}}", ADDR1).replace("{{ADDR2}}", ADDR2)
                .replace("{{FB}}", FB).replace("{{IG}}", IG).replace("{{TT}}", TT))
        html = head(page) + header(page) + body + footer()
        if page == "404.html":  # served at any depth on GitHub Pages, so use root-absolute paths
            for a in ('href="', 'src="'):
                for d in ("css/", "js/", "img/"):
                    html = html.replace(a + d, a + "/" + d)
            for h in [p for p in PAGES] :
                html = html.replace(f'href="{h}"', f'href="/{h}"')
        (ROOT / page).write_text(html)
    today = datetime.date.today().isoformat()
    urls = "".join(
        f"<url><loc>{DOMAIN}/{'' if p == 'index.html' else p}</loc><lastmod>{today}</lastmod></url>"
        for p in PAGES if p != "404.html")
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")


if __name__ == "__main__":
    build()
