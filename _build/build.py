# -*- coding: utf-8 -*-
"""Builds texastrailmark.com as a static multi-page site with clean URLs."""
import json, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import SITE, AREAS, PRODUCTS, GENERAL_FAQ, POSTS

OUT = sys.argv[1]
HERE = os.path.dirname(__file__)
U = SITE["url"]
P = {p["slug"]: p for p in PRODUCTS}

def esc(s): return html.escape(s, quote=True)
def strip(s): return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")
def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)
def nice_date(d):
    y, m, dd = d.split("-")
    return ["January","February","March","April","May","June","July","August","September","October","November","December"][int(m)-1] + f" {int(dd)}, {y}"
def img(slug, card=False): return f"/images/products/{slug}-denton-tx{'-card' if card else ''}.jpg"

# ---------------------------------------------------------------- icons
I = {
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14M13 5l7 7-7 7"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
 "chev": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 3v18h18"/><path d="m7 14 4-4 4 4 5-5"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}

ADDR_HTML = f'{SITE["street"]}<br>{SITE["city"]}, Texas {SITE["zip"]}'

# ---------------------------------------------------------------- schema
def org_schema():
    return {
        "@type": "InsuranceAgency", "@id": U + "/#agency",
        "name": SITE["name"], "url": U + "/",
        "logo": U + "/images/logo.png", "image": U + "/images/logo.png",
        "description": "Independent insurance agency in Denton, Texas offering auto, home, renters, condo and townhome, motorcycle, landlord, jewelry, umbrella, boat, business and RV insurance from multiple carriers.",
        "telephone": SITE["tel"], "email": SITE["email"], "priceRange": "Free quotes",
        "address": {"@type": "PostalAddress", "streetAddress": SITE["street"], "addressLocality": SITE["city"],
                    "addressRegion": SITE["region"], "postalCode": SITE["zip"], "addressCountry": "US"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "17:00",
            "description": "Phone hours. Office visits by appointment only."}],
        "areaServed": [{"@type": "City", "name": f"{a}, TX"} for a in AREAS] + [{"@type": "State", "name": "Texas"}],
        "employee": {"@type": "Person", "name": SITE["advisor"], "jobTitle": "Insurance Advisor"},
        "knowsAbout": [p["name"] for p in PRODUCTS],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Insurance Products",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["name"], "url": f"{U}/products/{p['slug']}/"}} for p in PRODUCTS]},
    }

def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i+1, "name": n, "item": U + h} for i, (n, h) in enumerate(items)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}

def ld(*nodes):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(nodes)}, ensure_ascii=False) + "</script>"

# ---------------------------------------------------------------- layout
def head(title, desc, path, image="/images/logo.png", schema="", og_type="website"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{U}{path}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#0f2244">
<meta name="geo.region" content="US-TX">
<meta name="geo.placename" content="Denton, Texas">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{U}{path}">
<meta property="og:image" content="{U}{image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{U}{image}">
<link rel="icon" type="image/png" href="/images/favicon.png">
<link rel="apple-touch-icon" href="/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/trailmark.css">
<script>document.documentElement.classList.add('js')</script>
{schema}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(active=""):
    def cur(k): return ' aria-current="page"' if k == active else ""
    dd = "\n".join(f'          <a href="/products/{p["slug"]}/">{p["name"]}</a>' for p in PRODUCTS)
    return f"""<div class="topbar">
  <div class="container">
    <div class="tb-group">
      <a href="tel:{SITE['tel']}">{I['phone']}{SITE['phone']}</a>
      <a href="mailto:{SITE['email']}" class="hide-sm">{I['mail']}{SITE['email']}</a>
    </div>
    <div class="tb-group">
      <span class="hide-sm">{I['clock']}Call Mon–Fri, 9 AM – 5 PM &nbsp;·&nbsp; Office visits by appointment</span>
      <span>{I['pin']}<span class="hide-sm">Denton, TX ·&nbsp;</span>Serving All of Texas</span>
    </div>
  </div>
</div>

<header class="site">
  <div class="container nav">
    <a href="/" class="brand" aria-label="Trailmark Insurance Advisors home"><img src="/images/emblem.png" alt="" width="640" height="375"><span class="bt"><b>TRAILMARK</b><i>Insurance Advisors</i></span></a>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="navlinks">{I['menu']}</button>
    <nav class="nav-links" id="navlinks" aria-label="Main">
      <a href="/"{cur('home')}>Home</a>
      <div class="dd">
        <button class="dd-toggle{' is-active' if active == 'products' else ''}" aria-expanded="false" aria-haspopup="true">Our Products {I['chev']}</button>
        <div class="dd-menu">
{dd}
          <a class="all" href="/products/">View all insurance products →</a>
        </div>
      </div>
      <a href="/news-and-insights/"{cur('news')}>News &amp; Insights</a>
      <a href="/faq/"{cur('faq')}>FAQ</a>
      <a href="/contact/"{cur('contact')}>Contact</a>
      <a href="/contact/#quote" class="btn btn-gold">Get a Free Quote</a>
    </nav>
  </div>
</header>
"""

def footer():
    prods = "\n".join(f'        <li><a href="/products/{p["slug"]}/">{p["name"]}</a></li>' for p in PRODUCTS)
    return f"""
<footer>
  <div class="container foot">
    <div>
      <div class="foot-logo"><img src="/images/logo.png" alt="Trailmark Insurance Advisors logo" width="900" height="580" loading="lazy"></div>
      <p>Trailmark Insurance Advisors is an independent, Texas-owned insurance agency in Denton, TX. We compare auto, home, renters, business and specialty insurance from multiple carriers for families and businesses across Denton County, Dallas–Fort Worth and all of Texas.</p>
    </div>
    <div>
      <h4>Our Products</h4>
      <ul class="foot-prods">
{prods}
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/products/">Our Products</a></li>
        <li><a href="/news-and-insights/">News &amp; Insights</a></li>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/contact/#quote">Get a Free Quote</a></li>
        <li><a href="/privacy/">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul class="foot-contact">
        <li>{I['phone']}<a href="tel:{SITE['tel']}">{SITE['phone']}</a></li>
        <li>{I['mail']}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
        <li>{I['pin']}<span>{ADDR_HTML}</span></li>
        <li>{I['clock']}<span>Phone: Mon–Fri, 9 AM – 5 PM<br>Office: By appointment</span></li>
      </ul>
    </div>
  </div>
  <div class="container foot-bottom">
    <span>© <span class="yr">2026</span> Trailmark Insurance Advisors · Denton, Texas · <a href="/privacy/">Privacy Policy</a></span>
    <span>Coverage is subject to policy terms, underwriting and availability. Information on this site is general and not a guarantee of coverage.</span>
  </div>
</footer>
<script src="/js/trailmark.js" defer></script>
</body>
</html>
"""

def page_hero(eyebrow, h1, lead, crumbs, image=None, alt=""):
    cr = ' <span>/</span> '.join(f'<a href="{h}">{n}</a>' if i < len(crumbs)-1 else f'<b>{n}</b>' for i, (n, h) in enumerate(crumbs))
    pic = f'<div class="ph-img"><img src="{image}" alt="{esc(alt)}" width="1400" height="1050" fetchpriority="high"></div>' if image else ""
    return f"""<section class="page-hero{' with-img' if image else ''}">
  <div class="container">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{lead}</p>
    </div>
    {pic}
  </div>
</section>
"""

def pcard(p, heading="h3"):
    return f"""<a class="pcard reveal" href="/products/{p['slug']}/">
        <img src="{img(p['slug'], True)}" alt="{esc(p['alt'])}" width="720" height="480" loading="lazy">
        <div class="body"><{heading}>{p['name']}</{heading}><p>{p['card']}</p><span class="more">Learn more {I['arrow']}</span></div>
      </a>"""

def product_grid():
    cards = "\n      ".join(pcard(p) for p in PRODUCTS)
    return f"""<div class="pgrid">
      {cards}
      <a class="pcard pcard-cta reveal" href="/contact/#quote">
        <div class="body"><span class="eyebrow">Bundle &amp; Save</span><h3>Not sure what you need?</h3><p>Combine home, auto and more for bigger discounts and one advisor who knows your whole picture. We'll build the right package for you.</p><span class="more">Get a free quote {I['arrow']}</span></div>
      </a>
    </div>"""

def faq_list(faqs):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs) + "</div>"

CHIPS = [(p["cov"], p["short"]) for p in PRODUCTS] + [("Bundle", "Bundle")]
def quote_form(source):
    chips = "\n".join(f'              <label><input type="checkbox" name="coverage" value="{v}"><span>{l}</span></label>' for v, l in CHIPS)
    return f"""<div class="form-card reveal">
      <form class="quote-form" data-endpoint="{SITE['formspree']}" novalidate>
        <input type="hidden" name="_subject" value="New quote request from texastrailmark.com">
        <input type="hidden" name="source_page" value="{source}">
        <h3>Quick Quote Request</h3>
        <p>No obligation. We never sell your information.</p>
        <div class="fgrid">
          <div class="field"><label for="fname">First Name *</label><input id="fname" name="first_name" required autocomplete="given-name"></div>
          <div class="field"><label for="lname">Last Name *</label><input id="lname" name="last_name" required autocomplete="family-name"></div>
          <div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="phone">Phone *</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="zip">ZIP Code</label><input id="zip" name="zip" inputmode="numeric" maxlength="5" autocomplete="postal-code"></div>
          <div class="field"><label for="contact_pref">Best Way to Reach You</label>
            <select id="contact_pref" name="contact_preference"><option>Phone call</option><option>Text message</option><option>Email</option></select></div>
          <div class="field full"><span class="lbl">Coverage I'm Interested In</span>
            <div class="chips">
{chips}
            </div>
          </div>
          <div class="field full"><label for="msg">Anything else we should know?</label><textarea id="msg" name="message" rows="4" placeholder="Current carrier, renewal date, questions…"></textarea></div>
        </div>
        <button type="submit" class="btn btn-gold">Request My Free Quote</button>
        <p class="form-note">By submitting, you agree to be contacted by Trailmark Insurance Advisors about your quote. See our <a href="/privacy/">Privacy Policy</a>.</p>
      </form>
      <div class="form-success" role="status">
        {I['check']}
        <h3>Thank you!</h3>
        <p>We received your request and an advisor will be in touch soon, usually within one business day.</p>
      </div>
    </div>"""

def contact_info(h2="Request Your Free Quote", eyebrow="Get in Touch"):
    return f"""<div class="contact-info reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{h2}</h2>
      <p>Tell us a little about what you need and an advisor will reach out, usually within one business day.</p>
      <div class="info-item"><div class="ico">{I['phone']}</div><div><small>Call Us</small><a href="tel:{SITE['tel']}"><strong>{SITE['phone']}</strong></a></div></div>
      <div class="info-item"><div class="ico">{I['mail']}</div><div><small>Email</small><a href="mailto:{SITE['email']}"><strong>{SITE['email']}</strong></a></div></div>
      <div class="info-item"><div class="ico">{I['pin']}</div><div><small>Office</small><strong>{ADDR_HTML}</strong></div></div>
      <div class="info-item last"><div class="ico">{I['clock']}</div><div><small>Hours</small><strong>Phone: Mon–Fri, 9:00 AM – 5:00 PM</strong><br><strong>Office: By appointment only</strong><span class="hours-note">Call or email to schedule a time to meet in person.</span></div></div>
    </div>"""

def cta_band(h="Ready to Blaze a Better Trail?", p="Get a free, no-obligation quote today and see how much you could save with the right coverage."):
    return f"""<section class="band">
  <div class="container reveal">
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="hero-ctas">
      <a href="/contact/#quote" class="btn btn-gold">Get My Free Quote</a>
      <a href="tel:{SITE['tel']}" class="btn btn-outline-light">Call {SITE['phone']}</a>
    </div>
  </div>
</section>
"""

def post_card(b):
    return f"""<a class="bcard reveal" href="/news-and-insights/{b['slug']}/">
        <img src="{img(b['img'], True)}" alt="{esc(P[b['img']]['alt'])}" width="720" height="480" loading="lazy">
        <div class="body"><span class="tag">{b['cat']}</span><h3>{b['title']}</h3><p>{b['excerpt']}</p><span class="meta">{nice_date(b['date'])} · {b['read']} min read</span></div>
      </a>"""

def areas_section():
    chips = "".join(f"<li>{a}</li>" for a in AREAS)
    return f"""<section class="section areas">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Areas We Serve</span>
      <h2>Your Local Insurance Agency in Denton County</h2>
      <p>From our office in Denton, we help families and businesses across North Texas and the Dallas–Fort Worth Metroplex, and we can serve clients anywhere in Texas by phone and email.</p>
      <div class="rule"></div>
    </div>
    <ul class="area-list reveal">{chips}<li class="all">All of Texas</li></ul>
  </div>
</section>
"""

# ---------------------------------------------------------------- HOME
def build_home():
    title = "Trailmark Insurance Advisors | Independent Insurance Agency in Denton, TX"
    desc = "Independent insurance agency in Denton, TX. Compare auto, home, renters, condo, motorcycle, landlord, umbrella, boat, RV and business insurance quotes from multiple carriers. Free quotes."
    web = {"@type": "WebSite", "@id": U + "/#website", "url": U + "/", "name": SITE["name"], "publisher": {"@id": U + "/#agency"}}
    home_faq = GENERAL_FAQ[:4]
    schema = ld(org_schema(), web, faq_schema(home_faq))
    posts = "\n      ".join(post_card(b) for b in POSTS[:3])
    body = head(title, desc, "/", schema=schema) + header("home") + f"""
<main id="main">
<section class="hero">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">Independent Insurance Agency · Denton, Texas</span>
      <h1>We Help You Find the <em>Right Trail</em> to Better Coverage.</h1>
      <p class="lead">Auto, home, renters, business and specialty insurance from a local advisor who works for you, not one insurance company. We compare multiple top-rated carriers so you get the protection you need at a price that makes sense.</p>
      <div class="hero-ctas">
        <a href="/contact/#quote" class="btn btn-gold">Get a Free Quote {I['arrow']}</a>
        <a href="tel:{SITE['tel']}" class="btn btn-outline">{I['phone']} Call {SITE['phone']}</a>
      </div>
      <div class="hero-trust">
        <div>{I['shield']}Licensed in Texas</div>
        <div>{I['users']}Locally Owned</div>
        <div>{I['chart']}Multiple Carriers</div>
      </div>
    </div>
    <div class="hero-art reveal">
      <div class="card">
        <img src="/images/family.png" class="photo" alt="A Texas family protected by Trailmark Insurance" width="1200" height="900" fetchpriority="high">
        <h2 class="h3">Protecting What Matters Most</h2>
        <p>Your family, your home and everything you've worked for, protected by people who treat it like their own.</p>
      </div>
      <div class="hero-badge"><strong>Free</strong><span>No-obligation<br>coverage review</span></div>
    </div>
  </div>
</section>

<section class="strip">
  <div class="container">
    <div>
      <h2 class="h3">Paying too much for insurance?</h2>
      <p>Let us shop your current policies. It takes about 10 minutes and costs nothing.</p>
    </div>
    <a href="/contact/#quote" class="btn btn-gold">Compare My Rates</a>
  </div>
</section>

<section class="section" id="coverage">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Products</span>
      <h2>Insurance Solutions for Every Part of Life</h2>
      <p>Whether you're protecting your car, your home, your boat or your business, Trailmark compares coverage from multiple insurance companies to build the right plan for you.</p>
      <div class="rule"></div>
    </div>
    {product_grid()}
    <div class="center-cta reveal"><a href="/products/" class="btn btn-navy">Explore All Insurance Products</a></div>
  </div>
</section>

<section class="section why" id="why">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">Why Trailmark</span>
      <h2>An Advisor in Your Corner, Not a Call Center</h2>
      <p class="intro">Captive agents can only sell one company's products. As an <a href="/news-and-insights/independent-insurance-agent-vs-captive-agent-denton/">independent insurance agency</a>, Trailmark works for you. We shop the market, explain your options clearly and stick around after the sale.</p>
      <div class="feat"><div class="num">{I['chart']}</div><div><h3 class="h4">We Shop, You Save</h3><p>One conversation, quotes from multiple carriers, so you can compare real options side by side.</p></div></div>
      <div class="feat"><div class="num">{I['chat']}</div><div><h3 class="h4">Plain-English Advice</h3><p>No jargon, no pressure. We explain what you're buying and why it matters.</p></div></div>
      <div class="feat"><div class="num">{I['shield']}</div><div><h3 class="h4">Here When You Need Us</h3><p>Claims questions, policy changes and annual reviews. You'll talk to a real person who knows your name.</p></div></div>
    </div>
    <div class="stats reveal">
      <div class="stat"><strong>TX</strong><span>Licensed, local &amp; Texas-owned</span></div>
      <div class="stat"><strong>1</strong><span>Advisor for all your policies</span></div>
      <div class="stat"><strong>10 min</strong><span>Typical time to start a quote</span></div>
      <div class="stat"><strong>$0</strong><span>Cost for a coverage review</span></div>
    </div>
  </div>
</section>

<section class="section" id="how">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How It Works</span>
      <h2>Better Coverage in Three Simple Steps</h2>
      <div class="rule"></div>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="circle">1</div><h3>Tell Us About You</h3><p>Fill out our quick quote form or give us a call. Share your current policy if you have one.</p></div>
      <div class="step reveal"><div class="circle">2</div><h3>We Shop the Market</h3><p>We compare coverage and pricing across multiple carriers to find your best fit.</p></div>
      <div class="step reveal"><div class="circle">3</div><h3>Pick &amp; Get Protected</h3><p>We walk you through your options, you choose, and we handle the paperwork.</p></div>
    </div>
  </div>
</section>

<section class="section about" id="about">
  <div class="container">
    <div class="about-img reveal">
      <img src="/images/eric-glenn-square.jpg" alt="Eric Glenn, insurance advisor at Trailmark Insurance Advisors in Denton, Texas" width="900" height="900" loading="lazy">
      <span class="tag">Texas Owned &amp; Operated</span>
    </div>
    <div class="reveal">
      <span class="eyebrow">About Us</span>
      <h2>Marking a Better Trail for Texas Families &amp; Businesses</h2>
      <p>Trailmark Insurance Advisors was founded on a simple idea: buying insurance should feel like getting advice from a trusted neighbor, not a sales pitch.</p>
      <p>Led by insurance advisor Eric Glenn, our Denton office brings hands-on insurance experience to drivers, homeowners, renters and business owners across North Texas. As an independent agency, we can offer more choices and find coverage that truly fits.</p>
      <ul class="checks">
        <li>{I['check']}Licensed Texas agents</li>
        <li>{I['check']}Independent &amp; unbiased</li>
        <li>{I['check']}Personal &amp; commercial lines</li>
        <li>{I['check']}Free annual policy reviews</li>
      </ul>
      <a href="/contact/" class="btn btn-navy">Talk to an Advisor</a>
    </div>
  </div>
</section>

{areas_section()}
<section class="section insights">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">News &amp; Insights</span>
      <h2>Insurance Tips for North Texas</h2>
      <p>Plain-English guides from our Denton office on saving money and avoiding coverage gaps.</p>
      <div class="rule"></div>
    </div>
    <div class="bgrid">
      {posts}
    </div>
    <div class="center-cta reveal"><a href="/news-and-insights/" class="btn btn-outline">Read All News &amp; Insights</a></div>
  </div>
</section>

<section class="section faq-teaser">
  <div class="container narrow">
    <div class="section-head reveal">
      <span class="eyebrow">Common Questions</span>
      <h2>Frequently Asked Questions</h2>
      <div class="rule"></div>
    </div>
    <div class="reveal">{faq_list(home_faq)}</div>
    <div class="center-cta reveal"><a href="/faq/" class="btn btn-outline">See All FAQs</a></div>
  </div>
</section>

{cta_band()}
<section class="section contact" id="quote">
  <div class="container">
    {contact_info()}
    {quote_form("Home page")}
  </div>
</section>
</main>
""" + footer()
    write("index.html", body)

# ---------------------------------------------------------------- PRODUCTS HUB
def build_products_hub():
    title = "Our Insurance Products | Auto, Home, Business & More in Denton, TX | Trailmark"
    desc = "Explore every insurance product Trailmark offers in Denton, TX: auto, home, renters, condo and townhome, motorcycle, landlord, jewelry, umbrella, boat, business and RV insurance."
    items = {"@type": "ItemList", "name": "Insurance products from Trailmark Insurance Advisors",
             "itemListElement": [{"@type": "ListItem", "position": i+1, "name": p["name"], "url": f"{U}/products/{p['slug']}/"} for i, p in enumerate(PRODUCTS)]}
    crumbs = [("Home", "/"), ("Our Products", "/products/")]
    schema = ld(org_schema(), crumbs_schema(crumbs), items)
    rows = "".join(f'<tr><td><a href="/products/{p["slug"]}/">{p["name"]}</a></td><td>{p["card"]}</td></tr>' for p in PRODUCTS)
    body = head(title, desc, "/products/", schema=schema) + header("products") + f"""
<main id="main">
{page_hero("Our Products", "Insurance Products for Texas Families &amp; Businesses", "Trailmark Insurance Advisors is an independent agency in Denton, Texas. We compare policies from multiple insurance companies for everything you drive, own, rent and run, so you get strong coverage at a competitive price.", crumbs)}
<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Personal &amp; Commercial Insurance</span>
      <h2>Choose the Coverage You Need</h2>
      <p>Select a product to learn what it covers, what Texas residents should know, and how to save. Need more than one? Bundling often unlocks the biggest discounts.</p>
      <div class="rule"></div>
    </div>
    {product_grid()}
  </div>
</section>

<section class="section tint">
  <div class="container narrow reveal">
    <div class="section-head">
      <span class="eyebrow">At a Glance</span>
      <h2>Every Product We Offer</h2>
      <div class="rule"></div>
    </div>
    <div class="table-wrap"><table class="glance"><thead><tr><th>Insurance</th><th>What it protects</th></tr></thead><tbody>{rows}</tbody></table></div>
  </div>
</section>

<section class="section">
  <div class="container narrow prose reveal">
    <h2>Why Buy Insurance Through an Independent Agency?</h2>
    <p>When you work with Trailmark, you get one local advisor and many insurance companies. Instead of getting a single quote from a single company, we compare coverage, deductibles and pricing across several carriers and explain the differences in plain English.</p>
    <p>That's especially valuable in Texas, where wind and hail deductibles, roof coverage and uninsured-driver protection vary widely from one policy to the next. And because we handle your auto, home, umbrella and specialty policies together, we can spot gaps and overlaps that are easy to miss when everything is with different companies.</p>
    <div class="callout"><strong>Bundle and save.</strong> Combining home and auto, or adding renters, condo, motorcycle, boat or RV coverage, is one of the easiest ways to lower your total insurance cost. <a href="/contact/#quote">Ask us for a bundle quote</a>.</div>
  </div>
</section>
{cta_band("Not Sure Where to Start?", "Tell us what you drive, own and rent. We'll recommend the right coverage and compare quotes for free.")}
</main>
""" + footer()
    write("products/index.html", body)

# ---------------------------------------------------------------- PRODUCT PAGES
def build_product(p):
    path = f"/products/{p['slug']}/"
    crumbs = [("Home", "/"), ("Our Products", "/products/"), (p["name"], path)]
    service = {"@type": "Service", "@id": U + path + "#service", "name": p["name"], "serviceType": p["name"],
               "description": strip(p["desc"]), "url": U + path, "image": U + img(p["slug"]),
               "provider": {"@id": U + "/#agency"},
               "areaServed": [{"@type": "City", "name": f"{a}, TX"} for a in AREAS[:10]] + [{"@type": "State", "name": "Texas"}]}
    schema = ld(org_schema(), service, crumbs_schema(crumbs), faq_schema(p["faqs"]))
    covers = "".join(f'<div class="cover"><div class="ck">{I["check"]}</div><div><h3>{h}</h3><p>{t}</p></div></div>' for h, t in p["covers"])
    save = "".join(f"<li>{s}</li>" for s in p["save"])
    intro = "".join(f"<p>{x}</p>" for x in p["intro"])
    rel = "".join(pcard(P[r]) for r in p["related"])
    others = "".join(f'<li><a href="/products/{o["slug"]}/">{o["name"]}</a></li>' for o in PRODUCTS if o["slug"] != p["slug"])
    rel_posts = [b for b in POSTS if p["slug"] in b["related"]]
    post_html = ""
    if rel_posts:
        post_html = '<div class="side-card"><h3>Related Insights</h3><ul class="side-links">' + "".join(f'<li><a href="/news-and-insights/{b["slug"]}/">{b["title"]}</a></li>' for b in rel_posts) + "</ul></div>"
    body = head(p["title"], p["desc"], path, image=img(p["slug"]), schema=schema) + header("products") + f"""
<main id="main">
{page_hero("Independent Insurance Agency · Denton, TX", p["h1"], p["lead"], crumbs, img(p["slug"]), p["alt"])}
<section class="section">
  <div class="container layout">
    <article class="prose">
      <h2>{p['name']} From a Local, Independent Advisor</h2>
      {intro}
      <h2>What {p['name']} Covers</h2>
      <div class="covers">{covers}</div>
      <h2>{p['texas_h']}</h2>
      {p['texas']}
      <h2>{p['save_h']}</h2>
      <ul>{save}</ul>
      <h2>{p['name']} FAQs</h2>
      {faq_list(p['faqs'])}
      <div class="callout">Ready to compare {p['name'].lower()} quotes? <a href="/contact/?coverage={p['cov']}#quote">Request a free quote</a> or call <a href="tel:{SITE['tel']}">{SITE['phone']}</a>. Eric Glenn and the team at Trailmark Insurance Advisors in Denton will shop multiple carriers for you.</div>
    </article>
    <aside class="side">
      <div class="side-card navy">
        <h3>Get a Free {p['short']} Quote</h3>
        <p>Compare coverage from multiple carriers in about 10 minutes. No obligation.</p>
        <a href="/contact/?coverage={p['cov']}#quote" class="btn btn-gold">Start My Quote</a>
        <a href="tel:{SITE['tel']}" class="side-phone">{I['phone']} {SITE['phone']}</a>
        <small>Phone: Mon–Fri, 9 AM – 5 PM</small>
      </div>
      {post_html}
      <div class="side-card">
        <h3>Other Insurance Products</h3>
        <ul class="side-links">{others}</ul>
      </div>
    </aside>
  </div>
</section>

<section class="section tint">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Bundle &amp; Save</span>
      <h2>Pair {p['name']} With</h2>
      <div class="rule"></div>
    </div>
    <div class="pgrid three">{rel}</div>
  </div>
</section>
{cta_band(f"Protect What Matters With the Right {p['short']} Coverage", "Get a free, no-obligation quote from a local, independent advisor in Denton.")}
</main>
""" + footer()
    write(f"products/{p['slug']}/index.html", body)

# ---------------------------------------------------------------- BLOG
def build_blog_index():
    title = "News & Insights | Texas Insurance Tips & Guides | Trailmark Insurance Advisors"
    desc = "Insurance news, tips and plain-English guides for Denton and North Texas families and businesses from Trailmark Insurance Advisors, an independent agency in Denton, TX."
    crumbs = [("Home", "/"), ("News & Insights", "/news-and-insights/")]
    blog = {"@type": "Blog", "name": "Trailmark News & Insights", "url": U + "/news-and-insights/", "publisher": {"@id": U + "/#agency"},
            "blogPost": [{"@type": "BlogPosting", "headline": b["title"], "url": f"{U}/news-and-insights/{b['slug']}/", "datePublished": b["date"]} for b in POSTS]}
    schema = ld(org_schema(), crumbs_schema(crumbs), blog)
    cards = "\n      ".join(post_card(b) for b in POSTS)
    body = head(title, desc, "/news-and-insights/", schema=schema) + header("news") + f"""
<main id="main">
{page_hero("News &amp; Insights", "Insurance News &amp; Insights for North Texas", "Practical, plain-English guidance on auto, home, renters, condo, umbrella and business insurance from our independent agency in Denton, Texas.", [("Home","/"),("News &amp; Insights","/news-and-insights/")])}
<section class="section">
  <div class="container">
    <div class="bgrid">
      {cards}
    </div>
  </div>
</section>
{cta_band("Have a Question We Haven't Covered?", "Call or send us a message. We're happy to explain your coverage, even if you're not ready to switch.")}
</main>
""" + footer()
    write("news-and-insights/index.html", body)

def build_post(b):
    path = f"/news-and-insights/{b['slug']}/"
    crumbs = [("Home", "/"), ("News & Insights", "/news-and-insights/"), (b["title"], path)]
    post = {"@type": "BlogPosting", "headline": b["title"], "description": b["desc"], "image": U + img(b["img"]),
            "datePublished": b["date"], "dateModified": b["date"], "mainEntityOfPage": U + path,
            "author": {"@type": "Person", "name": SITE["advisor"], "jobTitle": "Insurance Advisor", "worksFor": {"@id": U + "/#agency"}},
            "publisher": {"@id": U + "/#agency"}, "articleSection": b["cat"],
            "about": [P[r]["name"] for r in b["related"]], "spatialCoverage": "Denton, Texas"}
    schema = ld(org_schema(), post, crumbs_schema(crumbs))
    rel_prod = "".join(pcard(P[r]) for r in b["related"])
    more = "".join(post_card(o) for o in POSTS if o["slug"] != b["slug"])[:]
    others = [o for o in POSTS if o["slug"] != b["slug"]][:3]
    more = "\n      ".join(post_card(o) for o in others)
    cr = ' <span>/</span> '.join([f'<a href="/">Home</a>', f'<a href="/news-and-insights/">News &amp; Insights</a>', f'<b>{b["cat"]}</b>'])
    body = head(b["title"] + " | Trailmark", b["desc"], path, image=img(b["img"]), schema=schema, og_type="article") + header("news") + f"""
<main id="main">
<section class="page-hero post-hero">
  <div class="container narrow">
    <nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
    <span class="eyebrow">{b['cat']}</span>
    <h1>{b['title']}</h1>
    <div class="byline"><img src="/images/eric-glenn-square.jpg" alt="" width="48" height="48"><div><strong>By {SITE['advisor']}</strong><span>Insurance Advisor, Trailmark Insurance Advisors · Denton, TX</span><span>{nice_date(b['date'])} · {b['read']} min read</span></div></div>
  </div>
</section>
<section class="section post">
  <div class="container narrow">
    <img class="post-img" src="{img(b['img'])}" alt="{esc(P[b['img']]['alt'])}" width="1400" height="1050">
    <article class="prose">
      {b['body']}
      <div class="author-box"><img src="/images/eric-glenn-square.jpg" alt="Eric Glenn" width="88" height="88" loading="lazy"><div><strong>About the author</strong><p>Eric Glenn is an insurance advisor with Trailmark Insurance Advisors, an independent, Texas-owned agency at {SITE['street']} in Denton. He helps families and businesses across Denton County and North Texas compare coverage from multiple carriers. Reach him at <a href="tel:{SITE['tel']}">{SITE['phone']}</a> or <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p></div></div>
      <p class="disclaimer">This article is general information, not legal advice or a guarantee of coverage. Coverage depends on your specific policy, carrier and underwriting.</p>
    </article>
  </div>
</section>
<section class="section tint">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Related Coverage</span><h2>Products Mentioned in This Article</h2><div class="rule"></div></div>
    <div class="pgrid two">{rel_prod}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Keep Reading</span><h2>More News &amp; Insights</h2><div class="rule"></div></div>
    <div class="bgrid">
      {more}
    </div>
  </div>
</section>
{cta_band()}
</main>
""" + footer()
    write(f"news-and-insights/{b['slug']}/index.html", body)

# ---------------------------------------------------------------- FAQ
def build_faq():
    title = "Insurance FAQ | Questions About Coverage in Denton, TX | Trailmark"
    desc = "Answers to common insurance questions from Trailmark Insurance Advisors in Denton, TX: independent agents, quotes, Texas auto minimums, hail, condo, renters, umbrella and business insurance."
    crumbs = [("Home", "/"), ("FAQ", "/faq/")]
    prod_faqs = [(q, a) for p in PRODUCTS for q, a in p["faqs"][:2]]
    schema = ld(org_schema(), crumbs_schema(crumbs), faq_schema(GENERAL_FAQ + prod_faqs))
    groups = "".join(f'<h3 class="faq-group"><a href="/products/{p["slug"]}/">{p["name"]}</a></h3>' + faq_list(p["faqs"][:2]) for p in PRODUCTS)
    body = head(title, desc, "/faq/", schema=schema) + header("faq") + f"""
<main id="main">
{page_hero("FAQ", "Frequently Asked Insurance Questions", "Straight answers about working with an independent insurance agency in Denton and the coverage Texas families and businesses ask about most.", crumbs)}
<section class="section">
  <div class="container narrow">
    <h2 class="faq-title reveal">Working With Trailmark</h2>
    <div class="reveal">{faq_list(GENERAL_FAQ)}</div>
    <h2 class="faq-title reveal">Coverage Questions by Product</h2>
    <div class="reveal">{groups}</div>
  </div>
</section>
{cta_band("Still Have Questions?", "Call (214) 531-7932 or send us a message. A real person will get back to you, usually within one business day.")}
</main>
""" + footer()
    write("faq/index.html", body)

# ---------------------------------------------------------------- CONTACT
def build_contact():
    title = "Contact Trailmark Insurance Advisors | Free Insurance Quote in Denton, TX"
    desc = "Contact Trailmark Insurance Advisors at 3616 Duchess Dr, Ste. 120, Denton, TX 76205. Call (214) 531-7932 or request a free auto, home, renters, business or specialty insurance quote online."
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    cp = {"@type": "ContactPage", "url": U + "/contact/", "name": "Contact Trailmark Insurance Advisors", "about": {"@id": U + "/#agency"}}
    schema = ld(org_schema(), crumbs_schema(crumbs), cp)
    q = "3616+Duchess+Dr+Ste+120,+Denton,+TX+76205"
    body = head(title, desc, "/contact/", schema=schema) + header("contact") + f"""
<main id="main">
{page_hero("Contact Us", "Contact Trailmark Insurance Advisors", "Request a free quote, ask a coverage question or schedule an office visit. We usually respond within one business day.", crumbs)}
<section class="section contact" id="quote">
  <div class="container">
    {contact_info("Let's Talk About Your Coverage", "Get in Touch")}
    {quote_form("Contact page")}
  </div>
</section>
<section class="section tint map-sec">
  <div class="container map-grid">
    <div class="reveal">
      <span class="eyebrow">Visit Our Office</span>
      <h2>Our Denton Office</h2>
      <p><strong>{ADDR_HTML}</strong></p>
      <p>We're located in Denton, Texas, convenient to I-35E, US-380 and Loop 288. Office visits are <strong>by appointment only</strong>, so please call <a href="tel:{SITE['tel']}">{SITE['phone']}</a> or email <a href="mailto:{SITE['email']}">{SITE['email']}</a> to schedule a time.</p>
      <p>Proudly serving {", ".join(AREAS[:-1])} and {AREAS[-1]}, plus clients throughout Texas.</p>
      <a class="btn btn-outline" href="https://www.google.com/maps/dir/?api=1&amp;destination={q}" target="_blank" rel="noopener">Get Directions</a>
    </div>
    <div class="map reveal"><iframe title="Map to Trailmark Insurance Advisors in Denton, Texas" src="https://www.google.com/maps?q={q}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
</main>
""" + footer()
    write("contact/index.html", body)

# ---------------------------------------------------------------- PRIVACY
def build_privacy():
    title = "Privacy Policy | Trailmark Insurance Advisors"
    desc = "How Trailmark Insurance Advisors in Denton, TX collects, uses and protects the information you share through texastrailmark.com."
    crumbs = [("Home", "/"), ("Privacy Policy", "/privacy/")]
    schema = ld(org_schema(), crumbs_schema(crumbs))
    body = head(title, desc, "/privacy/", schema=schema) + header() + f"""
<main id="main">
{page_hero("Legal", "Privacy Policy", "Effective November 1, 2026", crumbs)}
<section class="section">
  <div class="container narrow prose">
    <p>Trailmark Insurance Advisors ("Trailmark," "we," "us") respects your privacy. This policy explains what information we collect through texastrailmark.com, how we use it and the choices you have.</p>
    <h2>Information we collect</h2>
    <ul>
      <li><strong>Information you give us.</strong> When you fill out a quote request or contact form, call or email us, we collect details such as your name, email address, phone number, ZIP code, the coverage you're interested in and anything you include in your message.</li>
      <li><strong>Information collected automatically.</strong> Like most websites, our hosting provider and the services we use may log basic technical information such as your IP address, browser type, pages visited and the date and time of your visit.</li>
    </ul>
    <h2>How we use your information</h2>
    <ul>
      <li>To respond to your questions and prepare insurance quotes</li>
      <li>To contact you by phone, text or email about your request, using the method you prefer</li>
      <li>To share necessary information with insurance companies when you ask us to obtain quotes or coverage for you</li>
      <li>To operate, secure and improve our website</li>
      <li>To meet legal and regulatory obligations</li>
    </ul>
    <h2>We do not sell your information</h2>
    <p>We do not sell, rent or trade your personal information. We share it only with insurance carriers and service providers as needed to provide the quotes and services you request, or when required by law.</p>
    <h2>Service providers we use</h2>
    <ul>
      <li><strong>Formspree</strong> processes the forms on our website and delivers your submission to us by email.</li>
      <li><strong>GitHub Pages</strong> and <strong>Cloudflare</strong> host and deliver our website.</li>
      <li><strong>Google Fonts</strong> and <strong>Google Maps</strong> provide fonts and the map on our contact page, and may collect technical information under Google's own privacy policy.</li>
    </ul>
    <h2>Cookies</h2>
    <p>Our website does not use advertising cookies. Third-party services such as Google Maps may set their own cookies when you interact with them. You can control cookies through your browser settings.</p>
    <h2>How we protect your information</h2>
    <p>We use reasonable administrative, technical and physical safeguards to protect the information you share with us. No method of transmission over the internet is completely secure, so please avoid sending sensitive information such as Social Security or bank account numbers through our website forms.</p>
    <h2>Your choices</h2>
    <p>You may ask us to update or delete the contact information you've submitted, or to stop contacting you, at any time by emailing <a href="mailto:{SITE['email']}">{SITE['email']}</a> or calling <a href="tel:{SITE['tel']}">{SITE['phone']}</a>. If you receive a text message from us, you can reply STOP to opt out.</p>
    <h2>Children's privacy</h2>
    <p>Our website is intended for adults and is not directed to children under 13. We do not knowingly collect personal information from children.</p>
    <h2>Changes to this policy</h2>
    <p>We may update this policy from time to time. The effective date at the top of this page shows when it was last revised.</p>
    <h2>Contact us</h2>
    <p>Trailmark Insurance Advisors<br>{ADDR_HTML}<br><a href="tel:{SITE['tel']}">{SITE['phone']}</a> · <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
  </div>
</section>
</main>
""" + footer()
    write("privacy/index.html", body)

def build_404():
    body = head("Page Not Found | Trailmark Insurance Advisors", "The page you're looking for couldn't be found.", "/404.html").replace('content="index, follow, max-image-preview:large"', 'content="noindex"') + header() + f"""
<main id="main">
{page_hero("404", "This Trail Doesn't Go Anywhere", "The page you're looking for may have moved. Try one of these instead.", [("Home","/"),("Page not found","/404.html")])}
<section class="section"><div class="container">{product_grid()}</div></section>
</main>
""" + footer()
    write("404.html", body)

# ---------------------------------------------------------------- SEO FILES
def build_seo_files():
    pages = [("/", "1.0"), ("/products/", "0.9")] + [(f"/products/{p['slug']}/", "0.9") for p in PRODUCTS] + \
            [("/news-and-insights/", "0.8")] + [(f"/news-and-insights/{b['slug']}/", "0.7") for b in POSTS] + \
            [("/faq/", "0.8"), ("/contact/", "0.8"), ("/privacy/", "0.3")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{U}{p}</loc><lastmod>{SITE['updated']}</lastmod><priority>{pr}</priority></url>\n" for p, pr in pages) + "</urlset>\n"
    write("sitemap.xml", sm)

    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "anthropic-ai", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot", "CCBot", "Meta-ExternalAgent"]
    rb = "# texastrailmark.com: search engines and AI assistants are welcome.\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + \
         f"User-agent: *\nAllow: /\n\nSitemap: {U}/sitemap.xml\n"
    write("robots.txt", rb)

    prod_lines = "\n".join(f"- [{p['name']}]({U}/products/{p['slug']}/): {strip(p['card'])}" for p in PRODUCTS)
    post_lines = "\n".join(f"- [{b['title']}]({U}/news-and-insights/{b['slug']}/): {b['excerpt']}" for b in POSTS)
    faq_lines = "\n".join(f"**Q: {q}**\nA: {strip(a)}\n" for q, a in GENERAL_FAQ)
    llms = f"""# Trailmark Insurance Advisors

> Trailmark Insurance Advisors is an independent, Texas-owned insurance agency in Denton, Texas. Insurance advisor Eric Glenn compares auto, home, renters, condo and townhome, motorcycle, landlord, jewelry, umbrella, boat, business and RV insurance from multiple insurance companies for families and businesses in Denton County, the Dallas–Fort Worth area and throughout Texas. Quotes and coverage reviews are free.

## Key facts
- Business name: Trailmark Insurance Advisors
- Type: Independent insurance agency (works with multiple carriers, not a captive agent of one company)
- Advisor: Eric Glenn, Insurance Advisor
- Address: {SITE['street']}, Denton, TX {SITE['zip']}
- Phone: {SITE['phone']}
- Email: {SITE['email']}
- Website: {U}/
- Phone hours: Monday–Friday, 9:00 AM–5:00 PM Central Time
- Office visits: By appointment only
- Cost to work with us: Free. No fee for quotes, advice or coverage reviews; the agency is paid a commission by the insurance company the client chooses.
- Pricing: Insurance premiums are set by each carrier and depend on the person, property and coverage. We do not publish prices; request a free quote for exact pricing.
- Service area: {", ".join(AREAS)}, and all of Texas
- Get a quote: {U}/contact/#quote

## Insurance products
{prod_lines}

## Main pages
- [Home]({U}/): Overview of Trailmark Insurance Advisors, products, service area and free quote form
- [Our Products]({U}/products/): All insurance products in one place
- [News & Insights]({U}/news-and-insights/): Plain-English insurance guides for North Texas
- [FAQ]({U}/faq/): Common questions about working with Trailmark and about coverage
- [Contact]({U}/contact/): Phone, email, office address, map and quote request form
- [Privacy Policy]({U}/privacy/)

## News & Insights articles
{post_lines}

## Frequently asked questions
{faq_lines}"""
    write("llms.txt", llms)

# ---------------------------------------------------------------- CSS / JS
def build_assets():
    css = open(os.path.join(HERE, "base.css")).read()
    css = css.replace(".reveal{opacity:0;", "html.js .reveal{opacity:0;").replace(".reveal.in{opacity:1;", "html.js .reveal.in{opacity:1;")
    css = css.replace("@media (prefers-reduced-motion:reduce){.reveal{", "@media (prefers-reduced-motion:reduce){html.js .reveal{")
    css = css.replace(".nav-links{display:flex;align-items:center;gap:34px}", ".nav-links{display:flex;align-items:center;gap:28px}")
    css = css.replace("transform:translateY(-130%);visibility:hidden;transition:transform .3s,visibility .3s;z-index:-1}",
                      "transform:translateY(-130%);visibility:hidden;transition:transform .3s,visibility .3s;z-index:-1;max-height:calc(100vh - 86px);overflow-y:auto}")
    css = "/* Trailmark Insurance Advisors - shared styles */\n" + css + open(os.path.join(HERE, "extra.css")).read()
    write("css/trailmark.css", css)
    write("js/trailmark.js", open(os.path.join(HERE, "site.js")).read())

if __name__ == "__main__":
    build_assets()
    build_home(); build_products_hub()
    for p in PRODUCTS: build_product(p)
    build_blog_index()
    for b in POSTS: build_post(b)
    build_faq(); build_contact(); build_privacy(); build_404(); build_seo_files()
    print("built")
