# Batch 2: eight long SEO articles (English) for thefacesbali.com.
# Prices and durations from the Altegio menu (thefaces/src/menu.py, 14 Nov 2026).
from articles import UB, SA, WA_U, WA_S, book

def related(*items):
    lis = ''.join('<li><a href="/%s/">%s</a></li>' % (s, t) for s, t in items)
    return '<h2>Keep reading</h2><ul>%s</ul>' % lis

R_UBUD = ("best-spa-in-ubud-guide", "Best spa in Ubud: how to choose your treatment")
R_HEAD = ("head-spa-bali-guide", "Head spa in Bali: hair spa, Shirodhara and scalp detox")
R_FACE = ("face-massage-bali-guide", "Face massage in Bali: which technique to choose")
R_SANUR = ("spa-in-sanur-guide", "Spa in Sanur: treatments, prices and tips")
R_COUPLE = ("couples-spa-bali-honeymoon", "Couples spa in Bali: rituals for two")
R_MASS = ("massage-in-ubud-guide", "Massage in Ubud: types, prices and tips")
R_FACIAL = ("facial-bali-skin-care-guide", "Facial in Bali: the complete skin care guide")
R_LYMPH = ("lymphatic-drainage-massage-bali", "Lymphatic drainage massage in Bali")

ARTICLES2 = [
dict(
 slug="massage-in-ubud-guide", catkey="rituals", cat="Rituals · 9 min read", img="g04-interior.webp",
 title="Massage in Ubud: Types, Prices and How to Choose (2026)",
 seo_title="Massage in Ubud 2026: Types, Prices & Best Treatments | THE FACES Ubud",
 metadesc="Every type of massage in Ubud explained: Balinese, full body, fire, foot reflexology, lymphatic and face massage. Real prices, durations and booking tips.",
 excerpt="A practical guide to massage in Ubud: the main types, what each one does, honest prices, how long to book and how to recognise a good therapist.",
 faq=[
  ("How much is a massage in Ubud?", "At THE FACES Ubud a full body massage costs IDR 650,000 for 60 minutes, IDR 900,000 for 90 minutes and IDR 950,000 for 120 minutes. Reflexology starts at IDR 300,000 for 30 minutes."),
  ("Which massage is best after hiking Mount Batur?", "A 90-minute full body massage or the Fire Massage, combined with a leg massage, is ideal after a volcano hike or long walks."),
  ("How long should a massage be?", "60 minutes is enough for a relaxing massage. Choose 90 or 120 minutes if you have muscle tension or want time for the back, legs and neck."),
  ("Is THE FACES Ubud open in the evening?", "Yes, THE FACES Ubud is open every day until 22:00, so you can book a massage after dinner."),
 ],
 html=f"""<p>Massage is part of daily life in Ubud. You will find it in tiny family studios, in yoga retreats and in luxury resorts, at prices that go from a few dollars to a few hundred. That choice is wonderful, but it also makes it easy to end up with a rushed, forgettable treatment. This guide explains the main types of massage you will find in Ubud, what each one is good for, what a fair price looks like and how to choose the right one for your body and your day.</p>

<h2>Why Ubud is the best place in Bali for a massage</h2>
<p>Ubud has been the island's centre of healing arts for generations. Many Balinese families have passed massage techniques from parents to children, and the town now attracts therapists trained in Ayurveda, Chinese medicine, osteopathy and modern sports massage. Add the calm of the rice fields and the jungle, and you have the perfect setting to slow down. The challenge is not finding a massage, it is finding a good one.</p>

<h2>The main types of massage in Ubud</h2>

<h3>Balinese massage</h3>
<p>The traditional massage of the island combines firm palm and thumb pressure, gentle stretches and long strokes with warm oil. It releases tension and improves circulation. In our salon the Balinese technique is the base of the full body massage.</p>

<h3>Full body massage</h3>
<p>The classic choice: back, legs, arms, neck and shoulders, with pressure adapted to you. At THE FACES Ubud:</p>
<ul>
<li>60 min: IDR 650,000</li>
<li>90 min: IDR 900,000</li>
<li>120 min: IDR 950,000</li>
</ul>
<p>If it is your first massage in Bali, choose 90 minutes: it gives the therapist time to work on the areas that really need it.</p>

<h3>Fire Massage · 90 min · IDR 1,100,000</h3>
<p>Our warming massage for deep tension. Heat relaxes the muscles so that the therapist can work deeper without pain. Perfect after a Mount Batur sunrise hike, a surf lesson or days on a scooter.</p>

<h3>Foot reflexology</h3>
<p>Pressure on precise points of the feet, linked in reflexology to the whole body. It is deeply relaxing and ideal after walking the Campuhan Ridge or the Monkey Forest.</p>
<ul>
<li>30 min: IDR 300,000</li>
<li>60 min: IDR 500,000</li>
<li>90 min: IDR 600,000</li>
</ul>

<h3>Lymphatic drainage / relaxing leg massage</h3>
<p>Light, rhythmic movements that help the body release excess fluid. The best treatment for heavy, swollen legs after a long flight or hot days. 30 min IDR 300,000, 60 min IDR 500,000, 90 min IDR 600,000. Read our full guide to <a href="/lymphatic-drainage-massage-bali/">lymphatic drainage in Bali</a>.</p>

<h3>Face massage</h3>
<p>THE FACES is best known for face massage: myofascial (90 min, IDR 900,000), sculptural (90 min, IDR 850,000), buccal and gua sha (60 min, IDR 750,000). They lift and relax the face in a way no facial can. See our <a href="/face-massage-bali-guide/">face massage guide</a>.</p>

<h3>Head massage and head spa</h3>
<p>The Ayurvedic head massage (60 min, IDR 750,000) and our head spa treatments with warm water are perfect for stress and poor sleep. Everything is explained in our <a href="/head-spa-bali-guide/">head spa guide</a>.</p>

<h3>Foam massage and Airkiss</h3>
<p>Our signature foam rituals are unique in Ubud: the Airkiss Detox Ritual (60 min, IDR 1,200,000), the Foamy back &amp; leg massage (60 min, IDR 1,400,000) and the Foamy Dream Ritual (120 min, IDR 2,300,000), in which the body is wrapped in a warm cloud of foam.</p>

<h2>Which massage for which situation?</h2>
<table>
<thead><tr><th>Situation</th><th>Our recommendation</th></tr></thead>
<tbody>
<tr><td>First massage in Bali</td><td>Full body massage, 90 min</td></tr>
<tr><td>After Mount Batur or a long hike</td><td>Fire Massage + reflexology 30 min</td></tr>
<tr><td>Jet lag, poor sleep</td><td>Ayurvedic head massage or Shirodhara Hair Spa</td></tr>
<tr><td>Swollen legs after the flight</td><td>Lymphatic drainage leg massage, 60 min</td></tr>
<tr><td>Tired face, jaw tension</td><td>Myofascial facial massage</td></tr>
<tr><td>A special treat</td><td>Foamy Dream Ritual or a Five Elements ritual</td></tr>
</tbody>
</table>

<h2>How to recognise a good massage in Ubud</h2>
<ul>
<li><strong>The therapist asks questions before starting:</strong> pressure, injuries, areas to avoid.</li>
<li><strong>The duration is real:</strong> 60 minutes on the table, not 60 minutes including the time to change.</li>
<li><strong>Clean linen and quality oil:</strong> you should not smell old oil or see stained towels.</li>
<li><strong>A quiet room:</strong> no loud music from the street, no therapists chatting.</li>
<li><strong>No pressure to buy:</strong> a good spa recommends, it does not push packages.</li>
</ul>

<h2>Massage prices in Ubud explained</h2>
<p>Very cheap massages exist in Ubud, and some are good. But a price that is too low usually means less time, less training or tired therapists working long shifts. In a professional spa you pay for a specialised therapist, a calm room, clean linen, quality products and time before and after the treatment. At THE FACES the price on the <a href="/menu/">menu</a> is the final price and the duration is the real time with your therapist.</p>

<h2>Practical tips</h2>
<ol>
<li><strong>Book ahead</strong> for the evening: 17:00–21:00 is the busiest time in Ubud.</li>
<li><strong>Leave margin for traffic:</strong> the roads around Ubud centre are slow in the late afternoon.</li>
<li><strong>Eat lightly before</strong> and drink water after the massage.</li>
<li><strong>Tell the therapist about pregnancy, injuries or skin conditions.</strong></li>
<li><strong>Keep the hour after free:</strong> no scooter rush, no heavy dinner.</li>
</ol>

<h2>Book your massage in Ubud</h2>
<p>THE FACES Ubud, Jl. Raya Lungsiakan, Kedewatan, Ubud, Bali 80571. Open every day, 10:00–22:00. You can {book("ubud")} or write to us on <a href="{WA_U}" target="_blank" rel="noopener">WhatsApp</a>.</p>
""" + related(R_UBUD, R_FACE, R_HEAD, R_LYMPH)),

dict(
 slug="balinese-massage-guide", catkey="rituals", cat="Rituals · 8 min read", img="g05-interior-s.webp",
 title="Balinese Massage: What It Is, Benefits and What to Expect",
 seo_title="Balinese Massage: What It Is, Benefits & What to Expect | THE FACES Bali",
 metadesc="What is a Balinese massage? History, techniques, benefits, how it differs from Thai and Swedish massage, what to expect and where to book in Ubud and Sanur.",
 excerpt="Everything about Balinese massage: where it comes from, how it works, its benefits, how it compares with Thai and Swedish massage and how to prepare.",
 faq=[
  ("What is a Balinese massage?", "Balinese massage is the traditional massage of Bali. It combines firm pressure with the palms and thumbs, gentle stretches, acupressure and long strokes with warm oil to release tension and improve circulation."),
  ("Is Balinese massage painful?", "It should not be painful. The pressure is firm but always adapted to you: tell the therapist if you want it stronger or softer."),
  ("What is the difference between Balinese and Thai massage?", "Thai massage is done clothed, without oil, with many stretches. Balinese massage uses warm oil on the skin and combines pressure, acupressure and long relaxing strokes."),
  ("How long should a Balinese massage be?", "60 minutes is good for relaxation, 90 minutes is ideal for a complete treatment of the back, legs, arms, neck and shoulders."),
 ],
 html=f"""<p>Balinese massage is one of the reasons people fall in love with Bali. It is firm and deeply relaxing at the same time, and it reflects the Balinese idea of balance between body, mind and spirit. Whether you are about to book your first massage on the island or want to understand what makes it special, this guide explains everything you need to know.</p>

<h2>A short history of Balinese massage</h2>
<p>Traditional healing in Bali, often called <em>usada</em>, has been practised for centuries by healers known as <em>balian</em>. Over time, local techniques mixed with influences from India, through Ayurveda, and from China, through acupressure. The result is a massage style that uses pressure on energy points, stretching and aromatic oils from the island's plants. Today it is taught in spas and schools across Bali and is the base of most massages you will receive here.</p>

<h2>The techniques of a Balinese massage</h2>
<ul>
<li><strong>Palm and thumb pressure</strong> along the muscles of the back, legs and arms.</li>
<li><strong>Acupressure</strong> on specific points to release blocked tension.</li>
<li><strong>Gentle stretches</strong> of the arms, legs and back.</li>
<li><strong>Long, flowing strokes</strong> with warm oil that connect the whole body.</li>
<li><strong>Skin rolling and kneading</strong> to improve circulation.</li>
</ul>

<h2>Benefits of Balinese massage</h2>
<ul>
<li><strong>Muscle relaxation:</strong> it releases tension in the back, neck and shoulders.</li>
<li><strong>Better circulation:</strong> warmth and pressure help blood and lymph move.</li>
<li><strong>Stress relief:</strong> the slow rhythm calms the nervous system.</li>
<li><strong>Better sleep:</strong> many guests sleep deeply the night after a massage.</li>
<li><strong>Recovery:</strong> perfect after hikes, surf sessions and long travel days.</li>
</ul>
<p>Massage supports well-being; it is not a medical treatment. If you have a health condition, talk to your doctor first.</p>

<h2>Balinese, Thai or Swedish massage?</h2>
<table>
<thead><tr><th></th><th>Balinese</th><th>Thai</th><th>Swedish</th></tr></thead>
<tbody>
<tr><td>Oil</td><td>Yes, warm oil</td><td>No, done clothed</td><td>Yes</td></tr>
<tr><td>Pressure</td><td>Firm, adapted</td><td>Firm, with body weight</td><td>Light to medium</td></tr>
<tr><td>Stretches</td><td>Gentle</td><td>Many, intense</td><td>None</td></tr>
<tr><td>Feeling</td><td>Deep and relaxing</td><td>Energising</td><td>Soft and relaxing</td></tr>
</tbody>
</table>

<h2>What to expect at THE FACES</h2>
<ol>
<li><strong>Welcome and tea.</strong> You tell the therapist what you need: pressure, areas of tension, injuries.</li>
<li><strong>Changing.</strong> You receive disposable underwear and a robe. During the massage you are always covered with a towel, except the area being worked on.</li>
<li><strong>The massage.</strong> Back first, then legs, arms, neck and shoulders. You can ask for more or less pressure at any moment.</li>
<li><strong>Rest.</strong> A few quiet minutes and water or tea before you leave.</li>
</ol>

<h2>Prices at THE FACES</h2>
<ul>
<li>Full body massage, 60 min: IDR 650,000</li>
<li>Full body massage, 90 min: IDR 900,000 in Ubud, IDR 850,000 in Sanur</li>
<li>Full body massage, 120 min: IDR 950,000</li>
<li>Fire Massage, 90 min: IDR 1,100,000</li>
</ul>
<p>See more on the <a href="/body-massage/">body massage page</a> and in the <a href="/menu/">full menu</a>.</p>

<h2>How to prepare</h2>
<ul>
<li>Eat lightly at least an hour and a half before.</li>
<li>Shower before if you come from the beach or the pool.</li>
<li>Tell us if you are pregnant, have high blood pressure, varicose veins or recent injuries.</li>
<li>After the massage, drink water and avoid strong sun and alcohol for a few hours.</li>
</ul>

<h2>Book a Balinese massage</h2>
<p>You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
""" + related(R_MASS, R_UBUD, R_SANUR, R_LYMPH)),

dict(
 slug="facial-bali-skin-care-guide", catkey="face", cat="Face · 9 min read", img="g02-face-s.webp",
 title="Facial in Bali: The Complete Guide to Skin Care Treatments",
 seo_title="Facial in Bali: Cleansing, Hydration, Oxygen & Cryo Prices | THE FACES",
 metadesc="Which facial to choose in Bali? Atraumatic, vacuum, ultrasonic and combination cleansing, deep hydration, oxygen pen, cryomassage and Lymphatic Glow, with prices.",
 excerpt="Sun, humidity and sunscreen change your skin in Bali. Here is how to choose the right facial: cleansing, hydration, oxygen, cryomassage and more.",
 faq=[
  ("What is the best facial in Bali for sun-damaged skin?", "Deep skin hydration (80 min, IDR 1,000,000) is the best choice after days of sun. Combine it with a gentle atraumatic cleansing if your pores feel congested."),
  ("How much is a facial at THE FACES?", "Facial cleansings cost IDR 1,200,000 (atraumatic, vacuum or ultrasonic) or IDR 1,350,000 (combination). Deep hydration is IDR 1,000,000, the oxygen pen IDR 900,000 and cryomassage IDR 970,000."),
  ("Can I go in the sun after a facial?", "Avoid strong sun for the rest of the day, especially after a cleansing, and use a high SPF sunscreen for the next days."),
  ("Is a facial cleansing painful?", "Our atraumatic cleansing is designed to be gentle. Vacuum and ultrasonic cleansings are also comfortable; the therapist adapts the intensity to your skin."),
 ],
 html=f"""<p>Bali is wonderful for the soul and a little harder on the skin. Strong sun, humidity, sweat, salt water, chlorine and several layers of sunscreen a day clog pores, dehydrate the surface and make the complexion dull. A professional facial resets the skin so that you leave Bali glowing, not tired. This guide explains the facial treatments at THE FACES and helps you choose the right one.</p>

<h2>What the tropical climate does to your skin</h2>
<ul>
<li><strong>Congested pores:</strong> sweat and sunscreen mix and block the pores, especially on the nose and chin.</li>
<li><strong>Dehydration:</strong> sun and air conditioning take water from the skin, even when it looks oily.</li>
<li><strong>Dullness and uneven tone:</strong> the surface thickens to protect itself from UV.</li>
<li><strong>Puffiness:</strong> heat and salty food make the face swell in the morning.</li>
</ul>

<h2>Facial cleansing</h2>
<p>A professional cleansing removes impurities, opens congested pores and prepares the skin to absorb care. We offer four methods:</p>

<h3>Atraumatic facial cleansing · 110 min · IDR 1,200,000</h3>
<p>A gentle method that cleans deeply without aggressive extraction, so the skin does not stay red for days. Ideal for sensitive skin and for a first cleansing.</p>

<h3>Vacuum facial cleansing · 120 min · IDR 1,200,000</h3>
<p>A soft vacuum lifts impurities from the pores. Great for combination skin with blackheads.</p>

<h3>Ultrasonic facial cleansing · 120 min · IDR 1,200,000</h3>
<p>Ultrasonic vibrations exfoliate and clean without friction. A good choice for a fresh, even surface.</p>

<h3>Combination facial cleansing · 150 min · IDR 1,350,000</h3>
<p>Several methods in one session, for skin that needs a full reset.</p>

<h2>Hydration and glow</h2>
<ul>
<li><strong>Deep skin hydration</strong>, 80 min, IDR 1,000,000: the best answer to sun and air conditioning.</li>
<li><strong>Oxygen pen</strong>, 75 min, IDR 900,000: oxygen and active care for a fresh, radiant complexion.</li>
<li><strong>Cryomassage</strong>, 75 min, IDR 970,000: cold tightens pores, reduces puffiness and tones the skin.</li>
<li><strong>Lymphatic Glow</strong>, 90 min, IDR 1,000,000 (Ubud): lymphatic drainage of the face for a de-puffed, luminous result.</li>
<li><strong>Hydrolift</strong>, 60 min, IDR 850,000 (Sanur): intensive hydration with a lifting effect.</li>
</ul>

<h2>How to choose your facial</h2>
<table>
<thead><tr><th>Your skin</th><th>Our recommendation</th></tr></thead>
<tbody>
<tr><td>Sensitive, first facial</td><td>Atraumatic cleansing</td></tr>
<tr><td>Blackheads, combination skin</td><td>Vacuum or combination cleansing</td></tr>
<tr><td>Dehydrated after the sun</td><td>Deep skin hydration</td></tr>
<tr><td>Dull, tired</td><td>Oxygen pen</td></tr>
<tr><td>Puffy in the morning</td><td>Cryomassage or Lymphatic Glow</td></tr>
<tr><td>Before an event</td><td>Hydrolift + face massage (Sanur)</td></tr>
</tbody>
</table>

<h2>Facial and face massage: the perfect pair</h2>
<p>A facial cares for the surface of the skin; a face massage works on the muscles and the fascia underneath. Together they give the best result: clean, hydrated skin and a lifted contour. Book them on two different days, or ask for a combined plan. Read our <a href="/face-massage-bali-guide/">face massage guide</a>.</p>

<h2>Before and after your facial</h2>
<ul>
<li>Avoid sunbathing the day before and the day after a cleansing.</li>
<li>Come without make-up if you can.</li>
<li>Tell us about retinoids, acids, recent peels or injections.</li>
<li>Use a high SPF sunscreen and a light moisturiser for the following days.</li>
<li>Do not swim in the sea or the pool on the day of a cleansing.</li>
</ul>

<h2>Plan a skin routine for your holiday</h2>
<p>For a two-week stay, many guests book a cleansing at the start, a hydration in the middle and a face massage before flying home. Your skin is clean, hydrated and lifted for the photos and for the return.</p>

<h2>Book your facial</h2>
<p>More details on the <a href="/skin-care/">skin care page</a>. You can {book()}, or ask us on WhatsApp which facial suits your skin: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
""" + related(R_FACE, R_LYMPH, R_UBUD, R_SANUR)),

dict(
 slug="lymphatic-drainage-massage-bali", catkey="rituals", cat="Rituals · 7 min read", img="g09-proc-s.webp",
 title="Lymphatic Drainage Massage in Bali: Benefits, Prices and When to Book",
 seo_title="Lymphatic Drainage Massage Bali: Benefits & Prices | THE FACES",
 metadesc="Lymphatic drainage massage in Bali for swollen legs, jet lag and a de-puffed face. How it works, benefits, legs and face treatments, prices in Ubud and Sanur.",
 excerpt="Heavy legs after the flight? Puffy face in the heat? How lymphatic drainage works, its benefits and the best treatments for legs and face in Bali.",
 faq=[
  ("What is lymphatic drainage massage?", "It is a gentle, rhythmic massage that follows the direction of the lymphatic system to help the body release excess fluid. It reduces the feeling of heavy, swollen legs and a puffy face."),
  ("Is lymphatic drainage good after a long flight?", "Yes. After a long flight the legs often feel heavy and swollen. A 60-minute lymphatic drainage leg massage is one of the most popular treatments for arrival day."),
  ("How much is lymphatic drainage at THE FACES?", "The lymphatic drainage / relaxing leg massage costs IDR 300,000 for 30 minutes, IDR 500,000 for 60 minutes and IDR 600,000 for 90 minutes. Lymphatic Glow for the face is IDR 1,000,000 (90 min, Ubud)."),
  ("Who should avoid lymphatic drainage?", "People with thrombosis, acute infections, heart or kidney conditions or who are pregnant should consult a doctor first and tell the therapist before the treatment."),
 ],
 html=f"""<p>Long-haul flights, heat, humidity, salty food and cocktails by the pool: it is no surprise that many travellers in Bali wake up with heavy legs and a puffy face. Lymphatic drainage massage is one of the most effective ways to feel light again. Here is how it works, what it does and which treatment to choose at THE FACES.</p>

<h2>What is the lymphatic system?</h2>
<p>The lymphatic system is a network of vessels and nodes that carries fluid, called lymph, back towards the blood and helps the body eliminate waste. Unlike blood, lymph has no pump: it moves thanks to muscle movement and breathing. When we sit for hours on a plane or stay still in the heat, it slows down, and fluid accumulates in the legs and the face.</p>

<h2>How lymphatic drainage massage works</h2>
<p>The therapist uses light, slow, rhythmic movements that follow the direction of the lymphatic vessels towards the lymph nodes. The pressure is much softer than in a classic massage: the goal is not to work on the muscles, but to help the fluid move. Many guests find it surprisingly relaxing.</p>

<h2>Benefits</h2>
<ul>
<li><strong>Lighter legs</strong> after a long flight or a day on your feet.</li>
<li><strong>Less puffiness</strong> in the face and around the eyes.</li>
<li><strong>A defined contour</strong> of the face and the ankles.</li>
<li><strong>Deep relaxation</strong> thanks to the slow rhythm.</li>
</ul>

<h2>Lymphatic treatments at THE FACES</h2>

<h3>Lymphatic drainage / relaxing leg massage</h3>
<ul>
<li>30 min: IDR 300,000</li>
<li>60 min: IDR 500,000</li>
<li>90 min: IDR 600,000</li>
</ul>
<p>Available in Ubud and Sanur. The 60-minute version is the most booked on arrival day.</p>

<h3>Lymphatic Glow · 90 min · IDR 1,000,000 · Ubud</h3>
<p>Lymphatic drainage for the face: it reduces puffiness, defines the contour and gives a luminous complexion. Perfect the morning before an event.</p>

<h3>Gua sha massage · 60 min · IDR 750,000</h3>
<p>The traditional stone tool also drains the face beautifully.</p>

<h3>Before Flight Ritual · IDR 2,200,000</h3>
<p>Our ritual for the first or last day of your trip combines head spa, body and face care, so that you fly relaxed.</p>

<h2>When to book lymphatic drainage in Bali</h2>
<ul>
<li><strong>The day you arrive</strong> or the day after, to recover from the flight.</li>
<li><strong>After days of heat</strong> when the ankles start to swell.</li>
<li><strong>The morning of an event</strong>, for a de-puffed face.</li>
<li><strong>Before flying home</strong>, to prepare the legs for the flight.</li>
</ul>

<h2>Who should ask a doctor first</h2>
<p>Lymphatic drainage is gentle, but it is not suitable for everyone. If you have or had thrombosis, an acute infection, a heart or kidney condition, cancer treatment or if you are pregnant, consult your doctor first and tell the therapist before the session.</p>

<h2>Tips to support your lymph on holiday</h2>
<ul>
<li>Drink plenty of water, especially with alcohol and in the heat.</li>
<li>Walk and swim: muscle movement moves the lymph.</li>
<li>Raise your legs for ten minutes in the evening.</li>
<li>Limit very salty food.</li>
</ul>

<h2>Book your lymphatic drainage</h2>
<p>You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>. See all body treatments on the <a href="/body-massage/">body massage page</a>.</p>
""" + related(R_MASS, R_FACIAL, R_FACE, R_SANUR)),

dict(
 slug="foot-reflexology-bali", catkey="rituals", cat="Rituals · 6 min read", img="g12-proc-s.webp",
 title="Foot Reflexology in Bali: What It Is and Why Travellers Love It",
 seo_title="Foot Reflexology Bali: Benefits, Prices & Where to Book | THE FACES",
 metadesc="Foot reflexology in Bali after long walks, hikes and flights. What reflexology is, benefits, 30, 60 and 90-minute sessions and prices in Ubud and Sanur.",
 excerpt="After the rice terraces, the temples and the beach path, your feet deserve care. How foot reflexology works and which session to book.",
 faq=[
  ("What is foot reflexology?", "Foot reflexology is a massage technique that applies pressure to specific points on the feet. In reflexology each point is linked to an area of the body. It is deeply relaxing and relieves tired feet and legs."),
  ("How long is a reflexology session?", "At THE FACES you can choose 30, 60 or 90 minutes. 30 minutes is perfect as an add-on, 60 minutes as a complete treatment."),
  ("How much is foot reflexology in Bali?", "At THE FACES reflexology costs IDR 300,000 for 30 minutes, IDR 500,000 for 60 minutes and IDR 600,000 for 90 minutes."),
  ("Can I combine reflexology with a face massage?", "Yes. In Sanur the 4 hands treatment combines a face massage and foot reflexology at the same time, with two therapists (IDR 950,000)."),
 ],
 html=f"""<p>In Bali you walk more than you think: up and down the steps of temples, along the rice terraces, on the beach path in Sanur and through the streets of Ubud in sandals. By the end of the day the feet are tired and the legs heavy. Foot reflexology is the simplest way to recover, and one of the most relaxing treatments on our menu.</p>

<h2>What is reflexology?</h2>
<p>Reflexology is a massage technique based on the idea that points on the feet correspond to areas of the body. The therapist applies precise pressure with the thumbs and fingers, combined with relaxing strokes of the feet, the ankles and the lower legs. Whatever you think of the theory, the effect is easy to feel: the feet relax, the legs feel lighter and the whole body calms down.</p>

<h2>Benefits travellers notice</h2>
<ul>
<li>Relief for tired, sore feet after long walks.</li>
<li>Lighter legs after a flight or a day in the heat.</li>
<li>Deep relaxation, often with sleep during the session.</li>
<li>A gentle treatment that suits almost everyone, including older guests.</li>
</ul>

<h2>Reflexology at THE FACES</h2>
<ul>
<li>Reflexology foot massage, 30 min: IDR 300,000</li>
<li>Reflexology foot massage, 60 min: IDR 500,000</li>
<li>Reflexology foot massage, 90 min: IDR 600,000</li>
</ul>
<p>In Sanur, try <strong>4 hands</strong> (IDR 950,000): a face massage and foot reflexology at the same time, with two therapists. It is one of the most relaxing experiences you can have in Bali.</p>

<h2>How to use reflexology in your trip</h2>
<ul>
<li><strong>After a day of sightseeing:</strong> 60 minutes in the evening, Ubud is open until 22:00.</li>
<li><strong>As an add-on:</strong> 30 minutes after a face massage or a head spa.</li>
<li><strong>For the whole family:</strong> grandparents and parents can enjoy it side by side.</li>
<li><strong>After the beach path in Sanur:</strong> walk from the beach to our salon on Jl. Danau Buyan.</li>
</ul>

<h2>What to expect</h2>
<p>You sit comfortably in a reclining chair or lie on the treatment bed. The therapist cleans your feet with warm water, then works with oil or balm on the feet, the ankles and the calves. You can tell the therapist at any moment if the pressure is too strong. Some points may feel tender: that is normal and passes quickly.</p>

<h2>Who should ask first</h2>
<p>Tell us if you are pregnant, have diabetes with reduced sensation in the feet, open wounds, fungal infections or recent injuries. The therapist will adapt the treatment or suggest another one.</p>

<h2>Book your reflexology</h2>
<p>You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
""" + related(R_MASS, R_LYMPH, R_SANUR, R_UBUD)),

dict(
 slug="mens-spa-bali", catkey="rituals", cat="Rituals · 6 min read", img="g11-proc-s.webp",
 title="Spa for Men in Bali: Treatments Designed for Men",
 seo_title="Men's Spa Bali: Massage & Treatments for Men | THE FACES Ubud",
 metadesc="Spa treatments for men in Bali: Power Reset and Stress Free programmes, deep massage, head spa and face massage for men. Prices and tips in Ubud and Sanur.",
 excerpt="More and more men book spa treatments in Bali. The programmes designed for men at THE FACES, and the treatments men choose most.",
 faq=[
  ("Do you have spa treatments for men?", "Yes. In Ubud we offer two programmes designed for men: Power Reset (130 min, IDR 1,400,000) and Stress Free (120 min, IDR 2,100,000). All our massages, head spa and face treatments are also available for men."),
  ("What is the best massage for men after surfing?", "The Fire Massage (90 min, IDR 1,100,000) or a 90-minute full body massage, combined with a reflexology session for the legs and feet."),
  ("Is face massage for men too?", "Absolutely. Many men book the myofascial facial massage for jaw tension, screen fatigue and a fresher face before meetings or events."),
  ("Can I book with my partner?", "Yes, you can book side by side treatments or one of our couples rituals."),
 ],
 html=f"""<p>Spa is no longer just for women, and in Bali more and more men book massages, head spas and even face treatments. Whether you are recovering from surf sessions, long scooter rides, a Mount Batur hike or simply work stress, here is what THE FACES offers for men and how to choose.</p>

<h2>Why men book spa treatments in Bali</h2>
<ul>
<li><strong>Physical recovery:</strong> surf, hikes, gym and long rides leave sore muscles.</li>
<li><strong>Stress:</strong> many guests come to Bali to switch off from demanding jobs.</li>
<li><strong>Sleep and jet lag:</strong> a deep massage or head spa resets the body clock.</li>
<li><strong>Looking fresh:</strong> before a wedding, a meeting or a photo shoot.</li>
</ul>

<h2>Programmes designed for men (Ubud)</h2>

<h3>Power Reset · 130 min · IDR 1,400,000</h3>
<p>A programme to recover energy: deep work on the back, shoulders and legs, where men hold most tension, combined with treatments that restore focus.</p>

<h3>Stress Free · 120 min · IDR 2,100,000</h3>
<p>A complete reset for the nervous system, for men who arrive in Bali exhausted and want to switch off fast.</p>

<h2>The treatments men choose most</h2>
<ul>
<li><strong>Fire Massage</strong>, 90 min, IDR 1,100,000: warmth and deep pressure for tight muscles.</li>
<li><strong>Full body massage</strong>, 60 / 90 / 120 min: IDR 650,000 / 900,000 (850,000 in Sanur) / 950,000.</li>
<li><strong>Reflexology</strong>, 30 / 60 / 90 min: IDR 300,000 / 500,000 / 600,000.</li>
<li><strong>Water spa therapy with detox hair spa</strong>, 90 min, IDR 1,100,000: the head spa men end up loving.</li>
<li><strong>Myofascial facial massage</strong>, 90 min, IDR 900,000: for jaw clenching and screen fatigue.</li>
</ul>

<h2>Face massage for men: why it works</h2>
<p>Men clench their jaw more than they think, especially under stress or during sport. Tension in the jaw, the temples and the neck causes headaches and a tired face. A myofascial facial massage releases it in one session. Read our <a href="/face-massage-bali-guide/">face massage guide</a>.</p>

<h2>Practical tips for men</h2>
<ul>
<li>No need to shave before a face massage, but tell the therapist if your skin is irritated.</li>
<li>Ask for stronger pressure if you are used to deep massage, or softer if you are sunburnt.</li>
<li>After surf, wait until the skin has cooled down and shower before your massage.</li>
<li>Book in the evening: Ubud is open until 22:00.</li>
</ul>

<h2>Book your treatment</h2>
<p>You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
""" + related(R_MASS, R_HEAD, R_FACE, R_UBUD)),

dict(
 slug="things-to-do-in-sanur", catkey="news", cat="Guides · 9 min read", img="salon-sanur.jpg",
 title="Things to Do in Sanur: A Slow Guide to Bali's Calm Coast",
 seo_title="Things to Do in Sanur 2026: Beach, Sunrise, Food & Spa | THE FACES",
 metadesc="The best things to do in Sanur, Bali: sunrise on the beach path, cycling, snorkelling, day trips to Nusa Lembongan and Penida, night market, and a spa day.",
 excerpt="Sanur is Bali at a slower pace. Sunrise walks, cycling, island day trips, local food and a spa afternoon: our guide to the calm coast.",
 faq=[
  ("Is Sanur worth visiting?", "Yes. Sanur is calm, family-friendly and close to the airport, with a long beach path, sunrise views and easy boat trips to Nusa Lembongan and Nusa Penida."),
  ("What is Sanur best known for?", "Sanur is known for its sunrise, its long seafront path along the beach, calm water protected by the reef and its relaxed atmosphere."),
  ("How far is Sanur from the airport?", "The drive from Ngurah Rai airport to Sanur usually takes around 30 minutes, depending on traffic."),
  ("Where can I get a spa treatment in Sanur?", "THE FACES Sanur is at Jl. Danau Buyan No. 34a, open every day from 10:00 to 20:00, with face massage, head spa, foam rituals and couples treatments."),
 ],
 html=f"""<p>Sanur is the Bali that many people dream of before they arrive: palm trees over a calm sea, a long path along the beach, sunrise every morning and a relaxed, friendly pace. It is less crowded than Seminyak or Canggu and perfect for families, couples and anyone who wants to rest. Here is our slow guide to the best things to do in Sanur, written by the team of THE FACES Sanur.</p>

<h2>1. Watch the sunrise on the beach</h2>
<p>Sanur faces east, so the sunrise over the sea is the main event of the day. Be on the beach before 6:00 on clear mornings, with a coffee, and watch the fishing boats and Mount Agung on very clear days.</p>

<h2>2. Walk or cycle the beach path</h2>
<p>A long paved path runs along the seafront, past hotels, warungs, temples and small beaches. Walk it in the early morning, or rent a bicycle and ride from end to end. It is the best way to discover Sanur's different beaches.</p>

<h2>3. Swim in calm water</h2>
<p>A reef protects much of Sanur's coast, so the water is usually calm and shallow at high tide: ideal for children and for a relaxed swim. Check the tide, because at low tide the water can be very shallow.</p>

<h2>4. Take a day trip to Nusa Lembongan or Nusa Penida</h2>
<p>Fast boats to the Nusa islands leave from Sanur. Spend a day snorkelling with manta rays, visiting the famous viewpoints of Nusa Penida or relaxing on the white beaches of Lembongan. Book with a reputable operator and check the sea conditions.</p>

<h2>5. Try snorkelling, paddleboard or kitesurf</h2>
<p>The calm lagoon is great for stand-up paddle and beginner snorkelling, and some seasons bring good wind for kitesurfing on the southern beaches.</p>

<h2>6. Eat at the night market and local warungs</h2>
<p>In the evening, look for the local night market and the small warungs where Balinese families eat: satay, nasi campur, grilled fish and fresh juices at local prices.</p>

<h2>7. Discover art and history</h2>
<p>Sanur has a long artistic history. Visit the museum dedicated to the Belgian painter Le Mayeur, who lived and painted by the beach, and look for the small temples hidden along the path.</p>

<h2>8. Spend an afternoon at the spa</h2>
<p>After a morning of sea and sun, the afternoon is perfect for a spa. At <a href="/sanur/">THE FACES Sanur</a>, on Jl. Danau Buyan, a few minutes from the beach, guests choose:</p>
<ul>
<li><strong>Myofascial facial massage</strong>, 90 min, IDR 900,000</li>
<li><strong>Hydrolift</strong>, 60 min, IDR 850,000, ideal for skin tired by sun and sea</li>
<li><strong>Airkiss Detox Ritual</strong>, 60 min, IDR 1,300,000</li>
<li><strong>Foamy Dream Ritual</strong>, 120 min, IDR 2,300,000</li>
<li><strong>Reflexology</strong>, 30 / 60 / 90 min, after the beach walk</li>
<li><strong>Sacred Honeymoon ritual</strong>, 200 min, IDR 3,800,000, for couples</li>
</ul>
<p>Read our complete <a href="/spa-in-sanur-guide/">guide to the spa in Sanur</a>.</p>

<h2>9. Use Sanur as your last stop before the airport</h2>
<p>Sanur is close to the airport, so it is the perfect place for the last night of your trip. On departure day, book our Before Flight Ritual (IDR 2,200,000): head spa, body and face care so that you board relaxed.</p>

<h2>A perfect day in Sanur</h2>
<ol>
<li>Sunrise on the beach and breakfast by the sea.</li>
<li>Bike ride along the beach path.</li>
<li>Swim at high tide and lunch at a warung.</li>
<li>Spa afternoon at THE FACES Sanur.</li>
<li>Sunset drinks and dinner at the night market.</li>
</ol>

<h2>When to visit Sanur</h2>
<p>The dry season, roughly April to October, brings sunny days and calm evenings. The rainy season, roughly November to March, is greener and quieter, with short tropical showers: perfect weather for a spa afternoon.</p>

<h2>Book your spa in Sanur</h2>
<p>THE FACES Sanur, Jl. Danau Buyan No. 34a, Sanur, Denpasar Selatan, Bali 80227. Open every day, 10:00–20:00. You can {book("sanur")} or write to us on <a href="{WA_S}" target="_blank" rel="noopener">WhatsApp</a>.</p>
""" + related(R_SANUR, R_COUPLE, R_LYMPH, R_FACIAL)),

dict(
 slug="shirodhara-bali-ayurveda", catkey="head", cat="Head spa · 7 min read", img="g10-proc-s.webp",
 title="Shirodhara in Bali: The Ayurvedic Oil Ritual for Deep Calm",
 seo_title="Shirodhara Bali: Ayurvedic Oil Ritual, Benefits & Price | THE FACES",
 metadesc="Shirodhara in Bali: the Ayurvedic ritual of warm oil on the forehead for stress, sleep and an overloaded mind. What happens, benefits and the Shirodhara Hair Spa.",
 excerpt="A thin stream of warm oil on the forehead, and the mind goes quiet. What Shirodhara is, what it feels like and how we combine it with a hair spa.",
 faq=[
  ("What is Shirodhara?", "Shirodhara is an Ayurvedic treatment in which a thin, continuous stream of warm oil flows over the forehead. It is known for its deeply calming effect on the mind."),
  ("What are the benefits of Shirodhara?", "Guests describe deep relaxation, a quiet mind and better sleep. In Ayurveda it is used to calm stress and an overactive mind. It is a well-being treatment, not a medical one."),
  ("How much is Shirodhara at THE FACES?", "The Shirodhara Hair Spa lasts 120 minutes and costs IDR 1,650,000."),
  ("Will my hair be oily after Shirodhara?", "The oil is part of the treatment. We wash the hair at the end, but it is best to keep the hair simple for the rest of the day and wash it again the next day."),
 ],
 html=f"""<p>Some treatments relax the body. Shirodhara quiets the mind. A thin, warm stream of oil flows slowly over the forehead, and within minutes most guests feel their thoughts slow down. It is one of the oldest rituals of Ayurveda and one of the most memorable treatments you can experience in Bali.</p>

<h2>What is Shirodhara?</h2>
<p>The name comes from Sanskrit: <em>shiro</em>, head, and <em>dhara</em>, flow. The guest lies on their back while warm oil is poured in a continuous stream onto the forehead, the point that Ayurveda calls the third eye. The stream moves gently from side to side. The sensation is warm, rhythmic and hypnotic.</p>

<h2>Why it feels so calming</h2>
<p>The steady warmth and rhythm give the mind one simple thing to follow, which is why many guests drift into a state between waking and sleep. In Ayurveda, Shirodhara is used to calm an overactive mind and to support sleep. Modern guests often describe it as the deepest relaxation they have ever felt.</p>

<h2>Who Shirodhara is for</h2>
<ul>
<li>People who arrive in Bali exhausted and cannot switch off.</li>
<li>Travellers with jet lag and disturbed sleep.</li>
<li>Anyone with a busy mind who struggles to meditate.</li>
<li>Guests looking for a unique, memorable ritual.</li>
</ul>

<h2>The Shirodhara Hair Spa at THE FACES · 120 min · IDR 1,650,000</h2>
<p>We combine the classic Shirodhara with a full hair spa, so that the ritual cares for both the mind and the hair:</p>
<ol>
<li><strong>Welcome</strong>, tea and a short conversation about your needs.</li>
<li><strong>Head, neck and shoulder massage</strong> to prepare the body.</li>
<li><strong>Shirodhara:</strong> the warm oil stream on the forehead.</li>
<li><strong>Hair spa:</strong> cleansing, nourishing care and warm water therapy for the scalp.</li>
<li><strong>Rest</strong> before you leave.</li>
</ol>

<h2>Other Ayurvedic and head treatments</h2>
<ul>
<li><strong>Ayurvedic head massage</strong>, 60 min, IDR 750,000: the short version, with warm oil.</li>
<li><strong>Water spa therapy with detox hair spa</strong>, 90 min, IDR 1,100,000.</li>
<li><strong>Hair spa &amp; water detox + face massage</strong>, 120 min, IDR 1,500,000.</li>
</ul>
<p>Compare them in our <a href="/head-spa-bali-guide/">head spa guide</a>.</p>

<h2>Before and after Shirodhara</h2>
<ul>
<li>Plan nothing demanding afterwards: the calm lasts for hours.</li>
<li>Do not drive a scooter immediately after; take a car or rest first.</li>
<li>Keep your hair simple for the rest of the day.</li>
<li>Drink warm water or tea and go to bed early: the night after is often the best sleep of the trip.</li>
<li>Tell us if you are pregnant, have a scalp condition, a cold or high blood pressure.</li>
</ul>

<h2>Book your Shirodhara</h2>
<p>You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
""" + related(R_HEAD, R_MASS, R_UBUD, R_SANUR)),
]
