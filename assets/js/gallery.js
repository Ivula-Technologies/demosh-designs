/* Demosh Designs gallery.
   Each entry shows a drawn sample mock-up until a real photo is added.
   To show a real job: put the photo in assets/gallery/ and add  img: 'assets/gallery/your-photo.jpg'  to the entry
   (or add a new entry). cat must be one of: apparel, branding, gifts, printing. */
window.DEMOSH_GALLERY = [
  { cat: 'apparel',  img: 'assets/img/products/tshirt.jpg',   title: 'Custom round-neck T-shirt' },
  { cat: 'apparel',  img: 'assets/img/products/jerseys.jpg',  title: 'Custom football jerseys' },
  { cat: 'branding', img: 'assets/img/products/polo.jpg',     title: 'Branded polo shirt' },
  { cat: 'gifts',    img: 'assets/img/products/umbrella.jpg', title: 'Branded umbrella' },
  { cat: 'apparel',  img: 'assets/img/products/hoodie.jpg',   title: 'Custom hoodie' },
  { cat: 'branding', img: 'assets/img/products/cap.jpg',      title: 'Branded caps' },
  { cat: 'printing', img: 'assets/gallery/demosh-flyer.jpg',  title: 'Demosh Designs flyer' },
  { cat: 'apparel',  type: 'tee',      bg: '#e8f7fd', color: '#0e0b16', ink: '#ffd21f', label: 'CLASS OF 26', title: 'Class or team T-shirts' },
  { cat: 'branding', type: 'card',     bg: '#fff1f7', color: '#0e0b16', ink: '#ff2d87', label: 'YOUR BRAND', title: 'Business cards' },
  { cat: 'gifts',    type: 'mug',      bg: '#fff8dc', color: '#ffffff', ink: '#ff2d87', label: 'BEST DAD', title: 'Personalised mugs' },
  { cat: 'apparel',  type: 'hoodie',   bg: '#f1ece3', color: '#ff2d87', ink: '#ffffff', label: 'CREW', title: 'Branded hoodies' },
  { cat: 'printing', type: 'banner',   bg: '#e8f7fd', color: '#00b8f0', ink: '#ffffff', label: 'GRAND OPENING', title: 'Banners and roll-ups' },
  { cat: 'apparel',  type: 'cap',      bg: '#fff1f7', color: '#0e0b16', ink: '#00b8f0', label: 'TEAM', title: 'Embroidered or printed caps' },
  { cat: 'gifts',    type: 'tote',     bg: '#f1ece3', color: '#efe4cf', ink: '#0e0b16', label: 'HANDLE WITH LOVE', title: 'Tote bags' },
  { cat: 'branding', type: 'polo',     bg: '#fff8dc', color: '#00b8f0', ink: '#ffffff', label: 'STAFF', title: 'Staff uniforms' },
  { cat: 'printing', type: 'sticker',  bg: '#e8f7fd', color: '#ffd21f', ink: '#0e0b16', label: 'FRESH', title: 'Stickers and labels' },
  { cat: 'gifts',    type: 'bottle',   bg: '#fff1f7', color: '#0e0b16', ink: '#ffd21f', label: 'STAY HYDRATED', title: 'Branded water bottles' },
  { cat: 'apparel',  type: 'tee',      bg: '#fff8dc', color: '#ff2d87', ink: '#ffffff', label: 'BIRTHDAY SQUAD', title: 'Event and birthday tees' },
  { cat: 'printing', type: 'flyer',    bg: '#f1ece3', color: '#ffffff', ink: '#ff2d87', label: 'BIG SALE', title: 'Flyers and posters' }
];

window.demoshMock = function (it) {
  var c = it.color, k = it.ink, L = it.label, bg = it.bg;
  var stroke = (c === '#ffffff' || c === '#efe4cf') ? '#d9d0c0' : 'rgba(0,0,0,.18)';
  function txt(x, y, size, fill, extra) {
    return '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="' + size + '" fill="' + fill + '" letter-spacing="-0.5" ' + (extra || '') + '>' + L + '</text>';
  }
  function dots(x, y, r) {
    return '<g><circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="#00b8f0"/><circle cx="' + (x + r * 2.6) + '" cy="' + y + '" r="' + r + '" fill="#ff2d87"/><circle cx="' + (x + r * 5.2) + '" cy="' + y + '" r="' + r + '" fill="#ffd21f"/></g>';
  }
  var fs = L.length > 10 ? 22 : 30;
  var s = '';
  switch (it.type) {
    case 'tee':
      s = '<svg viewBox="0 0 400 440" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="440" fill="' + bg + '"/>' +
        '<path d="M140 70 L95 85 L40 140 L78 185 L110 160 L110 380 L290 380 L290 160 L322 185 L360 140 L305 85 L260 70 Q200 112 140 70Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<path d="M140 70 Q200 112 260 70" fill="none" stroke="' + stroke + '" stroke-width="5"/>' +
        dots(170, 200, 8) + txt(200, 255, fs, k) + '<rect x="150" y="272" width="100" height="5" rx="2.5" fill="' + k + '" opacity=".6"/></svg>';
      break;
    case 'hoodie':
      s = '<svg viewBox="0 0 400 480" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="480" fill="' + bg + '"/>' +
        '<path d="M150 80 Q200 30 250 80 L310 100 L360 200 L360 380 L320 385 L315 220 L300 210 L300 420 L100 420 L100 210 L85 220 L80 385 L40 380 L40 200 L90 100Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<path d="M150 80 Q200 160 250 80" fill="rgba(0,0,0,.18)"/><path d="M190 125 L186 175 M210 125 L214 175" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".8"/>' +
        '<rect x="130" y="320" width="140" height="60" rx="14" fill="rgba(0,0,0,.12)"/>' + txt(200, 265, 44, k) + '</svg>';
      break;
    case 'cap':
      s = '<svg viewBox="0 0 400 340" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="340" fill="' + bg + '"/>' +
        '<path d="M80 220 Q80 90 200 85 Q320 90 320 220Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<path d="M60 222 Q200 200 350 222 Q370 245 330 255 Q200 235 70 255 Q40 245 60 222Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2" opacity=".95"/>' +
        '<circle cx="200" cy="88" r="8" fill="' + k + '"/><path d="M200 90 L200 215" stroke="rgba(255,255,255,.15)" stroke-width="2"/>' +
        txt(200, 175, 40, k) + '</svg>';
      break;
    case 'mug':
      s = '<svg viewBox="0 0 400 380" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="380" fill="' + bg + '"/>' +
        '<path d="M290 140 Q360 140 355 205 Q350 265 285 262" fill="none" stroke="' + stroke + '" stroke-width="22"/><path d="M290 140 Q360 140 355 205 Q350 265 285 262" fill="none" stroke="' + c + '" stroke-width="16"/>' +
        '<path d="M90 95 L300 95 L292 305 Q290 320 275 320 L115 320 Q100 320 98 305Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<ellipse cx="195" cy="95" rx="105" ry="16" fill="#e9e2d6" stroke="' + stroke + '" stroke-width="2"/>' +
        '<path d="M150 170 q15 -22 30 0 q15 -22 30 0 q0 25 -30 42 q-30 -17 -30 -42z" fill="' + k + '" transform="translate(15 -10)"/>' +
        txt(195, 255, 34, '#0e0b16') + '</svg>';
      break;
    case 'tote':
      s = '<svg viewBox="0 0 400 470" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="470" fill="' + bg + '"/>' +
        '<path d="M140 150 Q140 50 200 50 Q260 50 260 150" fill="none" stroke="#c9b993" stroke-width="12"/>' +
        '<rect x="80" y="140" width="240" height="280" rx="6" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<circle cx="200" cy="245" r="52" fill="none" stroke="' + k + '" stroke-width="5"/>' + dots(173, 245, 9) +
        '<text x="200" y="345" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="20" fill="' + k + '">' + L + '</text></svg>';
      break;
    case 'card':
      s = '<svg viewBox="0 0 400 330" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="330" fill="' + bg + '"/>' +
        '<g transform="rotate(-8 200 165)"><rect x="70" y="80" width="250" height="150" rx="10" fill="#fff" stroke="#e1d8c8" stroke-width="2"/>' +
        '<rect x="70" y="80" width="10" height="150" fill="' + k + '"/><text x="100" y="150" font-family="Arial" font-size="14" fill="#55505f">Name Surname</text><text x="100" y="170" font-family="Arial" font-size="11" fill="#8a8494">+254 700 000 000</text></g>' +
        '<g transform="rotate(6 200 165)"><rect x="95" y="105" width="250" height="150" rx="10" fill="' + c + '"/>' + dots(130, 150, 9) +
        '<text x="125" y="210" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="30" fill="' + k + '">' + L + '</text></g></svg>';
      break;
    case 'banner':
      s = '<svg viewBox="0 0 400 520" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="520" fill="' + bg + '"/>' +
        '<rect x="110" y="40" width="180" height="420" rx="4" fill="' + c + '"/><rect x="100" y="455" width="200" height="22" rx="6" fill="#2a2633"/><rect x="104" y="30" width="192" height="14" rx="5" fill="#2a2633"/>' +
        '<circle cx="200" cy="150" r="55" fill="#ffd21f"/><circle cx="200" cy="150" r="30" fill="#ff2d87"/>' +
        '<text x="200" y="270" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="34" fill="' + k + '">GRAND</text>' +
        '<text x="200" y="305" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="34" fill="' + k + '">OPENING</text>' +
        '<rect x="140" y="340" width="120" height="8" rx="4" fill="#fff" opacity=".7"/><rect x="155" y="358" width="90" height="8" rx="4" fill="#fff" opacity=".5"/></svg>';
      break;
    case 'polo':
      s = '<svg viewBox="0 0 400 440" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="440" fill="' + bg + '"/>' +
        '<path d="M150 70 L95 88 L45 150 L82 188 L110 166 L110 390 L290 390 L290 166 L318 188 L355 150 L305 88 L250 70 L200 100Z" fill="' + c + '" stroke="' + stroke + '" stroke-width="2"/>' +
        '<path d="M150 70 L175 120 L200 100 L225 120 L250 70" fill="' + c + '" stroke="rgba(0,0,0,.25)" stroke-width="3"/><path d="M200 100 L200 165" stroke="rgba(0,0,0,.25)" stroke-width="3"/><circle cx="200" cy="130" r="4" fill="#fff"/><circle cx="200" cy="152" r="4" fill="#fff"/>' +
        dots(240, 175, 6) + '<text x="256" y="205" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="16" fill="' + k + '">' + L + '</text></svg>';
      break;
    case 'sticker':
      s = '<svg viewBox="0 0 400 360" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="360" fill="' + bg + '"/>' +
        '<g transform="rotate(-10 150 170)"><circle cx="150" cy="170" r="92" fill="#fff"/><circle cx="150" cy="170" r="80" fill="' + c + '"/>' + txt(150, 182, 36, k) + '</g>' +
        '<g transform="rotate(12 285 220)"><rect x="220" y="160" width="130" height="120" rx="26" fill="#fff"/><rect x="230" y="170" width="110" height="100" rx="20" fill="#ff2d87"/>' + dots(255, 220, 8) + '</g>' +
        '<g transform="rotate(8 300 90)"><rect x="250" y="55" width="110" height="60" rx="30" fill="#fff"/><rect x="258" y="63" width="94" height="44" rx="22" fill="#00b8f0"/></g></svg>';
      break;
    case 'bottle':
      s = '<svg viewBox="0 0 400 500" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="500" fill="' + bg + '"/>' +
        '<rect x="168" y="40" width="64" height="40" rx="10" fill="#3a3545"/><path d="M160 80 L240 80 L262 130 L262 440 Q262 460 242 460 L158 460 Q138 460 138 440 L138 130Z" fill="' + c + '"/>' +
        '<rect x="150" y="135" width="10" height="300" rx="5" fill="rgba(255,255,255,.12)"/>' +
        '<text x="200" y="300" text-anchor="middle" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="20" fill="' + k + '" transform="rotate(-90 200 290)">' + L + '</text></svg>';
      break;
    case 'flyer':
      s = '<svg viewBox="0 0 400 500" role="img" aria-label="' + it.title + ' mock-up"><rect width="400" height="500" fill="' + bg + '"/>' +
        '<g transform="rotate(-4 200 250)"><rect x="80" y="50" width="240" height="340" fill="#fff" stroke="#e1d8c8" stroke-width="2"/>' +
        '<rect x="80" y="50" width="240" height="150" fill="#0e0b16"/><circle cx="250" cy="125" r="46" fill="' + k + '"/><circle cx="160" cy="105" r="22" fill="#ffd21f"/>' +
        '<text x="105" y="250" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="40" fill="#0e0b16">BIG</text>' +
        '<text x="105" y="292" font-family="Bricolage Grotesque,Arial,sans-serif" font-weight="800" font-size="40" fill="' + k + '">SALE</text>' +
        '<rect x="105" y="320" width="150" height="7" rx="3.5" fill="#d6cfc2"/><rect x="105" y="338" width="110" height="7" rx="3.5" fill="#d6cfc2"/></g>' +
        '<g transform="rotate(7 230 300)"><rect x="200" y="300" width="150" height="160" fill="#00b8f0"/>' + dots(225, 340, 9) + '</g></svg>';
      break;
  }
  return s;
};
