#!/usr/bin/env python3
"""Generates the static Demosh Designs pages (shared header/footer)."""
import os, urllib.parse
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
WA = '254704121852'
TEL = '+254704121852'
PHONE = '+254 704 121 852'
FB = 'https://www.facebook.com/search/top?q=Demosh%20Designs'
MAPQ = 'Kamutiini, Lower Kabete, Kenya'
MAPS = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(MAPQ)

def wa(msg):
    return f'https://wa.me/{WA}?text=' + urllib.parse.quote(msg)

I = {
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-.9 1.2-.3.2-.6.1a8.2 8.2 0 0 1-4.1-3.6c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.1 1.1 0 0 0-.8.4 3.4 3.4 0 0 0-1.1 2.5 5.9 5.9 0 0 0 1.2 3.1 13.4 13.4 0 0 0 5.2 4.6c1.9.8 2.7.9 3.6.7a3.1 3.1 0 0 0 2-1.4 2.5 2.5 0 0 0 .2-1.4c-.1-.2-.3-.3-.6-.4zM12 21.8a9.8 9.8 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7a11.8 11.8 0 0 0 5.6 1.4 11.8 11.8 0 0 0 8.4-20.1z"/></svg>',
 'tel': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4h-3V12h3V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9V12h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg>',
}
DOTS = '<span class="dots" aria-hidden="true"><i></i><i></i><i></i><i></i></span>'
PAGES = [('index.html', 'Home'), ('services.html', 'Services'), ('gallery.html', 'Gallery'), ('about.html', 'About'), ('contact.html', 'Contact')]
MCOL = ['var(--c)', 'var(--m)', 'var(--y)', '#fff', 'var(--c)']

def head(title, desc, current):
    nav = ''.join(f'<a href="{h}"{" aria-current=page" if h == current else ""}>{n}</a>' for h, n in PAGES)
    mnav = ''.join(f'<a class="l" href="{h}"><i style="background:{MCOL[i]}"></i>{n}</a>' for i, (h, n) in enumerate(PAGES))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0e0b16">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/og.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://assets.mixkit.co">
<link rel="stylesheet" href="assets/css/site.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Store","name":"Demosh Designs","description":"Quality apparel, professional branding, personalised gifts and printing services.","telephone":"{TEL}","founder":{{"@type":"Person","name":"Gordon Omala"}},"address":{{"@type":"PostalAddress","streetAddress":"Kamutiini","addressLocality":"Lower Kabete","addressRegion":"Kiambu","addressCountry":"KE"}},"openingHoursSpecification":{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"}}}}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Demosh Designs home">{DOTS}<span><b>Demosh</b><small>Designs</small></span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="hdr-cta">
      <a class="btn btn-wa btn-sm" href="{wa("Hi Demosh Designs, I would like to ask about ")}" target="_blank" rel="noopener">{I["wa"]}Chat on WhatsApp</a>
      <button class="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mnav" id="mnav" aria-hidden="true">
  <button class="mnav-close" aria-label="Close menu">&times;</button>
  {mnav}
  <div class="foot">
    <a class="btn btn-wa" href="{wa("Hi Demosh Designs, I would like to ask about ")}" target="_blank" rel="noopener">{I["wa"]}Chat on WhatsApp</a>
    <a class="btn btn-ghost" href="tel:{TEL}">{I["tel"]}Call {PHONE}</a>
  </div>
</div>
<main id="main">
'''

def foot(extra_js=''):
    return f'''</main>
<footer class="ftr">
  <div class="wrap">
    <div class="big">Demosh {DOTS}</div>
    <div class="cols">
      <div>
        <p style="max-width:36ch">Quality apparel, professional branding, personalised gifts and printing. We bring ideas to life through creativity, quality and attention to detail.</p>
      </div>
      <div><h4>Explore</h4><ul>{''.join(f'<li><a href="{h}">{n}</a></li>' for h, n in PAGES)}</ul></div>
      <div><h4>Services</h4><ul>
        <li><a href="services.html#apparel">Apparel</a></li><li><a href="services.html#branding">Branding</a></li>
        <li><a href="services.html#gifts">Personalised gifts</a></li><li><a href="services.html#printing">Printing</a></li></ul></div>
      <div><h4>Reach us</h4><ul>
        <li><a href="tel:{TEL}">{PHONE}</a></li>
        <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="{MAPS}" target="_blank" rel="noopener">Kamutiini, Lower Kabete</a></li>
        <li>Open 24 hours</li></ul></div>
    </div>
    <div class="base"><span>&copy; <span data-year>2026</span> Demosh Designs. All rights reserved.</span><span>Website by <a href="https://ivulatechnologies.com" target="_blank" rel="noopener">Ivula Technologies</a></span></div>
  </div>
</footer>
<a class="fab" href="{wa("Hi Demosh Designs, I would like to ask about ")}" target="_blank" rel="noopener" aria-label="Chat with Demosh Designs on WhatsApp">{I["wa"]}</a>
{extra_js}<script src="assets/js/site.js" defer></script>
</body>
</html>
'''

def vid(mx, name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<video{c} data-mx="{mx}" data-local="assets/media/{name}.mp4" muted loop playsinline preload="none" aria-hidden="true"></video>'

def subhero(mx, name, crumb, h1, lead, extra=''):
    return f'''<section class="hero sub">
  <div class="hero-media">{vid(mx, name)}</div>
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>
'''

SERVICES = [
 dict(id='apparel', n='01', bg='bg-c', mx='34707', name='apparel', h='Apparel',
      short='T-shirts, hoodies, caps and uniforms that look sharp and last.',
      intro='Custom clothing for your team, school, church, event or brand. Tell us the look you want and we will help you get it right, from the first sketch to the finished piece.',
      ticks=['Custom T-shirts', 'Hoodies and sweatshirts', 'Caps and hats', 'Staff and team uniforms', 'Event and group wear', 'Your own clothing line']),
 dict(id='branding', n='02', bg='bg-m', mx='45750', name='branding', h='Branding',
      short='A look people remember, on everything your business touches.',
      intro='Professional branding that makes your business look as good as the work you do. We help you put one clear look on your logo, cards, uniforms and signs.',
      ticks=['Logo design', 'Business cards', 'Branded uniforms', 'Signs and banners', 'Company merchandise', 'Social media graphics']),
 dict(id='gifts', n='03', bg='bg-y', mx='15082', name='gifts', h='Personalised gifts',
      short='Mugs, bags and keepsakes made with a name, a photo or a message.',
      intro='Gifts that say you thought about it. Add a name, a photo, a date or a message for birthdays, weddings, graduations, corporate thank-yous and more.',
      ticks=['Printed mugs', 'Tote bags', 'Water bottles', 'Photo gifts', 'Corporate gift sets', 'Birthday and wedding gifts']),
 dict(id='printing', n='04', bg='bg-w', mx='25260', name='printing', h='Printing',
      short='Flyers, posters, stickers and banners with clean, bright colour.',
      intro='Printing services for business, school and events. Bring your design or let us create one for you, then we print it with sharp detail and true colour.',
      ticks=['Flyers and posters', 'Banners and roll-ups', 'Stickers and labels', 'Brochures', 'Certificates', 'Event programmes']),
]

def build_index():
    cards = ''.join(f'''<a class="svc rv d{i}" href="services.html#{s["id"]}">{vid(s["mx"], s["name"])}<span class="n {s["bg"]}">{s["n"]}</span><h3>{s["h"]}</h3><p>{s["short"]}</p><span class="go">Explore</span></a>''' for i, s in enumerate(SERVICES))
    mq_words = ['Custom T-shirts', 'Branding', 'Personalised gifts', 'Printing', 'Hoodies', 'Business cards', 'Mugs', 'Banners', 'Uniforms', 'Stickers']
    mq = ''.join(f'<span>{w}</span>' for w in mq_words)
    chips = ['T-shirts', 'Hoodies', 'Caps', 'Uniforms', 'Mugs', 'Tote bags', 'Water bottles', 'Business cards', 'Flyers', 'Posters', 'Banners', 'Stickers', 'Labels', 'Gift sets']
    cols = ['var(--c)', 'var(--m)', 'var(--y)', 'var(--ink)']
    chip_html = ''.join(f'<span class="chip"><i style="background:{cols[i % 4]}"></i>{c}</span>' for i, c in enumerate(chips))
    body = f'''<section class="hero">
  <div class="hero-media">{vid('45527', 'hero')}</div>
  <div class="wrap">
    <span class="kicker"><span class="live"></span>Open 24 hours &middot; Lower Kabete</span>
    <h1>Your idea, <em>made real</em> in <span class="swap" data-swap="apparel.|branding.|gifts.|print.">apparel.</span></h1>
    <p class="lead">Demosh Designs is your destination for quality apparel, professional branding, personalised gifts and printing services. We bring ideas to life through creativity, quality and attention to detail.</p>
    <div class="ctas">
      <a class="btn btn-wa" href="{wa("Hi Demosh Designs, I would like a quote for ")}" target="_blank" rel="noopener">{I["wa"]}Get a quote on WhatsApp</a>
      <a class="btn btn-ghost" href="services.html">See what we make</a>
    </div>
    <div class="meta">
      <span>{I["tel"]}<a href="tel:{TEL}" style="text-decoration:none">{PHONE}</a></span>
      <span>{I["pin"]}Kamutiini, Lower Kabete</span>
      <span>{I["clock"]}Open 24 hours</span>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">Scroll</div>
</section>
<div class="marquee" aria-hidden="true"><div class="track">{mq}{mq}</div></div>

<section class="sec">
  <div class="wrap">
    <div class="head-row">
      <div><p class="eyebrow">{DOTS} What we do</p><h2 class="h2 rv">Four ways we bring your idea to life.</h2></div>
      <a class="btn btn-dark" href="services.html">All services</a>
    </div>
    <div class="svc-grid">{cards}</div>
  </div>
</section>

<section class="sec dark">
  <div class="wrap">
    <div class="head-row">
      <div><p class="eyebrow">{DOTS} How it works</p><h2 class="h2 rv">From idea to finished piece.</h2></div>
      <p class="sub-p" style="margin:0">Simple and personal. You talk to us directly on WhatsApp or by phone, any time of day.</p>
    </div>
    <div class="steps">
      <div class="step rv"><h3>Share your idea</h3><p>Send a message with what you need, how many, and your logo, photo or sketch if you have one.</p></div>
      <div class="step rv d1"><h3>We design it</h3><p>We prepare the design and show you how it will look before anything is made.</p></div>
      <div class="step rv d2"><h3>You approve</h3><p>Ask for changes until you are happy. Nothing goes to print until you say yes.</p></div>
      <div class="step rv d3"><h3>We make it</h3><p>Your order is produced with care and checked for detail before it reaches you.</p></div>
    </div>
  </div>
</section>

<section class="band">
  {vid('12525', 'detail')}
  <div class="wrap">
    <p class="eyebrow" style="color:rgba(255,255,255,.7)">{DOTS} Attention to detail</p>
    <h2 class="rv">Every stitch, print and colour checked.</h2>
    <p class="rv d1">Creativity, quality and attention to detail are how we work. Small things make the big difference.</p>
    <a class="btn btn-y rv d2" href="about.html">About Demosh</a>
  </div>
</section>

<section class="sec cream">
  <div class="wrap">
    <p class="eyebrow">{DOTS} Ask us about</p>
    <h2 class="h2 rv" style="margin-bottom:36px">Put your name or brand on almost anything.</h2>
    <div class="chips rv d1">{chip_html}</div>
    <p class="sub-p">Don't see your item? Ask anyway. Send a photo of what you have in mind.</p>
  </div>
</section>

<section class="sec tight">
  <div class="wrap">
    <div class="cta rv">
      <p class="eyebrow" style="color:rgba(255,255,255,.7)">{DOTS} Ready when you are</p>
      <h2>Got an idea? Let's make it.</h2>
      <p>Message us on WhatsApp or call {PHONE}. We are open 24 hours.</p>
      <div class="ctas">
        <a class="btn btn-wa" href="{wa("Hi Demosh Designs, I have an idea I would like to make: ")}" target="_blank" rel="noopener">{I["wa"]}Chat on WhatsApp</a>
        <a class="btn btn-ghost" href="contact.html">Request a quote</a>
      </div>
    </div>
  </div>
</section>
'''
    return head('Demosh Designs · Apparel, branding, gifts and printing in Lower Kabete',
                'Demosh Designs, Kamutiini, Lower Kabete: quality apparel, professional branding, personalised gifts and printing. Open 24 hours. WhatsApp or call +254 704 121 852.',
                'index.html') + body + foot()

def build_services():
    jump = '<div class="jump">' + ''.join(f'<a href="#{s["id"]}">{s["h"]}</a>' for s in SERVICES) + '</div>'
    rows = ''
    for s in SERVICES:
        ticks = ''.join(f'<li>{t}</li>' for t in s['ticks'])
        rows += f'''<div class="svc-row" id="{s["id"]}">
      <div class="media rv">{vid(s["mx"], s["name"])}<span class="tag {s["bg"]}">{s["n"]}</span></div>
      <div>
        <p class="eyebrow">{DOTS} Service {s["n"]}</p>
        <h2 class="rv">{s["h"]}</h2>
        <p class="intro rv d1">{s["intro"]}</p>
        <ul class="ticks rv d2">{ticks}</ul>
        <div style="display:flex;flex-wrap:wrap;gap:10px">
          <a class="btn btn-wa" href="{wa(f"Hi Demosh Designs, I would like a quote for {s['h'].lower()}: ")}" target="_blank" rel="noopener">{I["wa"]}Ask about {s["h"].lower()}</a>
          <a class="btn btn-dark" href="contact.html?service={urllib.parse.quote(s["h"])}#quote">Request a quote</a>
        </div>
      </div>
    </div>
'''
    body = subhero('11696', 'services-hero', 'Services', 'What we <em>make</em>.',
                   'Apparel, branding, personalised gifts and printing, all under one roof in Lower Kabete.', jump)
    body += f'<section class="sec" style="padding-top:20px"><div class="wrap">{rows}</div></section>'
    body += f'''<section class="sec tight cream"><div class="wrap"><div class="cta rv">
      <h2>Not sure what you need?</h2><p>Tell us what it is for and your budget. We will suggest options that work.</p>
      <div class="ctas"><a class="btn btn-wa" href="{wa("Hi Demosh Designs, I need some advice. It is for: ")}" target="_blank" rel="noopener">{I["wa"]}Ask on WhatsApp</a>
      <a class="btn btn-ghost" href="tel:{TEL}">{I["tel"]}Call us</a></div></div></div></section>'''
    return head('Services · Demosh Designs', 'Custom apparel, branding, personalised gifts and printing from Demosh Designs in Lower Kabete. Ask for a quote on WhatsApp.', 'services.html') + body + foot()

def build_gallery():
    body = subhero('48152', 'gallery-hero', 'Gallery', 'Ideas we <em>bring to life</em>.',
                   'A look at the kind of pieces we make. Tap any item to ask for something similar.')
    body += f'''<section class="sec" style="padding-top:60px"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter gallery">
    <button type="button" data-f="all" aria-pressed="true">All</button>
    <button type="button" data-f="apparel" aria-pressed="false">Apparel</button>
    <button type="button" data-f="branding" aria-pressed="false">Branding</button>
    <button type="button" data-f="gifts" aria-pressed="false">Gifts</button>
    <button type="button" data-f="printing" aria-pressed="false">Printing</button>
  </div>
  <p class="note">These are sample mock-ups to show the range. Photos of real Demosh jobs are coming soon, and you can see recent work on our <a href="{FB}" target="_blank" rel="noopener">Facebook page</a>.</p>
  <div class="gallery" id="gallery"></div>
</div></section>
<div class="lb" role="dialog" aria-modal="true" aria-label="Gallery item">
  <button class="lb-close" aria-label="Close">&times;</button>
  <div class="inner"><div class="art"></div><div class="bar"><b class="t"></b><a class="btn btn-wa btn-sm" target="_blank" rel="noopener">{I["wa"]}I want something like this</a></div></div>
</div>
'''
    return head('Gallery · Demosh Designs', 'Custom T-shirts, hoodies, caps, mugs, business cards, banners and more from Demosh Designs, Lower Kabete.', 'gallery.html') + body + foot('<script src="assets/js/gallery.js"></script>\n')

def build_about():
    body = subhero('11698', 'about-hero', 'About', 'Creativity. Quality. <em>Detail.</em>',
                   'Demosh Designs is a design and print studio in Kamutiini, Lower Kabete, led by Gordon Omala.')
    body += f'''<section class="sec"><div class="wrap">
  <div class="head-row" style="align-items:flex-start">
    <div><p class="eyebrow">{DOTS} Our story</p><h2 class="h2 rv">We bring ideas to life.</h2></div>
    <div style="max-width:560px">
      <p class="sub-p rv" style="margin-top:0;color:var(--text);font-size:1.25rem">Demosh Designs is your destination for quality apparel, professional branding, personalised gifts and printing services.</p>
      <p class="sub-p rv d1">Whether it is a T-shirt for your team, a new look for your business or a gift for someone special, we treat every order as a chance to make something people are proud to wear, use and give. And because ideas don't keep office hours, neither do we: Demosh is open 24 hours.</p>
    </div>
  </div>
  <div class="values">
    <div class="val bg-c rv"><span>{DOTS}</span><div><h3>Creativity</h3><p>Every piece starts with your idea. We help shape it into a design that stands out.</p></div></div>
    <div class="val bg-m rv d1" style="color:#fff"><span>{DOTS}</span><div><h3>Quality</h3><p>Good materials and careful production, so what you get looks right and lasts.</p></div></div>
    <div class="val bg-y rv d2"><span>{DOTS}</span><div><h3>Attention to detail</h3><p>Colours, spelling, placement and finish are checked before anything leaves the studio.</p></div></div>
  </div>
</div></section>
<section class="band">
  {vid('32433', 'needle')}
  <div class="wrap">
    <p class="eyebrow" style="color:rgba(255,255,255,.7)">{DOTS} Meet the founder</p>
    <h2 class="rv">Gordon Omala</h2>
    <p class="rv d1">Gordon runs Demosh Designs and works with every client directly. Message him on WhatsApp with your idea and he will help you bring it to life.</p>
    <a class="btn btn-wa rv d2" href="{wa("Hi Gordon, I found Demosh Designs online and I would like to ask about ")}" target="_blank" rel="noopener">{I["wa"]}Message Gordon</a>
  </div>
</section>
<section class="sec tight"><div class="wrap"><div class="cta rv">
  <h2>Visit us in Lower Kabete.</h2><p>Find us in Kamutiini, Lower Kabete. Call ahead or message us so we can have your order ready.</p>
  <div class="ctas"><a class="btn btn-y" href="contact.html">Directions and contact</a><a class="btn btn-ghost" href="tel:{TEL}">{I["tel"]}{PHONE}</a></div>
</div></div></section>
'''
    return head('About · Demosh Designs', 'Demosh Designs is a design and print studio in Kamutiini, Lower Kabete, led by Gordon Omala. Creativity, quality and attention to detail.', 'about.html') + body + foot()

def build_contact():
    svc_opts = ''.join(f'<label><input type="checkbox" name="service" value="{s["h"]}"><span>{s["h"]}</span></label>' for s in SERVICES)
    body = subhero('22382', 'contact-hero', 'Contact', "Let's make <em>something</em>.",
                   'Call, WhatsApp or visit us in Kamutiini, Lower Kabete. We are open 24 hours.')
    body += f'''<section class="sec" style="padding-top:60px"><div class="wrap">
  <div class="c-grid">
    <a class="c-card bg-c rv" href="https://wa.me/{WA}" target="_blank" rel="noopener">{I["wa"]}<small>WhatsApp</small><b>Chat with us</b><span>Fastest reply &rarr;</span></a>
    <a class="c-card bg-m rv d1" href="tel:{TEL}" style="color:#fff">{I["tel"]}<small>Call</small><b>{PHONE}</b><span>Tap to call &rarr;</span></a>
    <a class="c-card bg-y rv d2" href="{MAPS}" target="_blank" rel="noopener">{I["pin"]}<small>Visit</small><b>Kamutiini, Lower Kabete</b><span>Open in Google Maps &rarr;</span></a>
    <a class="c-card rv d3" href="{FB}" target="_blank" rel="noopener" style="background:var(--ink);color:#fff">{I["fb"]}<small>Facebook</small><b>Demosh Designs</b><span>See our page &rarr;</span></a>
  </div>
</div></section>
<section class="sec cream" id="quote-sec"><div class="wrap">
  <div class="quote">
    <div>
      <p class="eyebrow">{DOTS} Request a quote</p>
      <h2 class="h2 rv">Tell us what you need.</h2>
      <p class="sub-p rv d1">Fill in what you know and tap the button. Your request opens in WhatsApp, ready to send. You can attach your logo, photo or design there.</p>
      <p class="hours"><span class="kicker" style="background:var(--ink);color:#fff"><span class="live"></span>Open 24 hours, every day</span></p>
    </div>
    <form class="form rv" id="quote" novalidate>
      <div class="field"><label for="q-name">Your name</label><input id="q-name" name="name" autocomplete="name" placeholder="e.g. Wanjiru"></div>
      <div class="field"><span class="lbl" id="svc-l">What do you need?</span><div class="pick" role="group" aria-labelledby="svc-l">{svc_opts}</div></div>
      <div class="two">
        <div class="field"><label for="q-item">Item</label><input id="q-item" name="item" placeholder="e.g. T-shirts, mugs, flyers"></div>
        <div class="field"><label for="q-qty">How many?</label><input id="q-qty" name="qty" inputmode="numeric" placeholder="e.g. 50"></div>
      </div>
      <div class="field"><label for="q-date">Needed by</label><input id="q-date" name="date" type="date"></div>
      <div class="field"><label for="q-details">Details</label><textarea id="q-details" name="details" placeholder="Colours, sizes, text to print, what it is for..."></textarea></div>
      <button class="btn btn-wa" type="submit">{I["wa"]}Send request on WhatsApp</button>
      <p class="fine">Opens WhatsApp with your message filled in. Nothing is sent until you tap send.</p>
    </form>
  </div>
</div></section>
<section class="sec tight"><div class="wrap">
  <p class="eyebrow">{DOTS} Find us</p>
  <h2 class="h2 rv" style="margin-bottom:28px">Kamutiini, Lower Kabete.</h2>
  <div class="map rv"><iframe title="Map of Kamutiini, Lower Kabete" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={urllib.parse.quote(MAPQ)}&amp;z=14&amp;output=embed"></iframe></div>
  <p style="margin-top:16px"><a class="btn btn-dark btn-sm" href="{MAPS}" target="_blank" rel="noopener">{I["pin"]}Get directions</a></p>
</div></section>
'''
    return head('Contact · Demosh Designs', 'Call or WhatsApp Demosh Designs on +254 704 121 852, or visit us in Kamutiini, Lower Kabete. Open 24 hours. Request a quote online.', 'contact.html') + body + foot()

def build_404():
    body = f'''<section class="hero sub" style="min-height:100svh;align-items:center">
  <div class="hero-media"></div>
  <div class="wrap"><h1>Misprint. <em>404</em></h1><p class="lead">This page doesn't exist. Let's get you back to something good.</p>
  <div class="ctas"><a class="btn btn-y" href="index.html">Go home</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div></div>
</section>'''
    return head('Page not found · Demosh Designs', 'Page not found.', '') .replace('href="assets/', 'href="/assets/').replace('href="index.html"', 'href="/"') + body + foot().replace('src="assets/', 'src="/assets/')

files = {
 'index.html': build_index(), 'services.html': build_services(), 'gallery.html': build_gallery(),
 'about.html': build_about(), 'contact.html': build_contact(), '404.html': build_404(),
}
for name, html in files.items():
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(html)
print('built', list(files))
