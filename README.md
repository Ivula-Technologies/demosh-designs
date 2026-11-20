# Demosh Designs website: setup notes

Client: Demosh Designs (owner Gordon Omala), Kamutiini, Lower Kabete. Phone/WhatsApp +254 704 121 852, open 24 hours.
Built by Ivula Technologies from the WhatsApp Business profile.

## What it is
Five pages (Home, Services, Gallery, About, Contact) plus a 404 page. Plain HTML/CSS/JS: no database, no build step, runs on any cPanel plan or on Vercel.
- Full-screen looping, muted background video on every page hero, with a colour gradient fallback while it loads (and for visitors who turn off motion or use data saver).
- Contact page: WhatsApp, click-to-call, Google Maps link and embedded map of Kamutiini, Lower Kabete, and a quote form that opens WhatsApp with the request already typed.
- Floating WhatsApp button on every page. Every service has its own pre-typed WhatsApp message.

## Upload to cPanel
1. cPanel > File Manager > `public_html` of the domain.
2. Upload `demosh-designs-website.zip`, then Extract. Files sit at the top of the zip so they land straight in `public_html` (turn on "Show hidden files" to see `.htaccess`).
3. Run AutoSSL so the site opens on https (`.htaccess` redirects to https).

## Videos
Free-licence Mixkit clips (commercial use, no credit needed), streamed from Mixkit:
hero 45527 (sewing machine, slow motion), apparel 34707, branding 45750, gifts 15082, printing 25260, detail band 12525, services 11696, gallery 48152, about 11698, needle 32433, contact 22382.
To serve one from the client's own hosting, download https://assets.mixkit.co/videos/<id>/<id>-720.mp4 and save it as `assets/media/<name>.mp4` (names: hero, apparel, branding, gifts, printing, detail, services-hero, gallery-hero, about-hero, needle, contact-hero). The page uses a local file first automatically when it exists.

## Gallery
Shows drawn sample mock-ups (labelled as samples) until real photos exist. To add a real job: put the photo in `assets/gallery/` and edit `assets/js/gallery.js` (add `img: 'assets/gallery/photo.jpg'` to an entry or add a new entry).

## Still needed from Gordon
1. Logo (PNG with transparent background or SVG). The site uses a typed "Demosh" wordmark with CMYK dots for now.
2. Real photos of finished work (10 to 20 is plenty) for the gallery and service sections.
3. The exact Facebook page link (the site links to a Facebook search for "Demosh Designs" for now; replace `https://www.facebook.com/search/top?q=Demosh%20Designs` in the pages).
4. A Google Maps pin for the shop if he wants a precise map instead of the area.
5. Confirm the product list on the Home page ("Ask us about") and Services page matches what he actually offers.
6. Domain name.

## Editing
The pages are generated from `tools/build.py` (shared header and footer). Edit it and run `python3 tools/build.py`, or edit the HTML directly. The site lives at the repo root: Vercel deploys `main` with no build step.
