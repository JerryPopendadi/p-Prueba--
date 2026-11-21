"""5 more carousels in the THE FACES PARTNERS story style. English, no prices."""
import os, json
D = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(D, 'carousel4.py'), encoding='utf-8').read()
exec(src[:src.index('jobs = []')])  # CSS, page(), I, FONTS

C = [
 ('ritual', 'RITUAL', [
  ('photo', 'sense-sight.jpg', 'THE FIVE ELEMENTS', 'Not a massage.\nA ritual.', 'Every visit is a journey: welcome, transition, care and return.'),
  ('photo', 'g01-face.jpg', '01 · EARTH', 'Grounding\nand calm', 'Warm stones, natural textures and slow hands.'),
  ('photo', 'sense-touch.jpg', '02 · WATER', 'The ritual begins\nwith water', 'Cleansing, flow and renewal.'),
  ('photo', 'sense-smell.jpg', '03 · FIRE & AIR', 'Warmth.\nBreath. Scent.', 'Warm oils, music and aroma composed for each ritual.'),
  ('photo', 'sense-intuition.jpg', '04 · LOVE', 'The element\nthat stays with you', 'Care, connection and the feeling guests come back for.'),
  ('dark', None, '05 · FOR PARTNERS', 'A concept\nno one can copy.', 'Protected in Indonesia. The reason guests return, and the heart of every THE FACES spa.'),
  ('cta', None, 'CURIOUS?', 'Comment «RITUAL»\nbelow', 'and we will send you the full story'),
 ], "🌿 Not a massage. A ritual.\n\nAt THE FACES every visit follows the Five Elements: Earth, Water, Fire, Air and Love. A welcome, a transition, the care itself and a calm return to everyday life.\n\nThat is what guests remember, and why they come back.\n\nFor our partners, it means something more: a signature concept, protected in Indonesia, at the heart of every THE FACES spa.\n\nComment «RITUAL» and we will send you the full story 👇\n\nInformation only, not a public offer.\n#Bali #Ubud #Sanur #SpaRitual #FiveElements #THEFACESPARTNERS"),
 ('founders', 'FOUNDERS', [
  ('photo', 'founders.jpg', 'THE FOUNDERS', 'Anna &\nEvgenii Dubinin', 'More than twenty years in beauty and wellness.'),
  ('photo', 'g04-interior.jpg', '01 · 2013', 'Our first salon\nin Bali', 'Built salon by salon, with our own hands and our own team.'),
  ('photo', 'g08-interior.jpg', '02', 'A family business,\nnot a fund', 'You talk to us directly. No intermediaries, no sales agents.'),
  ('photo', 'g11-proc-s.jpg', '03', 'Anna: concept,\nrituals, brand', 'The Five Elements, the menu and the guest experience.'),
  ('photo', 'DSC03214-scaled.jpg', '04', 'Evgenii: building\nand operations', 'Construction, teams and the day-to-day running of every spa.'),
  ('dark', None, '05 · TODAY', 'Four spa projects\nin Ubud and Sanur.', 'And room for a few partners who share the vision.'),
  ('cta', None, 'WANT TO MEET US?', 'Comment «FOUNDERS»\nbelow', 'and we will arrange a private call'),
 ], "🤝 A family business, not a fund.\n\nWe are Anna and Evgenii Dubinin. For more than twenty years we have created and run beauty and wellness concepts, and in 2013 we opened our first salon in Bali.\n\nAnna leads the concept, the rituals and the brand. Evgenii builds the spaces and runs the operations.\n\nToday THE FACES has four spa projects in Ubud and Sanur, and room for a few partners who share the vision. You talk to us directly. No intermediaries.\n\nComment «FOUNDERS» and we will arrange a private call 👇\n\nInformation only, not a public offer.\n#Bali #FounderStory #WellnessBusiness #Spa #THEFACESPARTNERS"),
 ('day', 'DAY', [
  ('photo', 'DSC03305-scaled.jpg', 'A DAY AT THE FACES', 'This is what\nyou would be part of', 'From the first guest to the last candle.'),
  ('photo', 'g08-interior.jpg', '09:00', 'The doors open', 'Fresh flowers, warm tea and the first guests of the day.'),
  ('photo', 'g02-face-s.jpg', '11:00', 'Hands that know\nthe face', 'Sculpting facial massage, one of our signature rituals.'),
  ('photo', 'g10-proc-s.jpg', '15:00', 'Water and silence', 'Head spa: the ritual guests book again and again.'),
  ('photo', 'DSC03501-scaled.jpg', '20:00', 'Slow evenings', 'Couples rituals and the last guests of the day.'),
  ('dark', None, 'BEHIND THE SCENES', 'Our team runs it.\nEvery single day.', 'Staff, rituals, bookings and marketing. Partners receive a monthly report.'),
  ('cta', None, 'WANT TO SEE IT LIVE?', 'Comment «DAY»\nbelow', 'and we will invite you for a visit'),
 ], "☀️ A day at THE FACES.\n\n09:00 · The doors open. Fresh flowers, warm tea, the first guests.\n11:00 · Sculpting facial massage, one of our signature rituals.\n15:00 · Head spa: water, silence and the ritual guests book again and again.\n20:00 · Slow evenings and couples rituals.\n\nBehind it all, our team runs every detail, every single day. Partners receive a monthly report.\n\nThis is what you would be part of.\n\nComment «DAY» and we will invite you for a visit 👇\n\nInformation only, not a public offer.\n#Bali #DayInTheLife #Spa #Ubud #Sanur #THEFACESPARTNERS"),
 ('hotel', 'HOTEL', [
  ('photo', 'waterfall.jpg', 'HOTEL & VILLA OWNERS', 'A spa your guests\nwill remember', 'Without building a spa team yourself.'),
  ('photo', 'g06-interior.jpg', '01', 'We create\nthe concept', 'Signature rituals, design and the guest journey.'),
  ('photo', 'g05-interior-s.jpg', '02', 'We train\nthe team', 'Therapists, service standards and the Five Elements rituals.'),
  ('photo', 'g12-proc-s.jpg', '03', 'We run\nthe spa', 'Bookings, marketing, quality and regular reporting.'),
  ('photo', 'DSC03400-scaled.jpg', '04', 'Your guests\nstay longer', 'A spa gives them one more reason to choose you.'),
  ('dark', None, 'FOUR FORMATS', 'Development · Management\nHotel spa · Licensing', 'Every partnership is shaped around your property.'),
  ('cta', None, 'HAVE A PROPERTY?', 'Comment «HOTEL»\nbelow', 'and we will contact you personally'),
 ], "🏝 Own a hotel, resort or villa?\n\nGuests choose a property for the experience, and a spa is often the moment they remember.\n\nTHE FACES can create the concept, train the team and run the spa for you, with our Five Elements rituals and regular reporting. Four formats: spa development, wellness management, hotel spa and licensing.\n\nComment «HOTEL» and we will contact you personally 👇\n\nInformation only, not a public offer.\n#HotelSpa #Hospitality #Bali #VillaOwners #THEFACESPARTNERS"),
 ('steps', 'PARTNER', [
  ('photo', 'dsc.jpg', 'HOW IT WORKS', 'From first call\nto partnership', 'Five calm steps. No pressure, no obligation.'),
  ('photo', 'g03-face-s.jpg', 'STEP 1', 'A private call', '30 minutes with the founders. Ask anything.'),
  ('photo', 'DSC03255-scaled.jpg', 'STEP 2', 'Visit the spa', 'Book a treatment as a guest and meet the team.'),
  ('photo', 'g07-interior-s.jpg', 'STEP 3', 'Review the documents', 'Accounts, lease, licences and structure, with your own advisers.'),
  ('photo', 'g09-proc-s.jpg', 'STEP 4', 'Agree in writing', 'Your role, reporting and terms, set out clearly.'),
  ('dark', None, 'STEP 5', 'We run the spa.\nYou stay informed.', 'Monthly reports and direct access to the founders.'),
  ('cta', None, 'READY FOR STEP 1?', 'Comment «PARTNER»\nbelow', 'and we will send you a link to book a call'),
 ], "📋 How a partnership with THE FACES works.\n\n1️⃣ A private 30-minute call with the founders\n2️⃣ Visit the spa as a guest and meet the team\n3️⃣ Review the documents with your own advisers\n4️⃣ Agree everything in writing\n5️⃣ We run the spa, you receive monthly reports\n\nNo pressure, no obligation. Just facts before decisions.\n\nComment «PARTNER» and we will send you a link to book a call 👇\n\nInformation only, not a public offer.\n#Partnership #Bali #SpaBusiness #Wellness #THEFACESPARTNERS"),
]

if __name__ == '__main__':
    out = os.path.join(D, 'instagram-more'); os.makedirs(out, exist_ok=True)
    jobs, md = [], ['# THE FACES PARTNERS · 5 more carousels (English, no prices)\n']
    CAL = 'https://calendar.app.google/b7nddp1H5fBoGYT98'
    for n, (slug, kw, slides, cap) in enumerate(C, 1):
        for i, sl in enumerate(slides):
            f = os.path.join(out, f'{n:02d}-{slug}-{i+1:02d}.html'); open(f, 'w').write(page(i, sl, len(slides))); jobs.append(f)
        link = f'https://thefacespeace.com/invest-in-a-spa-in-bali-3-projects-the-faces-invest/?utm_source=instagram&utm_medium=social&utm_campaign=comment_{kw.lower()}'
        md.append(f'## {n}. {slug} · images {n:02d}-{slug}-01 … 07\n\n### Post text\n{cap}\n\n### Automatic reply to «{kw}»\nThank you for your interest! Here is more about THE FACES PARTNERS: {link} · Book a call with the founders: {CAL}\n')
    json.dump(jobs, open('/tmp/claude-0/-home-user-p-Prueba--/da6eeaca-3a38-54c2-b2cc-cd456339a57d/scratchpad/ig_jobs.json', 'w'))
    open(os.path.join(out, 'post-texts-EN.md'), 'w').write('\n'.join(md))
    print(len(jobs))
