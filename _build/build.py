# -*- coding: utf-8 -*-
"""Builds texastrailmark.com as a static multi-page site with clean URLs."""
import json, os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from content import SITE, AREAS, PRODUCTS, GENERAL_FAQ, POSTS, CARRIERS

OUT = sys.argv[1]
HERE = os.path.dirname(__file__)
U = SITE["url"]
P = {p["slug"]: p for p in PRODUCTS}
QL = f'href="{SITE["quote"]}" target="_blank" rel="noopener"'
CL = f'href="{SITE["client"]}" target="_blank" rel="noopener"'

def esc(s): return html.escape(s, quote=True)
def strip(s): return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")
def write(path, text):
    if path.endswith(".html"):
        # Every "get a quote" link goes to the EZLynx Consumer Quoting portal.
        text = re.sub(r'href="/contact/(?:\?coverage=\w+)?#quote"', QL, text)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or OUT, exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)

def nice_date(d):
    y, m, dd = d.split("-")
    return ["January","February","March","April","May","June","July","August","September","October","November","December"][int(m)-1] + f" {int(dd)}, {y}"
def img(slug, card=False): return f"/images/products/{slug}-denton-tx{'-card' if card else ''}.jpg"

# ---------------------------------------------------------------- icons
I = {
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h4"/></svg>',
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
        "legalName": "Trailmark Insurance Advisors LLC",
        "description": "Independent insurance agency in Denton, Texas, working with Progressive, Travelers, Liberty Mutual, The Hartford and National General, offering auto, home, renters, condo and townhome, motorcycle, landlord, jewelry, umbrella, boat, business and RV insurance from multiple carriers.",
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
      <a {CL} class="tb-client">{I['lock']}Client Login</a>
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
      <a {CL} class="nav-client">{I['lock']} Client Center Login</a>
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
      <p>Trailmark Insurance Advisors is an independent, Texas-owned insurance agency in Denton, TX. We compare auto, home, renters, business and specialty insurance from carriers like Progressive, Travelers, Liberty Mutual, The Hartford and National General for families and businesses across Denton County, Dallas–Fort Worth and all of Texas.</p>
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
        <li><a {CL}>Client Center Login</a></li>
        <li><a href="/privacy-policy/">Privacy Policy</a></li>
        <li><a href="/terms/">Text Messaging Terms</a></li>
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
    <span>© <span class="yr">2026</span> Trailmark Insurance Advisors LLC · Denton, Texas · <a href="/privacy-policy/">Privacy Policy</a> · <a href="/terms/">Terms</a></span>
    <span>Coverage is subject to policy terms, underwriting and availability. Information on this site is general and not a guarantee of coverage.</span>
  </div>
</footer>
<div class="sticky-cta">
  <a href="/contact/#quote" class="btn btn-gold">Get a Free Quote</a>
  <a href="tel:{SITE['tel']}" class="sticky-call" aria-label="Call {SITE['phone']}">{I['phone']}</a>
</div>
<script src="/js/trailmark.js" defer></script>
</body>
</html>
"""

def page_hero(eyebrow, h1, lead, crumbs, image=None, alt="", ctas=""):
    cr = ' <span>/</span> '.join(f'<a href="{h}">{n}</a>' if i < len(crumbs)-1 else f'<b>{n}</b>' for i, (n, h) in enumerate(crumbs))
    pic = f'<div class="ph-img"><img src="{image}" alt="{esc(alt)}" width="1400" height="1050" fetchpriority="high"></div>' if image else ""
    return f"""<section class="page-hero{' with-img' if image else ''}">
  <div class="container">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p>{lead}</p>
      {ctas}
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
      <form class="quote-form" data-endpoint="{SITE['formspree']}" enctype="multipart/form-data" novalidate>
        <input type="hidden" name="_subject" value="New message for Eric from texastrailmark.com">
        <input type="hidden" name="source_page" value="{source}">
        <h3>Talk With Eric</h3>
        <p>Ask a question or request a free review of your current policy. No obligation.</p>
        <div class="fgrid">
          <div class="field"><label for="fname">First Name *</label><input id="fname" name="first_name" required autocomplete="given-name"></div>
          <div class="field"><label for="lname">Last Name *</label><input id="lname" name="last_name" required autocomplete="family-name"></div>
          <div class="field"><label for="email">Email *</label><input id="email" name="email" type="email" required autocomplete="email"></div>
          <div class="field"><label for="phone">Phone *</label><input id="phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="field"><label for="zip">ZIP Code</label><input id="zip" name="zip" inputmode="numeric" maxlength="5" autocomplete="postal-code"></div>
          <div class="field"><label for="contact_pref">Best Way to Reach You</label>
            <select id="contact_pref" name="contact_preference"><option>Phone call</option><option>Text message</option><option>Email</option></select></div>
          <div class="field full"><span class="lbl">What Can Eric Help With?</span>
            <div class="chips">
{chips}
            </div>
          </div>
          <div class="field full"><label for="policy_file">Attach Your Current Policy <em>(optional)</em></label>
            <label class="file-drop" for="policy_file">{I['doc']}<span class="file-text"><strong>Choose files</strong> or drag them here<small>Your declarations page works best. PDF, JPG or PNG.</small></span></label>
            <input id="policy_file" class="file-input" name="attachment" type="file" accept=".pdf,.jpg,.jpeg,.png,.heic,application/pdf,image/*" multiple>
          </div>
          <div class="field full"><label for="msg">Questions or Details</label><textarea id="msg" name="message" rows="4" placeholder="Current carrier, renewal date, what you'd like Eric to look at…"></textarea></div>
          <div class="field full consent"><label><input type="checkbox" name="sms_consent" value="Yes, I agree to receive customer service text messages"><span>Yes, I'd like to receive customer service text messages from Trailmark Insurance Advisors LLC about my quote requests, appointments, applications, policy servicing and renewals. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe or HELP for help. Consent is not a condition of purchasing insurance. See our <a href="/privacy-policy/">Privacy Policy</a> and <a href="/terms/">Text Messaging Terms</a>.</span></label></div>
        </div>
        <button type="submit" class="btn btn-gold">Send to Eric</button>
        <p class="form-note">By submitting, you agree to be contacted by Trailmark Insurance Advisors LLC about your request. See our <a href="/privacy-policy/">Privacy Policy</a>.</p>
      </form>
      <div class="form-success" role="status">
        {I['check']}
        <h3>Thank you!</h3>
        <p class="ok-msg">Eric received your message and will be in touch soon, usually within one business day.</p>
      </div>
    </div>"""

def contact_info(h2="Prefer to Talk With Eric?", eyebrow="Talk to a Real Person"):
    return f"""<div class="contact-info reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{h2}</h2>
      <p>Have a question, a complicated situation or a policy you'd like a second opinion on? Send Eric a message and attach your current policy if you'd like. He'll review it and reach out, usually within one business day.</p>
      <p class="quote-nudge">Want numbers right now? <a href="/contact/#quote">Start a free online quote {I['arrow']}</a></p>
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
    desc = "Compare Texas home and auto insurance rates from Progressive, Travelers, Liberty Mutual, The Hartford and National General in about 10 minutes. Independent insurance agency in Denton, TX."
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
      <h1>Compare Texas Home &amp; Auto Rates From Top Carriers in <em>About 10 Minutes</em>.</h1>
      <p class="lead">Instead of one company's price, Trailmark shows you quotes from carriers like Progressive, Travelers, Liberty Mutual, The Hartford and National General, plus a local advisor who explains the difference.</p>
      <div class="hero-ctas">
        <a href="/contact/#quote" class="btn btn-gold">Start My Free Quote {I['arrow']}</a>
        <a href="tel:{SITE['tel']}" class="btn btn-outline">{I['phone']} Call {SITE['phone']}</a>
      </div>
      <div class="hero-trust">
        <div>{I['shield']}Licensed in Texas</div>
        <div>{I['users']}Saving clients money since 2020</div>
        <div>{I['chart']}Multiple top-rated carriers</div>
      </div>
      <p class="hero-client">Already a client? <a {CL}>Log in to the Client Center {I['arrow']}</a></p>
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

<section class="review-band">
  <div class="container">
    <div class="rb-ico">{I['doc']}</div>
    <div class="rb-text">
      <h2>Paying too much for insurance?</h2>
      <p>Send Eric your current policy and he'll compare it against multiple carriers for free. No obligation, no pressure.</p>
    </div>
    <div class="rb-ctas">
      <a href="/contact/#talk" class="btn btn-navy">Send My Policy for a Free Review</a>
      <a href="/contact/#quote" class="rb-alt">Or compare quotes online now {I['arrow']}</a>
    </div>
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
    <div class="reveal">
      <div class="stats">
        <div class="stat"><strong>$5,726</strong><span>Most saved for one client in a year on home &amp; auto*</span></div>
        <div class="stat"><strong>2020</strong><span>Saving Texans money on insurance since</span></div>
        <div class="stat"><strong>10 min</strong><span>Typical time to compare quotes online</span></div>
        <div class="stat"><strong>$0</strong><span>Cost for a quote or policy review</span></div>
      </div>
      <p class="stat-note">*Based on one client's annual home and auto premiums before and after switching. Individual savings vary.</p>
    </div>
  </div>
</section>
{carriers_band()}
<section class="section" id="how">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How It Works</span>
      <h2>Better Coverage in Three Simple Steps</h2>
      <div class="rule"></div>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="circle">1</div><h3>Start Your Quote</h3><p>Answer a few questions online in about 10 minutes, or call us and we'll do it together.</p></div>
      <div class="step reveal"><div class="circle">2</div><h3>Compare Carriers</h3><p>See coverage and pricing from multiple top-rated insurance companies side by side.</p></div>
      <div class="step reveal"><div class="circle">3</div><h3>Pick &amp; Get Protected</h3><p>Eric walks you through your options, you choose, and we handle the paperwork.</p></div>
    </div>
    <div class="center-cta reveal"><a href="/contact/#quote" class="btn btn-gold">Start My Free Quote {I['arrow']}</a></div>
  </div>
</section>

<section class="section about" id="about">
  <div class="container">
    <div class="about-img reveal">
      <img src="/images/eric-glenn-square.jpg" alt="Eric Glenn, insurance advisor at Trailmark Insurance Advisors in Denton, Texas" width="900" height="900" loading="lazy">
      <span class="tag">Texas Owned &amp; Operated</span>
    </div>
    <div class="reveal">
      <span class="eyebrow">Meet Your Advisor</span>
      <h2>Hi, I'm Eric Glenn.</h2>
      <p>I've been helping Texas families and business owners save money on home, auto, condo, renters, landlord, motorcycle and business insurance since 2020. My biggest win so far: saving one client $5,726 a year on their home and auto.</p>
      <p>I started Trailmark so my clients would always get to compare. As an independent agency, I can shop your coverage with carriers like Progressive, Travelers, Liberty Mutual, The Hartford and National General, so I can match you with the right coverage at the best available price instead of fitting you into one company's box.</p>
      <ul class="checks">
        <li>{I['check']}Licensed Texas agent</li>
        <li>{I['check']}Independent &amp; unbiased</li>
        <li>{I['check']}Personal &amp; commercial lines</li>
        <li>{I['check']}Free annual policy reviews</li>
      </ul>
      <a href="/contact/#talk" class="btn btn-navy">Talk With Eric</a>
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
<section class="section contact" id="talk">
  <div class="container">
    {contact_info()}
    {quote_form("Home page")}
  </div>
</section>
</main>
""" + footer()
    write("index.html", body)

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
{carriers_band()}
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
    ctas = f'<div class="hero-ctas ph-ctas"><a href="/contact/#quote" class="btn btn-gold">Get a Free {p["short"]} Quote {I["arrow"]}</a><a href="/contact/#talk" class="btn btn-outline-light">Talk With Eric</a></div>'
    body = head(p["title"], p["desc"], path, image=img(p["slug"]), schema=schema) + header("products") + f"""
<main id="main">
{page_hero("Independent Insurance Agency · Denton, TX", p["h1"], p["lead"], crumbs, img(p["slug"]), p["alt"], ctas)}
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
      <div class="callout">Ready to compare {p['name'].lower()} rates? <a href="/contact/#quote">Start your free online quote</a> or call <a href="tel:{SITE['tel']}">{SITE['phone']}</a>. Have questions first, or want Eric to review your current policy? <a href="/contact/#talk">Send Eric a message</a>.</div>
    </article>
    <aside class="side">
      <div class="side-card navy">
        <h3>Get a Free {p['short']} Quote</h3>
        <p>Compare rates from multiple top-rated carriers in about 10 minutes. No obligation.</p>
        <a href="/contact/#quote" class="btn btn-gold">Start My Quote</a>
        <a href="tel:{SITE['tel']}" class="side-phone">{I['phone']} {SITE['phone']}</a>
        <small>Phone: Mon–Fri, 9 AM – 5 PM</small>
        <a href="/contact/#talk" class="side-talk">Prefer to talk first? Message Eric →</a>
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
{carriers_band()}
{cta_band(f"Protect What Matters With the Right {p['short']} Coverage", "Get a free, no-obligation quote from a local, independent advisor in Denton.")}
</main>
""" + footer()
    write(f"products/{p['slug']}/index.html", body)

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
      <div class="author-box"><img src="/images/eric-glenn-square.jpg" alt="Eric Glenn" width="88" height="88" loading="lazy"><div><strong>About the author</strong><p>Eric Glenn is an insurance advisor with Trailmark Insurance Advisors, an independent, Texas-owned agency at {SITE['street']} in Denton. He has been helping Texans save money on insurance since 2020 and compares coverage from carriers like Progressive, Travelers, Liberty Mutual, The Hartford and National General for families and businesses across Denton County and North Texas. Reach him at <a href="tel:{SITE['tel']}">{SITE['phone']}</a> or <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p></div></div>
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
    desc = "Contact Trailmark Insurance Advisors at 3616 Duchess Dr, Ste. 120, Denton, TX 76205. Call (214) 531-7932, start a free online quote, or send Eric your current policy for a free review."
    crumbs = [("Home", "/"), ("Contact", "/contact/")]
    cp = {"@type": "ContactPage", "url": U + "/contact/", "name": "Contact Trailmark Insurance Advisors", "about": {"@id": U + "/#agency"}}
    schema = ld(org_schema(), crumbs_schema(crumbs), cp)
    q = "3616+Duchess+Dr+Ste+120,+Denton,+TX+76205"
    body = head(title, desc, "/contact/", schema=schema) + header("contact") + f"""
<main id="main">
{page_hero("Contact Us", "Contact Trailmark Insurance Advisors", "Start a free online quote, send Eric a question or a policy to review, or log in to manage an existing policy.", crumbs)}
<section class="section choices">
  <div class="container">
    <div class="choice-grid">
      <div class="choice reveal featured"><div class="ico">{I['chart']}</div><h2 class="h3">Compare Quotes Online</h2><p>See real rates from multiple top-rated carriers in about 10 minutes.</p><a href="/contact/#quote" class="btn btn-gold">Start My Free Quote</a></div>
      <div class="choice reveal"><div class="ico">{I['chat']}</div><h2 class="h3">Talk With Eric</h2><p>Questions, or a current policy you'd like reviewed? Send a message below.</p><a href="#talk" class="btn btn-outline">Send a Message</a></div>
      <div class="choice reveal"><div class="ico">{I['lock']}</div><h2 class="h3">Already a Client?</h2><p>View your policies and request service in our secure Client Center.</p><a {CL} class="btn btn-navy">Client Center Login</a></div>
    </div>
  </div>
</section>
<section class="section contact" id="talk">
  <div class="container">
    {contact_info()}
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

def build_privacy():
    E = f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>'
    legal_page("/privacy-policy/", "Privacy Policy | Trailmark Insurance Advisors LLC",
        "How Trailmark Insurance Advisors LLC collects, uses, shares and protects your information, including text messaging privacy.",
        "Privacy Policy", "Trailmark Insurance Advisors LLC", f"""
    <p>We collect information you provide when requesting insurance information, obtaining a quote, contacting our agency, or receiving policy assistance. This may include your name, email address, telephone number, mailing address, and information needed to quote or service insurance.</p>
    <p>We use this information to respond to requests, obtain insurance quotes, assist with applications, service policies, and communicate about appointments, coverage, and renewals.</p>
    <p>We may share information as necessary with insurance carriers and service providers to obtain quotes, process applications, and service insurance, or as required by law.</p>
    <h2>Text Messaging Privacy</h2>
    <p>No mobile information will be shared with third parties or affiliates for marketing or promotional purposes. Text messaging originator opt-in data and consent will not be shared with third parties, except service providers necessary to deliver our text messaging services.</p>
    <p>We use text messaging for customer service communications, including requested quotes, appointment reminders, policy updates, and renewal reminders. We do not send promotional offers by text.</p>
    <h2>Information Protection</h2>
    <p>We use reasonable administrative and technical safeguards to protect personal information. No method of electronic transmission or storage is completely secure.</p>
    <h2>Your Choices</h2>
    <p>You may contact us to request access to or correction of information you have provided, subject to applicable recordkeeping requirements.</p>
    <p>To stop text messages, reply STOP. For assistance, reply HELP or email {E}.</p>
    <h2>Contact</h2>
    <p>Trailmark Insurance Advisors LLC<br>Email: {E}</p>
    <p>We may update this policy by posting a revised version on this page.</p>
    <p class="legal-links">See also: <a href="/terms/">Text Messaging Terms &amp; Conditions</a></p>""")
    # Old address -> forward to the new one
    write("privacy/index.html", f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Privacy Policy | Trailmark Insurance Advisors LLC</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{U}/privacy-policy/">
<meta http-equiv="refresh" content="0; url=/privacy-policy/"></head>
<body><p>Our Privacy Policy has moved to <a href="/privacy-policy/">texastrailmark.com/privacy-policy</a>.</p></body></html>
""")

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
            [("/faq/", "0.8"), ("/contact/", "0.8"), ("/privacy-policy/", "0.3"), ("/terms/", "0.3")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{U}{p}</loc><lastmod>{SITE['updated']}</lastmod><priority>{pr}</priority></url>\n" for p, pr in pages) + "</urlset>\n"
    write("sitemap.xml", sm)

    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "anthropic-ai", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended", "DuckDuckBot", "CCBot", "Meta-ExternalAgent"]
    rb = "# texastrailmark.com: search engines and AI assistants are welcome.\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + \
         f"User-agent: *\nAllow: /\n\nSitemap: {U}/sitemap.xml\n"
    write("robots.txt", rb)

    carriers = ", ".join(c[1] + (" (an Allstate company)" if c[0] == "national-general" else "") for c in CARRIERS)
    prod_lines = "\n".join(f"- [{p['name']}]({U}/products/{p['slug']}/): {strip(p['card'])}" for p in PRODUCTS)
    post_lines = "\n".join(f"- [{b['title']}]({U}/news-and-insights/{b['slug']}/): {b['excerpt']}" for b in POSTS)
    faq_lines = "\n".join(f"**Q: {q}**\nA: {strip(a)}\n" for q, a in GENERAL_FAQ)
    llms = f"""# Trailmark Insurance Advisors

> Trailmark Insurance Advisors LLC is an independent, Texas-owned insurance agency in Denton, Texas. Insurance advisor Eric Glenn, who has been helping Texans save money on insurance since 2020, compares auto, home, renters, condo and townhome, motorcycle, landlord, jewelry, umbrella, boat, business and RV insurance from carriers including {carriers}. Online quotes take about 10 minutes, and quotes and policy reviews are free.

## Key facts
- Business name: Trailmark Insurance Advisors LLC
- Type: Independent insurance agency (works with multiple carriers, not a captive agent of one company)
- Insurance carriers: {carriers}
- Advisor: Eric Glenn, Insurance Advisor, helping clients save on insurance since 2020
- Largest single-client savings to date: $5,726 per year on home and auto combined (individual savings vary)
- Address: {SITE['street']}, Denton, TX {SITE['zip']}
- Phone: {SITE['phone']}
- Email: {SITE['email']}
- Website: {U}/
- Phone hours: Monday–Friday, 9:00 AM–5:00 PM Central Time
- Office visits: By appointment only
- Get an online quote (about 10 minutes): {SITE['quote']}
- Existing clients – Client Center (view and service policies): {SITE['client']}
- Talk with Eric or send a current policy for a free review: {U}/contact/#talk
- Cost to work with us: Free. No fee for quotes, advice or policy reviews; the agency is paid a commission by the insurance company the client chooses.
- Pricing: Premiums are set by each carrier and depend on the person, property and coverage. We do not publish prices; request a free quote for exact pricing.
- Service area: {", ".join(AREAS)}, and all of Texas

## Insurance products
{prod_lines}

## Main pages
- [Home]({U}/): Overview, carriers, products, service area and contact form
- [Our Products]({U}/products/): All insurance products in one place
- [News & Insights]({U}/news-and-insights/): Plain-English insurance guides for North Texas
- [FAQ]({U}/faq/): Common questions about working with Trailmark and about coverage
- [Contact]({U}/contact/): Online quote, message Eric, Client Center, office address and map
- [Privacy Policy]({U}/privacy-policy/)
- [Text Messaging Terms & Conditions]({U}/terms/)

## News & Insights articles
{post_lines}

## Frequently asked questions
{faq_lines}"""
    write("llms.txt", llms)

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

def carriers_band(h="Compare rates from carriers you know"):
    def items(hidden):
        ah = ' aria-hidden="true"' if hidden else ""
        out = ""
        for slug, name, hh, w in CARRIERS:
            alt = "" if hidden else name
            out += f'<li{ah}><img src="/images/carriers/{slug}.png" alt="{alt}" width="{round(w*hh/120)}" height="{hh}" style="height:{hh}px" loading="lazy"></li>'
        return out
    return f"""<section class="carriers" aria-label="Insurance carriers we work with">
  <div class="container"><p class="carriers-h">{h}</p></div>
  <div class="marquee"><ul class="track">{items(False)}{items(True)}{items(True)}{items(True)}</ul></div>
</section>
"""

def legal_page(path, title, desc, h1, sub, body_html):
    crumbs = [("Home", "/"), (h1, path)]
    schema = ld(org_schema(), crumbs_schema(crumbs))
    body = head(title, desc, path, schema=schema) + header() + f"""
<main id="main">
{page_hero("Trailmark Insurance Advisors LLC", h1, sub, crumbs)}
<section class="section">
  <div class="container narrow prose legal">
{body_html}
  </div>
</section>
</main>
""" + footer()
    write(path.strip("/") + "/index.html", body)

def build_terms():
    E = f'<a href="mailto:{SITE["email"]}">{SITE["email"]}</a>'
    legal_page("/terms/", "Text Messaging Terms & Conditions | Trailmark Insurance Advisors LLC",
        "Text messaging terms and conditions for the Trailmark Insurance Advisors Customer Service Text Messaging program.",
        "Text Messaging Terms &amp; Conditions", "Trailmark Insurance Advisors LLC", f"""
    <h2>Program Name</h2>
    <p>Trailmark Insurance Advisors Customer Service Text Messaging.</p>
    <h2>Program Description</h2>
    <p>By opting in, you agree to receive customer service text messages from Trailmark Insurance Advisors LLC related to insurance quote requests, appointments, applications, policy servicing, and renewals. We do not send promotional offers through this program.</p>
    <h2>Message Frequency and Charges</h2>
    <p>Messages may be recurring. Message frequency varies based on your requests and insurance servicing needs.</p>
    <p>Message and data rates may apply.</p>
    <h2>Consent</h2>
    <p>Consent to receive text messages is not a condition of purchasing insurance. You may contact our agency by email for assistance without enrolling in text messaging.</p>
    <h2>Opting Out and Getting Help</h2>
    <p>Reply STOP at any time to unsubscribe. You may receive a final message confirming your opt-out, after which no further messages will be sent unless you opt in again.</p>
    <p>Reply HELP for assistance, or email {E}.</p>
    <h2>Carrier Disclaimer</h2>
    <p>Carriers are not liable for delayed or undelivered messages.</p>
    <h2>Privacy</h2>
    <p>Please review our <a href="/privacy-policy/">Privacy Policy</a> for information about how we collect, use, and protect your information.</p>
    <h2>Insurance Requests</h2>
    <p>Text messages do not bind, change, or cancel insurance coverage. Coverage requests require confirmation from an authorized agency representative or insurance carrier.</p>""")

if __name__ == "__main__":
    build_assets()
    build_home(); build_products_hub()
    for p in PRODUCTS: build_product(p)
    build_blog_index()
    for b in POSTS: build_post(b)
    build_faq(); build_contact(); build_privacy(); build_terms(); build_404(); build_seo_files()
    print("built")
