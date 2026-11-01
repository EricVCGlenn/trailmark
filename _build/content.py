# -*- coding: utf-8 -*-
# All written content for texastrailmark.com lives here. build.py turns it into pages.

SITE = {
    "name": "Trailmark Insurance Advisors",
    "url": "https://texastrailmark.com",
    "phone": "(214) 531-7932",
    "tel": "+12145317932",
    "email": "eric@texastrailmark.com",
    "street": "3616 Duchess Dr, Ste. 120",
    "city": "Denton",
    "region": "TX",
    "zip": "76205",
    "advisor": "Eric Glenn",
    "formspree": "https://formspree.io/f/mvkzywbz",
    "updated": "2026-11-01",
    "quote": "https://www.agentinsure.com/compare/auto-insurance-home-insurance/trailmarkins/quote.aspx",
    "client": "https://customerservice.agentinsure.com/EzlynxCustomerService/trailmarkins/Account/LogIn",
}

# (file slug, name, display height px, source width at 120px tall)
CARRIERS = [("progressive", "Progressive", 30, 956), ("travelers", "Travelers", 38, 588), ("liberty-mutual", "Liberty Mutual", 44, 472),
            ("the-hartford", "The Hartford", 38, 613), ("national-general", "National General", 56, 219)]

AREAS = ["Denton", "Corinth", "Lake Dallas", "Hickory Creek", "Argyle", "Flower Mound",
         "Highland Village", "Lewisville", "Little Elm", "Aubrey", "Sanger", "Krum",
         "Justin", "Northlake", "Prosper", "Frisco", "The Colony", "Carrollton"]

# ---------------------------------------------------------------- PRODUCTS
# Each "covers" item is (heading, text). HTML is allowed in text fields.
PRODUCTS = [
dict(
 slug="auto-insurance", cov="Auto", name="Auto Insurance", short="Auto",
 title="Auto Insurance in Denton, TX | Compare Car Insurance Quotes | Trailmark",
 desc="Compare car insurance quotes from multiple carriers with Trailmark, an independent insurance agency in Denton, TX. Liability, full coverage and bundle discounts across North Texas.",
 h1="Auto Insurance in Denton, Texas",
 alt="Smiling family standing beside their gray SUV in the driveway of their North Texas home",
 lead="Car insurance that fits the way you drive, compared across multiple top-rated carriers by a local, independent advisor.",
 card="Liability, full coverage and everything in between, with discounts for safe drivers, multiple vehicles and bundling.",
 intro=["Whether you commute down I-35E to Dallas, drive the kids across Denton County or put miles on a work truck, your auto policy is one of the most important protections you own. At Trailmark Insurance Advisors, Eric Glenn compares car insurance quotes from multiple insurance companies so you get the right coverage at a competitive price, without calling around yourself.",
        "Because we're an independent insurance agency, we aren't tied to one company. If your rate jumps at renewal, we can shop your policy again and look for a better fit."],
 covers=[("Liability (bodily injury and property damage)", "Pays for injuries and damage you cause to others. Texas requires at least 30/60/25 coverage: $30,000 per injured person, $60,000 per accident and $25,000 for property damage. Many drivers choose higher limits to protect their savings and home."),
         ("Collision", "Repairs or replaces your vehicle after an accident with another car or object, regardless of who caused it."),
         ("Comprehensive", "Covers hail, flood, fire, theft, vandalism and hitting a deer. It's a must-have for North Texas hail season."),
         ("Uninsured and underinsured motorist", "Protects you when the other driver has no insurance, or not enough to pay for your injuries and repairs."),
         ("Personal Injury Protection (PIP)", "Helps pay medical bills and lost wages for you and your passengers, no matter who caused the accident. Texas insurers must offer PIP unless you reject it in writing."),
         ("Helpful extras", "Rental reimbursement, roadside assistance and towing, and gap coverage for financed or leased vehicles.")],
 texas_h="Car Insurance Built for Texas Roads",
 texas="<p>Texas drivers face a unique mix of risks: heavy traffic on I-35, US-380 and the Dallas North Tollway, sudden spring hailstorms, flash flooding and deer on rural roads around Denton, Sanger and Krum. A state-minimum policy may keep you legal, but it often isn't enough to pay for a serious accident.</p><p>We'll walk you through liability limits, deductibles and optional coverages in plain English, so you know exactly what you're buying and why.</p>",
 save_h="Ways to Save on Car Insurance",
 save=["Bundle auto with home, renters or condo insurance", "Insure multiple vehicles on one policy", "Safe-driver and claims-free discounts", "Good-student discounts for teen and college drivers", "Defensive driving course discounts, where the carrier offers them", "Paid-in-full, paperless and automatic-payment discounts", "Usage-based (telematics) programs that reward safe driving"],
 faqs=[("What is the minimum car insurance required in Texas?", "Texas requires liability coverage of at least $30,000 per injured person, $60,000 per accident and $25,000 for property damage, often written as 30/60/25. Most advisors recommend higher limits, because medical bills and vehicle repairs can quickly exceed those amounts."),
       ("Is full coverage worth it on an older car?", "It depends on the car's value and how easily you could replace it. We'll compare the cost of collision and comprehensive against your vehicle's value and help you decide. Many Texas drivers keep comprehensive for hail protection even on older cars."),
       ("Can I switch car insurance companies before my policy renews?", "Usually, yes. Most carriers let you cancel mid-term and refund any unused premium. We'll line up your new policy first so there's never a gap in coverage.")],
 related=["home-insurance", "umbrella-insurance", "motorcycle-insurance"],
),
dict(
 slug="home-insurance", cov="Home", name="Home Insurance", short="Home",
 title="Homeowners Insurance in Denton, TX | Home Insurance Quotes | Trailmark",
 desc="Protect your Texas home from hail, wind, fire and theft. Trailmark compares homeowners insurance quotes from multiple carriers for Denton, Flower Mound and North Texas homeowners.",
 h1="Homeowners Insurance in Denton, Texas",
 alt="Two-story brick and stone home with a green lawn and two-car garage in a Denton County neighborhood",
 lead="Protect your home, your belongings and your family's financial future with a homeowners policy built for North Texas weather.",
 card="Protect your house, belongings and liability against Texas hail, wind, fire and theft with the right deductible for you.",
 intro=["Your home is likely your biggest investment, and in North Texas it faces hailstorms, high winds, severe thunderstorms and the occasional ice storm. Trailmark Insurance Advisors helps homeowners in Denton, Corinth, Argyle, Flower Mound and across Denton County compare homeowners insurance from multiple carriers, so they get strong coverage at a fair price.",
        "We look beyond the premium. Roof coverage, wind and hail deductibles and replacement cost can make a huge difference when you file a claim, so we explain each choice before you buy."],
 covers=[("Dwelling", "Repairs or rebuilds the structure of your home after a covered loss such as fire, wind or hail."),
         ("Other structures", "Covers detached garages, fences, sheds and other structures on your property."),
         ("Personal property", "Protects furniture, electronics, clothing and other belongings, at home or while you travel."),
         ("Loss of use", "Pays additional living expenses, like a hotel and meals, if a covered loss forces you out of your home."),
         ("Personal liability", "Protects you if someone is injured on your property or you accidentally damage someone else's property."),
         ("Medical payments", "Helps pay minor medical bills for guests injured at your home, regardless of fault.")],
 texas_h="What Texas Homeowners Should Know",
 texas="<p>Not all homeowners policies are created equal, especially in Texas. Before you buy, ask about:</p><ul><li><strong>Wind and hail deductibles.</strong> Many Texas policies use a separate deductible for wind and hail, often a percentage of your dwelling coverage (such as 1% or 2%) instead of a flat dollar amount.</li><li><strong>Roof coverage.</strong> Some policies pay replacement cost for your roof, while others pay actual cash value, which subtracts depreciation. This matters most on older roofs.</li><li><strong>Replacement cost vs. actual cash value</strong> for your belongings.</li><li><strong>Water backup</strong> from drains and sewers, which usually requires an added endorsement.</li><li><strong>Flood.</strong> Standard homeowners policies exclude flood damage. Flood insurance is a separate policy, so ask us about your options.</li></ul>",
 save_h="Ways to Save on Home Insurance",
 save=["Bundle home and auto insurance", "A newer roof or impact-resistant (Class 4) shingles", "Monitored security and fire alarm systems", "Updated plumbing, electrical and HVAC systems", "Claims-free discounts", "A deductible that balances your premium and out-of-pocket risk"],
 faqs=[("Does homeowners insurance cover hail damage in Texas?", "Most Texas homeowners policies cover hail damage to your roof, siding and windows, but the details matter. Check whether your policy has a separate wind and hail deductible and whether your roof is covered at replacement cost or actual cash value."),
       ("How much homeowners insurance do I need?", "Your dwelling coverage should reflect what it would cost to rebuild your home at today's labor and material prices, not its market value or purchase price. We'll help estimate a rebuild cost and set liability limits that protect your assets."),
       ("Does homeowners insurance cover foundation problems?", "Settling and cracking caused by North Texas clay soil are generally not covered. Some policies offer limited coverage for foundation damage caused by a sudden plumbing leak. We'll show you how each policy handles it.")],
 related=["auto-insurance", "umbrella-insurance", "jewelry-insurance"],
),
dict(
 slug="renters-insurance", cov="Renters", name="Renters Insurance", short="Renters",
 title="Renters Insurance in Denton, TX | Affordable Apartment Insurance | Trailmark",
 desc="Affordable renters insurance for apartments, rental homes and student housing in Denton, TX. Protect your belongings and liability. Great for UNT and TWU students. Free quotes.",
 h1="Renters Insurance in Denton, Texas",
 alt="Three-story brick and stone apartment building with balconies and landscaping in Denton, Texas",
 lead="Your landlord's insurance covers the building, not your stuff. Renters insurance protects your belongings and your liability for less than you might think.",
 card="Affordable coverage for your belongings and personal liability, often just a few dollars a month when bundled with auto.",
 intro=["Whether you rent an apartment near the Denton Square, a house in Corinth or student housing near the University of North Texas or Texas Woman's University, renters insurance (also called an HO-4 policy) protects the things you own and the liability you carry.",
        "Many apartment communities in North Texas require proof of renters insurance before you move in. Trailmark makes it easy to get a policy quickly, and bundling it with your auto insurance can often lower your total cost."],
 covers=[("Personal property", "Covers clothing, furniture, laptops, phones, bikes and more against fire, smoke, theft, vandalism and certain water damage, even when they're away from home."),
         ("Personal liability", "Protects you if a guest is injured in your apartment or you accidentally cause damage, like a kitchen fire that spreads to a neighbor's unit."),
         ("Loss of use", "Pays for temporary housing and extra living costs if your rental becomes unlivable after a covered loss."),
         ("Medical payments to others", "Covers small medical bills for guests hurt in your home."),
         ("Replacement cost option", "Pays to replace items with new ones instead of their depreciated value.")],
 texas_h="Renters Insurance for Students and Young Professionals in Denton",
 texas="<p>Denton is home to the University of North Texas and Texas Woman's University, and thousands of students rent apartments every year. A laptop, gaming system, bike and wardrobe add up fast.</p><p>A parent's homeowners policy may offer limited coverage for a student living away from home, but it often comes with low limits and a high deductible. A renters policy in the student's own name is usually simple and affordable. <a href=\"/news-and-insights/renters-insurance-unt-twu-students-denton/\">Read our renters insurance guide for UNT and TWU students</a>.</p>",
 save_h="Ways to Save on Renters Insurance",
 save=["Bundle renters with auto insurance", "Choose a higher deductible", "Monitored smoke detectors and security systems", "Pay in full or enroll in autopay", "A claims-free history"],
 faqs=[("How much does renters insurance cost in Texas?", "Renters insurance is one of the most affordable types of coverage. Your price depends on how much coverage you choose, your deductible, your location and your claims history. We'll compare options and show you exact quotes for free."),
       ("Does renters insurance cover my roommate?", "Usually not automatically. Each roommate should typically have their own policy unless they're a relative living with you. Ask us how your carrier handles roommates."),
       ("Is renters insurance required in Texas?", "Texas law doesn't require it, but many landlords and apartment communities require it in the lease. Even when it isn't required, it's an inexpensive way to protect your belongings and liability.")],
 related=["auto-insurance", "jewelry-insurance", "condo-insurance"],
),
dict(
 slug="condo-insurance", cov="Condo", name="Townhome & Condo Insurance", short="Townhome & Condo",
 title="Condo & Townhome Insurance in Denton, TX | HO-6 Quotes | Trailmark",
 desc="Condo and townhome insurance (HO-6) for Denton and North Texas owners. Cover your interior, upgrades, belongings, liability and HOA loss assessments. Compare quotes from multiple carriers.",
 h1="Townhome & Condo Insurance in Denton, Texas",
 alt="Row of two-story brick townhomes with a second-floor balcony and shade trees in North Texas",
 lead="Your HOA's master policy covers the building. Your condo or townhome policy fills the gaps: your interior, upgrades, belongings and liability.",
 card="Coverage built for shared walls and HOAs: your interior, upgrades, belongings and liability, plus loss assessment protection.",
 intro=["Owning a condo or townhome in Denton, Lewisville, Flower Mound or anywhere in North Texas means sharing some responsibility with your homeowners association. The HOA's master policy typically insures common areas and parts of the building, while you're responsible for everything the master policy doesn't cover.",
        "A condo insurance policy, often called an HO-6, is designed to fill exactly those gaps. Trailmark reviews your HOA documents and master policy so your coverage fits, with no costly overlaps and no dangerous holes."],
 covers=[("Interior walls, floors and fixtures", "Repairs the parts of your unit you're responsible for under your HOA documents."),
         ("Improvements and upgrades", "Protects the granite countertops, flooring, cabinets and other upgrades you or a previous owner added."),
         ("Personal property", "Covers your furniture, electronics, clothing and other belongings."),
         ("Personal liability", "Protects you if someone is injured inside your unit or you accidentally damage a neighbor's unit."),
         ("Loss assessment", "Helps pay your share when the HOA charges owners for a large claim or a high master-policy deductible."),
         ("Loss of use", "Pays for temporary housing if a covered loss makes your unit unlivable.")],
 texas_h="Condo or Townhome? Why Your HOA Documents Matter",
 texas="<p>Master policies vary. A <strong>bare walls</strong> policy covers only the structure, leaving you responsible for nearly everything inside. A <strong>single entity</strong> policy covers original fixtures but not your upgrades. An <strong>all-in</strong> policy covers more of the interior, including some improvements.</p><p>Townhomes add another wrinkle. In some North Texas communities the HOA insures the building, and a condo-style (HO-6) policy is the right fit. In others you own the structure and land outright and need a full <a href=\"/products/home-insurance/\">homeowners policy</a>. We'll read the fine print with you and recommend the right form.</p>",
 save_h="Ways to Save on Condo Insurance",
 save=["Bundle condo and auto insurance", "Monitored security and smoke detectors", "Claims-free discounts", "The right loss assessment limit for your HOA's deductible"],
 faqs=[("What is HO-6 insurance?", "An HO-6 is a homeowners policy designed for condo owners and some townhome owners. It covers the parts of your unit the HOA's master policy doesn't, plus your belongings, liability and loss assessments."),
       ("Do I need condo insurance if my HOA has a master policy?", "Yes, in almost all cases. The master policy protects the building and common areas, but generally not your belongings, your liability or your interior improvements. Many HOAs and mortgage lenders also require owners to carry their own policy."),
       ("What is loss assessment coverage?", "If your HOA has a large claim or a high master-policy deductible, it may split the cost among owners. Loss assessment coverage helps pay your share.")],
 related=["home-insurance", "renters-insurance", "umbrella-insurance"],
),
dict(
 slug="motorcycle-insurance", cov="Motorcycle", name="Motorcycle Insurance", short="Motorcycle",
 title="Motorcycle Insurance in Denton, TX | Cycle Insurance Quotes | Trailmark",
 desc="Motorcycle insurance for cruisers, sport bikes, touring bikes and scooters in Denton and North Texas. Liability, collision, custom parts and riding gear coverage. Compare quotes free.",
 h1="Motorcycle Insurance in Denton, Texas",
 alt="Motorcyclist riding down an open Texas highway toward the sunset",
 lead="From weekend rides on Texas back roads to daily commutes, get motorcycle coverage that protects you, your bike and your gear.",
 card="Coverage for cruisers, sport bikes and touring bikes, including custom parts, riding gear and roadside help.",
 intro=["North Texas is great riding country, from the farm roads around Lake Ray Roberts to long highway trips across the state. Trailmark Insurance Advisors compares motorcycle insurance from multiple carriers for cruisers, sport bikes, touring bikes, dual-sport bikes, trikes and scooters.",
        "Motorcycle coverage works differently from car insurance, so we'll help you choose the right protection for your bike, your riding style and the custom parts you've added."],
 covers=[("Liability", "Pays for injuries and damage you cause to others. Texas requires the same 30/60/25 minimum liability for motorcycles as for cars."),
         ("Collision", "Repairs or replaces your bike after an accident."),
         ("Comprehensive", "Covers theft, hail, fire, vandalism and animal collisions."),
         ("Uninsured and underinsured motorist", "Protects you when a driver without enough insurance causes an accident."),
         ("Medical payments or PIP", "Helps pay medical bills for you and your passenger."),
         ("Custom parts and equipment", "Protects aftermarket chrome, exhaust, seats, saddlebags and custom paint."),
         ("Riding gear", "Covers helmets, jackets and other protective gear."),
         ("Roadside assistance and trip interruption", "Help with towing and lodging if you break down far from home.")],
 texas_h="Riding in Texas",
 texas="<p>Texas riders face heavy traffic, high summer heat and drivers who don't always see motorcycles. Uninsured motorist coverage and strong medical protection are especially important, because injuries in a motorcycle accident can be serious and the other driver may not carry enough insurance.</p>",
 save_h="Ways to Save on Motorcycle Insurance",
 save=["Completing a motorcycle safety course", "Bundling with auto or home insurance", "Insuring multiple bikes on one policy", "Anti-theft devices and garage storage", "Riding experience and a claims-free history", "Paid-in-full discounts"],
 faqs=[("Is motorcycle insurance required in Texas?", "Yes. Texas requires motorcycle owners to carry liability insurance with at least 30/60/25 limits, the same minimums as passenger cars."),
       ("Does my auto policy cover my motorcycle?", "No. Motorcycles need their own policy. Many carriers offer a discount when you bundle motorcycle insurance with your auto or home policy."),
       ("Are my custom parts covered?", "Standard policies include only a small amount of custom parts and equipment coverage. If you've added chrome, exhaust, seats, saddlebags or custom paint, we can help you add enough coverage to protect your investment.")],
 related=["auto-insurance", "rv-insurance", "umbrella-insurance"],
),
dict(
 slug="landlord-insurance", cov="Landlord", name="Landlord Insurance", short="Landlord",
 title="Landlord Insurance in Denton, TX | Rental Property Insurance | Trailmark",
 desc="Landlord and rental property insurance for single-family homes, duplexes and investment properties in Denton County and North Texas. Dwelling, loss of rent and liability coverage.",
 h1="Landlord Insurance in Denton, Texas",
 alt="Single-story brick duplex rental property with two front doors and covered porches",
 lead="Protect your rental homes, duplexes and investment properties, and the rental income that depends on them.",
 card="Rental property coverage for homes and duplexes: dwelling, lost rent and landlord liability in one policy.",
 intro=["Rental property is a smart investment in fast-growing Denton County, but a standard homeowners policy usually won't cover a home you rent to tenants. Landlord insurance, often written as a dwelling fire policy such as a DP-3, is built for owners who rent out single-family homes, duplexes, townhomes and condos.",
        "Whether you own one rental near UNT or a growing portfolio across North Texas, Trailmark compares landlord insurance from multiple carriers and helps you protect the property, your income and your liability."],
 covers=[("Dwelling", "Repairs or rebuilds the rental structure after a covered loss such as fire, wind or hail."),
         ("Other structures", "Covers detached garages, fences and sheds on the rental property."),
         ("Loss of rental income", "Replaces lost rent if a covered loss makes the property uninhabitable during repairs."),
         ("Landlord liability", "Protects you if a tenant or visitor is injured because of a condition on your property."),
         ("Landlord-owned property", "Covers appliances, window coverings and lawn equipment you provide for tenants."),
         ("Vandalism and malicious mischief", "Often available as an option to protect against intentional damage.")],
 texas_h="Smart Coverage Choices for Texas Rental Owners",
 texas="<p>Ask about wind and hail deductibles, roof coverage on older rentals and how long loss-of-rent coverage lasts. If you rent your property short-term through Airbnb or VRBO, let us know, because short-term rentals often need different coverage than a traditional lease.</p><p>We also recommend requiring tenants to carry <a href=\"/products/renters-insurance/\">renters insurance</a>, since your landlord policy won't cover their belongings.</p>",
 save_h="Ways to Save on Landlord Insurance",
 save=["Insure multiple rental properties together", "Bundle with your own home and auto policies", "Updated roof, plumbing and electrical systems", "Security systems and smoke detectors", "A claims-free history", "An umbrella policy for extra liability across all properties"],
 faqs=[("Does homeowners insurance cover a rental property?", "Generally no. Once you rent a home to tenants, you usually need a landlord (dwelling) policy. Keeping a homeowners policy on a rental could leave a claim unpaid."),
       ("Does landlord insurance cover my tenant's belongings?", "No. Landlord insurance covers the building and the property you own. Tenants need their own renters insurance to protect their belongings and liability."),
       ("What is loss of rent coverage?", "If a covered loss, like a fire, makes your rental unlivable, loss of rent (fair rental value) coverage replaces the rent you would have collected while it's being repaired.")],
 related=["home-insurance", "umbrella-insurance", "business-insurance"],
),
dict(
 slug="jewelry-insurance", cov="Jewelry", name="Jewelry Insurance", short="Jewelry",
 title="Jewelry Insurance in Denton, TX | Engagement Ring Insurance | Trailmark",
 desc="Insure engagement rings, wedding bands, watches and heirlooms against loss, theft and damage. Trailmark helps Denton and North Texas families schedule jewelry coverage. Free quote.",
 h1="Jewelry Insurance in Denton, Texas",
 alt="Close-up of a diamond engagement ring on a woman's hand",
 lead="Engagement rings, wedding bands, watches and family heirlooms deserve more than the small limit on a standard homeowners or renters policy.",
 card="Protect engagement rings, watches and heirlooms against loss, theft and damage at their full appraised value.",
 intro=["Most homeowners and renters policies include only a small limit for jewelry theft, often a few thousand dollars or less, and they may not cover a stone falling out of its setting or a ring lost down the drain. Jewelry insurance closes that gap.",
        "Trailmark helps you protect your most valuable pieces, either by scheduling them on your home or renters policy (a personal articles floater) or with a standalone jewelry policy, so each item is covered for its appraised value."],
 covers=[("Loss and mysterious disappearance", "Coverage when a ring slips off or a piece simply goes missing."),
         ("Theft", "Protection at home, at the gym or on vacation."),
         ("Accidental damage", "Chipped stones, broken prongs and other everyday damage."),
         ("Worldwide coverage", "Your jewelry is protected wherever you travel."),
         ("Appraised value", "Each scheduled item is insured for its documented value."),
         ("Low or no deductible options", "Many scheduled jewelry policies carry little or no deductible.")],
 texas_h="What You'll Need to Insure Your Jewelry",
 texas="<p>Insuring jewelry is simple. For most pieces, you'll need a recent appraisal or a sales receipt showing the item's value. We recommend updating appraisals every few years, because gold, platinum and diamond prices change.</p><p>Keep photos of each piece and store your appraisals somewhere safe outside your home, or in the cloud.</p>",
 save_h="Popular Items to Insure",
 save=["Engagement rings and wedding bands", "Luxury watches", "Family heirlooms", "Earrings, necklaces and bracelets", "Anniversary and milestone gifts"],
 faqs=[("Does homeowners insurance cover my engagement ring?", "Only up to a limited amount for theft, and often not at all if you simply lose it. Scheduling your ring gives it its own coverage at its appraised value."),
       ("How much does it cost to insure an engagement ring?", "Cost depends mainly on the ring's value and where you live. Scheduled jewelry coverage is typically affordable compared to the value it protects, and we'll quote it for you for free."),
       ("Do I need an appraisal to insure jewelry?", "Usually, yes. A current appraisal or receipt documents the item's value and helps any future claim go smoothly.")],
 related=["home-insurance", "renters-insurance", "condo-insurance"],
),
dict(
 slug="umbrella-insurance", cov="Umbrella", name="Umbrella Insurance", short="Umbrella",
 title="Umbrella Insurance in Denton, TX | Personal Liability Coverage | Trailmark",
 desc="Add $1 million or more of liability protection above your auto, home and boat policies. Personal umbrella insurance for Denton and North Texas families. Compare quotes free.",
 h1="Umbrella Insurance in Denton, Texas",
 alt="Red and white open umbrella representing umbrella liability insurance",
 lead="One serious accident or lawsuit can exceed your auto and home liability limits. An umbrella policy adds an extra layer of protection for everything you've worked for.",
 card="Extra liability protection above your auto and home limits, so one bad day doesn't put everything you've built at risk.",
 intro=["A personal umbrella policy provides additional liability coverage, commonly in $1 million increments, that kicks in after the liability limits on your auto, homeowners, renters, boat or motorcycle policy are used up.",
        "Umbrella insurance is often one of the most affordable ways to protect your savings, home equity and future earnings. Trailmark helps Denton County families decide how much coverage makes sense and coordinates it with their other policies."],
 covers=[("Extra auto liability", "Protection above your car insurance limits after a serious accident."),
         ("Extra home liability", "Protection above your homeowners or renters liability limits."),
         ("Boat, RV and motorcycle liability", "Extends over your recreational vehicle policies, too."),
         ("Legal defense costs", "Helps pay attorney fees and court costs for covered claims."),
         ("Personal injury claims", "Many policies cover claims such as libel, slander and defamation."),
         ("Worldwide coverage", "Protection that travels with you.")],
 texas_h="Who Should Consider an Umbrella Policy?",
 texas="<ul><li>Homeowners with growing equity or savings</li><li>Families with teen drivers</li><li>Homes with pools, trampolines or dogs</li><li>Landlords and rental property owners</li><li>Boat, RV and motorcycle owners</li><li>Coaches, volunteers and anyone who hosts often</li></ul><p><a href=\"/news-and-insights/umbrella-insurance-texas-families/\">Learn why so many Texas families add an umbrella policy</a>.</p>",
 save_h="Good to Know",
 save=["Most umbrella policies require minimum liability limits on your auto and home policies", "Coverage is typically sold in $1 million increments", "Placing auto, home and umbrella with one carrier can simplify claims and lower your cost"],
 faqs=[("How much does umbrella insurance cost?", "Umbrella coverage is often surprisingly affordable for the amount of protection it provides. The price depends on how many homes, vehicles and drivers you have. We'll quote it alongside your other policies."),
       ("How much umbrella coverage do I need?", "A common starting point is enough coverage to protect your net worth and future income. Many families choose $1 million; others choose $2 million or more."),
       ("Does a personal umbrella policy cover my business?", "A personal umbrella generally excludes business activities. Businesses need a commercial umbrella or excess liability policy, which we can also help with.")],
 related=["auto-insurance", "home-insurance", "boat-insurance"],
),
dict(
 slug="boat-insurance", cov="Boat", name="Boat Insurance", short="Boat",
 title="Boat Insurance in Denton, TX | Lake Ray Roberts & Lewisville Lake | Trailmark",
 desc="Boat insurance for pontoons, bass boats, ski boats, cruisers and personal watercraft on Lake Ray Roberts, Lewisville Lake, Grapevine Lake and Texas waters. Compare quotes free.",
 h1="Boat Insurance in Denton, Texas",
 alt="Family cruising on a navy and white boat with a bimini top on a North Texas lake",
 lead="Spend your weekends on the water, not worrying about it. Get boat and personal watercraft coverage for North Texas lakes and beyond.",
 card="Coverage for pontoons, bass boats, ski boats and jet skis, on the water, on the trailer or in storage.",
 intro=["From Lake Ray Roberts and Lewisville Lake to Grapevine Lake and Lake Texoma, North Texas offers some of the best boating in the state. Trailmark Insurance Advisors compares boat insurance for pontoons, bass and fishing boats, ski and wake boats, cabin cruisers, sailboats and personal watercraft like jet skis.",
        "Homeowners policies typically offer very little coverage for boats, especially once they're on the water. A dedicated boat policy protects your boat, your passengers and your liability."],
 covers=[("Physical damage", "Covers your hull, motor and equipment against accidents, storms, fire and theft."),
         ("Boating liability", "Protects you if you injure someone or damage another boat or dock."),
         ("Uninsured boater", "Protects you and your passengers when an uninsured boater causes an accident."),
         ("Medical payments", "Helps pay medical bills for you and your passengers."),
         ("On-water towing and assistance", "Help when you run out of fuel, break down or run aground."),
         ("Trailer coverage", "Protects the trailer you use to haul your boat."),
         ("Personal effects and fishing equipment", "Covers gear you keep on board."),
         ("Fuel spill liability", "Covers cleanup costs required after an accidental fuel spill.")],
 texas_h="Boating in North Texas",
 texas="<p>Busy summer weekends, sudden storms and submerged hazards when lake levels change all add risk on Texas lakes. Liability coverage protects you if you injure someone or damage another boat or dock, and uninsured boater coverage protects you from the boaters who carry little or no insurance.</p>",
 save_h="Ways to Save on Boat Insurance",
 save=["Completing a boating safety course", "Bundling boat, auto and home insurance", "A claims-free history", "Lay-up options for the off-season", "Experience operating a boat"],
 faqs=[("Does homeowners insurance cover my boat?", "Homeowners policies usually provide only limited coverage for small boats and often exclude liability on the water entirely. A separate boat policy is the safest way to protect your boat and your liability."),
       ("Is boat insurance required in Texas?", "Texas law doesn't require boat insurance, but lenders usually require it if you finance a boat, and many marinas require liability coverage to rent a slip."),
       ("Do you insure jet skis and personal watercraft?", "Yes. We can quote personal watercraft such as jet skis and WaveRunners, along with the trailer you tow them on.")],
 related=["rv-insurance", "umbrella-insurance", "auto-insurance"],
),
dict(
 slug="business-insurance", cov="Business", name="Business Insurance", short="Business",
 title="Business Insurance in Denton, TX | Small Business Insurance | Trailmark",
 desc="Small business insurance for Denton and North Texas: general liability, BOPs, commercial property, commercial auto, workers' comp and more. Compare quotes from multiple carriers.",
 h1="Business Insurance in Denton, Texas",
 alt="Small business owners standing in front of their pet grooming salon storefront",
 lead="Protect the business you've worked so hard to build, with coverage tailored to your industry, your employees and your customers.",
 card="General liability, commercial property, business auto, BOPs and workers' comp for small businesses and contractors.",
 intro=["From retail shops on the Denton Square to contractors, salons, pet groomers, restaurants and professional offices across North Texas, every small business faces risks that personal policies won't cover. Trailmark Insurance Advisors compares business insurance from multiple carriers to build a plan that fits your operation.",
        "We take time to understand how your business actually works, including your location, equipment, vehicles, employees and contracts, so you're not paying for coverage you don't need or missing coverage you do."],
 covers=[("General liability", "Protects against customer injuries, property damage and advertising claims."),
         ("Business owner's policy (BOP)", "Combines general liability and property coverage, often at a lower cost than buying them separately."),
         ("Commercial property", "Covers your building, equipment, inventory and furniture."),
         ("Commercial auto", "Insures vehicles your business owns or uses."),
         ("Workers' compensation", "Covers medical care and lost wages for employees injured on the job."),
         ("Professional liability (E&amp;O)", "Protects service businesses against claims of mistakes or negligence."),
         ("Cyber liability", "Helps respond to data breaches and cyberattacks."),
         ("Tools and equipment (inland marine)", "Protects contractors' tools and equipment on the job site."),
         ("Commercial umbrella", "Adds extra liability limits above your other business policies.")],
 texas_h="Business Insurance in Texas",
 texas="<p>Texas is the only state where most private employers can choose whether to carry workers' compensation insurance. Employers who opt out, known as nonsubscribers, give up important legal protections, so it's a decision worth discussing carefully.</p><p>Many commercial leases and client contracts also require specific liability limits and certificates of insurance. We'll help you meet those requirements quickly.</p>",
 save_h="Businesses We Commonly Help",
 save=["Retail stores and boutiques", "Contractors and skilled trades", "Salons, spas and pet groomers", "Restaurants and food service", "Professional and medical offices", "Home-based businesses"],
 faqs=[("What insurance does a small business need in Texas?", "Most small businesses start with general liability and property coverage, often combined in a business owner's policy (BOP). Depending on your business, you may also need commercial auto, workers' compensation, professional liability or cyber coverage."),
       ("Is workers' compensation required in Texas?", "For most private employers, no. Texas lets employers choose. However, employers without coverage lose certain legal protections, and some contracts and government projects require it. We'll help you weigh the decision."),
       ("Can you provide a certificate of insurance quickly?", "Yes. Once your policy is in place, we can help you get certificates of insurance for landlords, clients and general contractors.")],
 related=["landlord-insurance", "umbrella-insurance", "auto-insurance"],
),
dict(
 slug="rv-insurance", cov="RV", name="RV Insurance", short="RV",
 title="RV Insurance in Denton, TX | Motorhome & Travel Trailer Insurance | Trailmark",
 desc="RV insurance for motorhomes, travel trailers and fifth wheels in Denton and North Texas. Full-timer, vacation liability, personal effects and roadside coverage. Compare quotes free.",
 h1="RV Insurance in Denton, Texas",
 alt="Retired couple relaxing by a campfire next to their motorhome at sunset",
 lead="Whether it's a weekend at the lake or a cross-country adventure, get RV coverage that protects your home on wheels.",
 card="Coverage for motorhomes, travel trailers and fifth wheels, from weekend camping trips to full-time RV living.",
 intro=["Recreational vehicles are part vehicle and part home, and they need coverage that understands both. Trailmark compares RV insurance for Class A, B and C motorhomes, travel trailers, fifth wheels, pop-ups and toy haulers for North Texas families and retirees.",
        "From campgrounds at Ray Roberts Lake State Park to national parks across the country, the right RV policy protects your rig, your belongings and your liability wherever the road takes you."],
 covers=[("Liability", "Required for motorhomes, just like a car."),
         ("Collision and comprehensive", "Covers accidents, hail, fire, theft and vandalism."),
         ("Personal effects", "Protects belongings you keep inside your RV."),
         ("Vacation liability", "Covers injuries at your campsite while your RV is being used as a temporary residence."),
         ("Full-timer coverage", "Homeowners-style protection if you live in your RV most of the year."),
         ("Emergency expenses", "Helps pay for lodging and transportation if your RV breaks down far from home."),
         ("Roadside assistance and towing", "Help for large vehicles that standard roadside plans may not handle."),
         ("Total loss replacement", "Options to replace a newer RV with a new model after a total loss.")],
 texas_h="Motorhomes vs. Towables",
 texas="<p>Motorized RVs need their own liability coverage, just like a car. For travel trailers and fifth wheels, liability usually extends from the vehicle towing it, but physical damage to the trailer itself typically requires its own coverage.</p><p>We'll make sure your truck and trailer policies work together with no gaps.</p>",
 save_h="Ways to Save on RV Insurance",
 save=["Bundling RV, auto and home insurance", "Storage (lay-up) options when your RV isn't in use", "RV safety and driving courses", "A claims-free history", "Paid-in-full discounts"],
 faqs=[("Do I need separate insurance for a travel trailer?", "Your auto policy may extend liability to a trailer you're towing, but it usually won't cover damage to the trailer itself or your belongings inside. A travel trailer policy fills those gaps."),
       ("What is full-timer RV insurance?", "If you live in your RV for most of the year, full-timer coverage adds protection similar to a homeowners policy, including personal liability and broader personal property coverage."),
       ("Is my RV covered when it's in storage?", "It can be. Many policies let you reduce coverage while your RV is stored to lower your premium, while keeping comprehensive protection against theft, hail and fire.")],
 related=["boat-insurance", "motorcycle-insurance", "auto-insurance"],
),
]

# ---------------------------------------------------------------- GENERAL FAQ
GENERAL_FAQ = [
 ("What is an independent insurance agency?", "An independent insurance agency works with multiple insurance companies instead of just one. That means Trailmark can compare coverage and prices from several carriers and recommend the policy that fits you best, rather than selling a single company's products."),
 ("Does it cost anything to work with Trailmark?", "No. There's no fee for quotes, coverage reviews or advice. Like most independent agencies, we're paid a commission by the insurance company you choose, so working with us doesn't add a fee on top of your premium."),
 ("What types of insurance do you offer?", "We help with <a href=\"/products/auto-insurance/\">auto</a>, <a href=\"/products/home-insurance/\">home</a>, <a href=\"/products/renters-insurance/\">renters</a>, <a href=\"/products/condo-insurance/\">townhome and condo</a>, <a href=\"/products/motorcycle-insurance/\">motorcycle</a>, <a href=\"/products/landlord-insurance/\">landlord</a>, <a href=\"/products/jewelry-insurance/\">jewelry</a>, <a href=\"/products/umbrella-insurance/\">umbrella</a>, <a href=\"/products/boat-insurance/\">boat</a>, <a href=\"/products/business-insurance/\">business</a> and <a href=\"/products/rv-insurance/\">RV</a> insurance. See all of them on our <a href=\"/products/\">Our Products</a> page."),
 ("What areas do you serve?", "Our office is in Denton, and we serve Denton County and the greater Dallas–Fort Worth area, including Corinth, Lake Dallas, Argyle, Flower Mound, Highland Village, Lewisville, Little Elm, Aubrey, Sanger, Krum, Prosper and Frisco. Because so much can be handled by phone and email, we can help clients throughout Texas."),
 ("Where is your office, and can I stop by?", "Our office is at 3616 Duchess Dr, Ste. 120, Denton, TX 76205. Office visits are by appointment only, so please call or email to schedule a time to meet in person."),
 ("What are your hours?", "Eric is available by phone Monday through Friday, 9:00 AM to 5:00 PM. In-person office visits are by appointment. You can request a quote online anytime."),
 ("How long does it take to get a quote?", "With our <a href=\"/contact/#quote\">online quoting tool</a>, most people can compare home and auto rates in about 10 minutes. Business and specialty policies may take a little longer because Eric gathers a few more details."),
 ("Which insurance companies do you work with?", "Trailmark works with Progressive, Travelers, Liberty Mutual, The Hartford and National General (an Allstate company), and we're adding carriers over time. Because we're independent, we compare them side by side to find your best fit."),
 ("What information do I need for a quote?", "For auto insurance: driver's license numbers, vehicle information (or VINs) and your current policy, if you have one. For home insurance: your address, the home's approximate age and square footage, and roof age. Your current declarations page is the most helpful document of all."),
 ("Can you review my current insurance policy?", "Yes, and it's free. <a href=\"/contact/#talk\">Send Eric a message</a> and attach your current declarations page. He'll explain what you have, point out any gaps and show you whether he can find better coverage or a better price."),
 ("I'm already a Trailmark client. How do I view or change my policy?", "Log in to our secure <a href=\"https://customerservice.agentinsure.com/EzlynxCustomerService/trailmarkins/Account/LogIn\" target=\"_blank\" rel=\"noopener\">Client Center</a> to view your policies and request service, or call (214) 531-7932, Monday through Friday from 9:00 AM to 5:00 PM."),
 ("Will switching insurance companies leave me uninsured?", "No. We set up your new policy to start the same day your old one ends, or we help you cancel the old policy after the new one is active, so there's no gap in coverage."),
 ("Do you help with claims?", "Yes. Claims are filed with your insurance company, but we're here to guide you through the process, answer questions and advocate for you when you need it most."),
 ("How can I save money on insurance?", "Bundling home and auto is one of the biggest ways to save. Other common discounts include multi-car, safe driver, good student, claims-free, new roof, security systems and paying in full. We'll look for every discount you qualify for."),
 ("Do you insure businesses?", "Yes. We help small businesses, contractors, salons, pet groomers, restaurants, retail shops and professional offices with general liability, business owner's policies, commercial property, commercial auto, workers' compensation and more. Learn more about <a href=\"/products/business-insurance/\">business insurance</a>."),
 ("How do I get started?", "The fastest way is to <a href=\"/contact/#quote\">start a free online quote</a> and compare rates from multiple carriers in about 10 minutes. Prefer to talk first? Call (214) 531-7932, email eric@texastrailmark.com or <a href=\"/contact/#talk\">send Eric a message</a>."),
]

# ---------------------------------------------------------------- BLOG POSTS
POSTS = [
dict(
 slug="texas-hail-season-homeowners-insurance-roof-coverage",
 title="Texas Hail Season: Is Your Roof Really Covered?",
 desc="Before the next North Texas hailstorm, learn how wind and hail deductibles, roof replacement cost and actual cash value work on Texas homeowners insurance policies.",
 img="home-insurance", cat="Home Insurance", date="2026-11-01", read=5,
 related=["home-insurance", "auto-insurance"],
 excerpt="Wind and hail deductibles, replacement cost vs. actual cash value, and what Denton County homeowners should check before the next storm.",
 body="""
<p>If you've lived in Denton County for more than a spring or two, you've probably heard hail hammering a roof or seen a neighborhood full of roofing trucks the week after a storm. North Texas sits squarely in one of the most hail-prone regions in the country, and a single storm can damage thousands of roofs, cars and windows in an afternoon.</p>
<p>Most homeowners assume their policy will take care of it. Often it will, but how much it pays depends on a few details that many people never look at until they file a claim. Here's what I recommend every Texas homeowner check now, while the sky is clear.</p>
<h2>1. Your wind and hail deductible</h2>
<p>Many Texas homeowners policies have a separate deductible just for wind and hail. Instead of a flat amount like $1,000, it's often a <strong>percentage of your dwelling coverage</strong>, commonly 1% or 2%.</p>
<p>On a home insured for $400,000, a 2% wind and hail deductible means you pay the first <strong>$8,000</strong> of a hail claim. That can be a shock if you were expecting a $1,000 deductible. A lower percentage usually raises your premium, so the right choice depends on your savings and comfort level.</p>
<h2>2. Replacement cost or actual cash value on your roof</h2>
<p>This is the big one. A <strong>replacement cost</strong> roof policy pays what it costs to put a new roof on your home, minus your deductible. An <strong>actual cash value (ACV)</strong> policy subtracts depreciation for the roof's age.</p>
<p>On a 15-year-old roof, depreciation can cut a claim payment dramatically, leaving you to cover much of a new roof yourself. Some carriers automatically switch older roofs to ACV, so it's worth asking how your policy treats your roof today.</p>
<h2>3. Cosmetic damage exclusions</h2>
<p>Some policies exclude "cosmetic" hail damage, such as dents in metal roofing, gutters or vents that don't affect how well the roof works. If you have a metal roof or plan to install one, ask whether cosmetic damage is covered.</p>
<h2>4. Impact-resistant shingle discounts</h2>
<p>If you're replacing your roof anyway, Class 4 impact-resistant shingles can hold up better to hail and may qualify you for a meaningful discount with many carriers. Keep your installation paperwork, because the insurance company may ask for proof.</p>
<h2>5. Don't forget your cars</h2>
<p>Hail damage to vehicles is covered by the <strong>comprehensive</strong> coverage on your <a href="/products/auto-insurance/">auto insurance</a>, not your homeowners policy. If you've dropped comprehensive on an older car to save money, a hailstorm could leave you paying for repairs yourself.</p>
<h2>What to do after a hailstorm</h2>
<ul>
<li>Take photos of any visible damage to your roof, siding, windows, gutters and vehicles.</li>
<li>Be cautious with door-to-door contractors who show up right after a storm. Get more than one estimate.</li>
<li>Report the claim to your insurance company promptly. Policies have deadlines for reporting damage.</li>
<li>Call us. We'll help you understand your coverage and what to expect.</li>
</ul>
<h2>Get a free hail coverage check</h2>
<p>As an independent agency in Denton, Trailmark Insurance Advisors compares <a href="/products/home-insurance/">homeowners insurance</a> from multiple carriers. <a href="/contact/#talk">Send me your current declarations page</a> and I'll review your wind and hail deductible, roof coverage and replacement cost for free, with no obligation.</p>
"""),
dict(
 slug="independent-insurance-agent-vs-captive-agent-denton",
 title="Independent vs. Captive Insurance Agents: What Denton Families Should Know",
 desc="What's the difference between an independent insurance agent and a captive agent? How independent agencies like Trailmark in Denton, TX compare multiple carriers for you.",
 img="auto-insurance", cat="Insurance Basics", date="2026-11-01", read=4,
 related=["auto-insurance", "home-insurance"],
 excerpt="Why working with an independent agency means more choices, a second opinion at renewal and one advisor for all your policies.",
 body="""
<p>When you shop for car or home insurance, you'll usually work with one of three options: a <strong>captive agent</strong>, an <strong>independent agent</strong>, or buying directly online or by phone. Each can work, but they're very different experiences. Here's a plain-English breakdown to help Denton County families choose.</p>
<h2>What is a captive agent?</h2>
<p>A captive agent represents a single insurance company. They know that company's products well and can offer good service, but they can only quote that one company. If its rates go up or it isn't a good fit for your situation, a captive agent can't shop you elsewhere.</p>
<h2>What is an independent agent?</h2>
<p>An independent insurance agency, like Trailmark Insurance Advisors, has relationships with multiple insurance companies. Instead of fitting you into one company's box, we compare coverage and pricing across several carriers and recommend the best match.</p>
<h2>Why that matters to you</h2>
<ul>
<li><strong>More choices, one conversation.</strong> You share your information once, and we do the comparison shopping.</li>
<li><strong>A second opinion at renewal.</strong> If your premium jumps, we can re-shop your policy instead of telling you to take it or leave it.</li>
<li><strong>Coverage for unusual situations.</strong> Teen drivers, older roofs, rental properties, boats and small businesses don't always fit one company's guidelines. Having options helps.</li>
<li><strong>One advisor for everything.</strong> Your <a href="/products/auto-insurance/">auto</a>, <a href="/products/home-insurance/">home</a>, <a href="/products/umbrella-insurance/">umbrella</a> and <a href="/products/business-insurance/">business</a> policies can all be reviewed together, so nothing falls through the cracks.</li>
</ul>
<h2>Does an independent agent cost more?</h2>
<p>No. Independent agencies are paid a commission by the insurance company you choose, and there's no extra fee for quotes or advice. Your price is set by the carrier, not by the agent.</p>
<h2>What about buying insurance online?</h2>
<p>Buying direct can be quick, but you're on your own when it comes to choosing limits, understanding exclusions or handling a complicated claim. Many people discover gaps only after something goes wrong. A local advisor helps you avoid that.</p>
<h2>Talk to a local, independent advisor in Denton</h2>
<p>Trailmark Insurance Advisors is a Texas-owned independent insurance agency based in Denton. I'd be glad to <a href="/contact/#talk">review your current policies</a> and show you how they compare, or you can <a href="/contact/#quote">start a free online quote</a> or call (214) 531-7932.</p>
"""),
dict(
 slug="condo-townhome-insurance-hoa-master-policy",
 title="Does Your HOA's Master Policy Cover Your Condo or Townhome?",
 desc="Bare walls, single entity or all-in? Learn what an HOA master policy covers in Texas, what it doesn't, and why condo and townhome owners need HO-6 insurance.",
 img="condo-insurance", cat="Condo & Townhome", date="2026-11-01", read=5,
 related=["condo-insurance", "home-insurance"],
 excerpt="Bare walls, single entity or all-in: how to read your HOA master policy and choose the right condo or townhome coverage.",
 body="""
<p>Condos and townhomes are popular across Denton, Lewisville and Flower Mound, and for good reason: less yard work, shared amenities and an HOA that handles a lot of maintenance. But when it comes to insurance, that shared responsibility creates confusion. The most common question I hear is, <em>"Doesn't my HOA's insurance cover this?"</em></p>
<p>The answer is: partly. Here's how to figure out what you're responsible for.</p>
<h2>What the HOA master policy usually covers</h2>
<p>Your homeowners association carries a master policy that typically insures common areas like hallways, roofs, pools, clubhouses and exterior walls, along with liability for those shared spaces. How far that coverage reaches inside your unit depends on the type of master policy.</p>
<h2>The three common types of master policies</h2>
<ul>
<li><strong>Bare walls.</strong> Covers only the building's structure. You're responsible for nearly everything inside your unit, including drywall, flooring, cabinets and fixtures.</li>
<li><strong>Single entity.</strong> Covers the structure plus the original fixtures and finishes, but not upgrades you or a previous owner made.</li>
<li><strong>All-in (all-inclusive).</strong> Covers more of the interior, including some improvements. Even then, your belongings and personal liability aren't covered.</li>
</ul>
<p>Your HOA's governing documents, often called the declarations or CC&amp;Rs, spell out which type you have and where your responsibility begins.</p>
<h2>What your own condo policy (HO-6) covers</h2>
<ul>
<li>The interior parts of your unit that the master policy doesn't cover</li>
<li>Upgrades such as granite countertops, hardwood floors and custom cabinets</li>
<li>Your furniture, electronics, clothing and other belongings</li>
<li>Personal liability if someone is hurt in your unit or you damage a neighbor's unit</li>
<li>Loss of use if you have to live elsewhere during repairs</li>
<li><strong>Loss assessment</strong>, which helps pay your share if the HOA bills owners for a large claim or a high master-policy deductible</li>
</ul>
<h2>Townhomes are different, so check carefully</h2>
<p>In some North Texas townhome communities, the HOA insures the buildings and an HO-6 condo policy makes sense. In others, you own the structure and the land underneath it, and you need a full <a href="/products/home-insurance/">homeowners policy</a>. Getting this wrong can leave you seriously underinsured.</p>
<h2>Watch the master-policy deductible</h2>
<p>Hail and wind deductibles on Texas master policies can be large. If the HOA passes that deductible on to owners, loss assessment coverage on your own policy can save you from an unexpected bill. Ask your HOA what its deductible is, then make sure your loss assessment limit is high enough.</p>
<h2>Let us read the fine print with you</h2>
<p>At Trailmark Insurance Advisors, we review your HOA documents and master policy and recommend <a href="/products/condo-insurance/">townhome and condo coverage</a> that fills the gaps without paying for duplicate coverage. <a href="/contact/#talk">Send Eric your HOA documents for a free review</a>.</p>
"""),
dict(
 slug="renters-insurance-unt-twu-students-denton",
 title="Renters Insurance for UNT and TWU Students: A Denton Guide",
 desc="A plain-English guide to renters insurance for University of North Texas and Texas Woman's University students renting apartments in Denton, TX.",
 img="renters-insurance", cat="Renters Insurance", date="2026-11-01", read=4,
 related=["renters-insurance", "auto-insurance"],
 excerpt="What renters insurance covers, whether a parent's policy is enough, and how students can protect laptops, bikes and more.",
 body="""
<p>Every August, thousands of students move into apartments and rental houses around the University of North Texas and Texas Woman's University. Between the lease, the deposit and the furniture, renters insurance is easy to overlook. It shouldn't be. Here's what students and parents in Denton should know.</p>
<h2>Your landlord's insurance doesn't cover your stuff</h2>
<p>Your apartment complex or landlord insures the building. If a fire, burst pipe or break-in damages your laptop, TV, bike or clothes, their policy won't pay to replace them. That's what renters insurance is for.</p>
<h2>What renters insurance covers</h2>
<ul>
<li><strong>Your belongings</strong>, including laptops, phones, gaming systems, furniture, bikes and textbooks, against fire, smoke, theft, vandalism and certain water damage</li>
<li><strong>Coverage away from home</strong>, so a laptop stolen from a library or car can be covered</li>
<li><strong>Personal liability</strong> if a guest is injured or you accidentally damage someone else's property, like a kitchen fire that spreads to a neighbor's unit</li>
<li><strong>Loss of use</strong>, which helps pay for somewhere to stay if your apartment becomes unlivable</li>
</ul>
<h2>Is a parent's homeowners policy enough?</h2>
<p>Sometimes, but often not. Many homeowners policies extend limited coverage to a full-time student living away from home, but it may come with a low limit, a high deductible, or rules that don't apply to off-campus apartments. A claim on a parent's policy could also affect their premium. A renters policy in the student's own name is usually simple, affordable and keeps claims separate.</p>
<h2>Many Denton apartments require it</h2>
<p>A lot of apartment communities near campus require proof of renters insurance before move-in and may ask to be listed as an "interested party." We can help you get a policy and proof of coverage quickly.</p>
<h2>Tips to keep it affordable</h2>
<ul>
<li>Bundle renters insurance with the student's <a href="/products/auto-insurance/">auto insurance</a></li>
<li>Choose a deductible you could comfortably pay</li>
<li>Ask about good-student discounts on auto policies</li>
<li>Take a quick video of your belongings so a future claim is easier</li>
</ul>
<h2>Get covered before move-in day</h2>
<p>Trailmark Insurance Advisors is a local, independent agency in Denton, minutes from both campuses. We'll compare <a href="/products/renters-insurance/">renters insurance</a> from multiple carriers and help you find the right fit. <a href="/contact/#quote">Get a free quote</a>.</p>
"""),
dict(
 slug="umbrella-insurance-texas-families",
 title="Umbrella Insurance: The Affordable Extra Layer Most Texas Families Skip",
 desc="What personal umbrella insurance covers, who needs it, and why Texas families with homes, teen drivers, pools or boats should consider $1 million or more of extra liability.",
 img="umbrella-insurance", cat="Umbrella Insurance", date="2026-11-01", read=4,
 related=["umbrella-insurance", "boat-insurance"],
 excerpt="How a personal umbrella policy protects your savings and home equity, and why it's often more affordable than people expect.",
 body="""
<p>Most families carefully choose their car and home insurance, then never think about what happens if a single accident costs more than those policies will pay. That's exactly the gap a personal umbrella policy is designed to fill, and it's often one of the best values in insurance.</p>
<h2>What is umbrella insurance?</h2>
<p>A personal umbrella policy adds extra liability protection, usually starting at $1 million, on top of your <a href="/products/auto-insurance/">auto</a>, <a href="/products/home-insurance/">homeowners</a>, renters, <a href="/products/boat-insurance/">boat</a> and motorcycle policies. When a covered claim exceeds the liability limit on one of those policies, the umbrella picks up where it leaves off.</p>
<h2>Why it matters</h2>
<p>Serious accidents can be expensive. A multi-car crash with injuries, a guest badly hurt at your home or a dog bite can lead to medical bills and legal judgments that exceed typical auto and home liability limits. When that happens, your savings, home equity and even future wages can be at risk.</p>
<h2>Who should consider an umbrella policy?</h2>
<ul>
<li>Homeowners with growing equity, savings or retirement accounts</li>
<li>Families with teen drivers</li>
<li>Homes with a pool, trampoline or dog</li>
<li>Landlords with one or more <a href="/products/landlord-insurance/">rental properties</a></li>
<li>Boat, RV and motorcycle owners</li>
<li>Anyone who coaches, volunteers or hosts frequently</li>
</ul>
<h2>What does it cost?</h2>
<p>Umbrella insurance is often surprisingly affordable for the amount of protection it provides, because it only pays after your other policies are exhausted. The exact price depends on how many homes, vehicles and drivers you have. Most carriers require you to carry certain minimum liability limits on your auto and home policies first.</p>
<h2>How much coverage should you get?</h2>
<p>A good starting point is enough coverage to protect your net worth and future income. Many families choose $1 million; others with more assets choose $2 million or more. We'll help you think it through.</p>
<h2>Add an umbrella with your next review</h2>
<p>Trailmark Insurance Advisors in Denton can quote <a href="/products/umbrella-insurance/">umbrella insurance</a> alongside your auto and home policies, and make sure your underlying limits line up. <a href="/contact/#quote">Request a free quote</a> or call (214) 531-7932.</p>
"""),
]
