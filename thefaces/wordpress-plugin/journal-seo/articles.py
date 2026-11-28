from extra import EXTRA
# Five long SEO articles (English) for the THE FACES Journal on thefacesbali.com.
# Prices and durations from the Altegio menu (thefaces/src/menu.py, 14 Nov 2026).
UB = "https://n831884.alteg.io/company/780725/personal/select-services?o=m-1"
SA = "https://n811764.alteg.io/company/762669/personal/select-services?o=m-1"
WA_U = "https://wa.me/6282266999965"
WA_S = "https://wa.me/6281337709190"

def book(where="both"):
    u = '<a href="%s" target="_blank" rel="noopener">book online in Ubud</a>' % UB
    s = '<a href="%s" target="_blank" rel="noopener">book online in Sanur</a>' % SA
    if where == "ubud":
        return u
    if where == "sanur":
        return s
    return u + " or " + s

ARTICLES = [
dict(
 slug="best-spa-in-ubud-guide",
 catkey="rituals", cat="Rituals · 7 min read", img="g06-interior.webp",
 title="Best Spa in Ubud: How to Choose Your Treatment (2026 Guide)",
 seo_title="Best Spa in Ubud 2026: Treatments, Prices & How to Choose | THE FACES",
 metadesc="Looking for the best spa in Ubud? Face massage, head spa, Five Elements rituals and couples spa at THE FACES Ubud, open daily 10:00–22:00. Prices and tips.",
 excerpt="How to choose a spa in Ubud, what each treatment really does, what it costs and how to plan your visit around the rice fields and the jungle.",
 faq=[
  ("What is the best spa treatment in Ubud for a first visit?", "For a first visit most guests choose a full body massage (60 or 90 minutes) or a Five Elements ritual. If you want a visible result on the face, choose the myofascial facial massage."),
  ("How much does a spa in Ubud cost?", "At THE FACES Ubud a 60-minute full body massage is IDR 650,000, face massages start at IDR 750,000 and the three-hour Five Elements rituals are IDR 1,800,000."),
  ("What are the opening hours of THE FACES Ubud?", "THE FACES Ubud is open every day from 10:00 to 22:00, so you can book a treatment after a day of sightseeing."),
  ("Do I need to book in advance?", "Yes, we recommend booking one or two days ahead, especially for evenings and for couples rituals. You can book online or on WhatsApp."),
 ],
 html=f"""<p>Ubud is the wellness heart of Bali. Between the rice terraces, the yoga shalas and the jungle there are hundreds of spas, from five-dollar roadside massages to resort spas with a view. Choosing one is harder than it looks. This guide explains what really makes a good spa in Ubud, which treatments are worth it, what they cost and how to plan your visit so that you leave lighter, not more tired.</p>

<h2>What makes a spa in Ubud worth your time</h2>
<p>A good spa is not about marble or a big pool. It is about three things you can check before you book:</p>
<ul>
<li><strong>Trained therapists who specialise.</strong> A face massage and a body massage are different crafts. Ask who will treat you and how long they have worked with that technique.</li>
<li><strong>A clear menu with real durations and prices.</strong> If the menu hides the price or the length of the treatment, you will be surprised at the end.</li>
<li><strong>Time around the treatment.</strong> Tea, a quiet changing room and a few minutes of rest after the massage make the difference between a service and a ritual.</li>
</ul>
<p>At <a href="/ubud/">THE FACES Ubud</a>, in Kedewatan, close to Sanggingan, every treatment comes with that time. Anna and Evgenii Dubinin opened their first salon in Bali in 2013, and the team in Ubud follows the same method: specialised therapists, honest prices and no rush.</p>

<h2>The treatments guests in Ubud choose most</h2>

<h3>1. Full body massage</h3>
<p>The classic for after a day of walking the Campuhan Ridge or the Tegallalang terraces. Our therapists combine Balinese pressure with long, calm strokes.</p>
<ul>
<li>Full body massage, 60 min: IDR 650,000</li>
<li>Full body massage, 90 min: IDR 900,000</li>
<li>Full body massage, 120 min: IDR 950,000</li>
<li>Fire Massage, 90 min: IDR 1,100,000, with warmth to release deep tension</li>
</ul>
<p>Read more on the <a href="/body-massage/">body massage page</a>.</p>

<h3>2. Face massage: the reason many guests find us</h3>
<p>THE FACES started as a face studio, and face massage is still our signature. It is not a facial with creams: the therapist works with the muscles and the fascia of the face, the neck and the upper back.</p>
<ul>
<li>Myofascial facial massage, 90 min: IDR 900,000, the most visible lift after one session</li>
<li>Sculptural face massage, 90 min: IDR 850,000, a slower, holistic approach</li>
<li>Buccal facial massage, 60 min: IDR 750,000, work from inside the cheeks for the jaw and contour</li>
<li>Gua sha massage, 60 min: IDR 750,000</li>
</ul>
<p>Not sure which one? Our guide <a href="/face-massage/">to face massage</a> compares them in detail.</p>

<h3>3. Head spa</h3>
<p>The treatment everyone is talking about in Bali. Warm water, scalp detox and a long head massage: many guests fall asleep in the first ten minutes. Try the Water spa therapy with detox hair spa (90 min, IDR 1,100,000) or the Shirodhara Hair Spa, with a warm oil stream on the forehead (120 min, IDR 1,650,000). In Ubud there is also Let Your Hair Shine (120 min, IDR 1,500,000) and a Hair spa for kids (60 min, IDR 750,000). See the <a href="/head-spa/">head spa page</a>.</p>

<h3>4. Five Elements rituals</h3>
<p>Our three-hour programmes are built around Air, Fire, Water, Earth and Love. Each one combines several techniques, face, body and head, into one journey (180 min, IDR 1,800,000). They are the best choice if you have one afternoon and want the full THE FACES experience. Discover them on the <a href="/five-elements/">Five Elements page</a>.</p>

<h3>5. Treatments for men</h3>
<p>Ubud has two programmes designed for men: Power Reset (130 min, IDR 1,400,000) and Stress Free (120 min, IDR 2,100,000).</p>

<h2>How to plan your spa day in Ubud</h2>
<ol>
<li><strong>Book the afternoon or the evening.</strong> The morning is for the rice fields and the temples; the spa is the perfect end of the day. THE FACES Ubud is open until 22:00.</li>
<li><strong>Arrive ten minutes early.</strong> You will have time for tea and to tell the therapist what you need.</li>
<li><strong>Do not eat a heavy meal just before.</strong> A light lunch two hours before is ideal.</li>
<li><strong>Keep an hour free after the treatment.</strong> Especially after a head spa or a ritual, give yourself time before you jump back on a scooter.</li>
<li><strong>Tell us about pregnancy, injuries or allergies.</strong> The therapist will adapt the treatment or suggest another one.</li>
</ol>

<h2>Ubud or Sanur?</h2>
<p>We have two salons. <a href="/ubud/">Ubud</a> is surrounded by green and is open until 22:00, perfect if you stay in the centre or in Sayan and Kedewatan. <a href="/sanur/">Sanur</a> is by the sea, quieter, and has a few treatments you will only find there, such as Hydrolift and the Sacred Honeymoon ritual. The full list is on our <a href="/menu/">menu</a>.</p>

<h2>Book your treatment</h2>
<p>You can {book("ubud")}, or write to the Ubud team on <a href="{WA_U}" target="_blank" rel="noopener">WhatsApp</a> and we will help you choose. Address: Jl. Raya Lungsiakan, Kedewatan, Ubud, Bali 80571. Open every day, 10:00–22:00.</p>
"""),

dict(
 slug="head-spa-bali-guide",
 catkey="head", cat="Head spa · 7 min read", img="g10-proc-s.webp",
 title="Head Spa in Bali: Hair Spa, Shirodhara and Scalp Detox Explained",
 seo_title="Head Spa Bali: Hair Spa, Shirodhara & Scalp Detox Prices | THE FACES",
 metadesc="What is a head spa and which one to choose in Bali? Water spa with detox hair spa, Shirodhara and Ayurvedic head massage in Ubud and Sanur, with prices.",
 excerpt="Everything about the head spa trend in Bali: what happens during a session, the benefits for the scalp and the nervous system, and which treatment to book.",
 faq=[
  ("What is a head spa?", "A head spa is a treatment for the scalp and the hair that combines cleansing, warm water, massage of the head, neck and shoulders and nourishing care. It relaxes deeply and leaves the hair soft and light."),
  ("How long does a head spa take?", "At THE FACES a head spa lasts from 60 minutes (Ayurvedic head massage) to 120 minutes (Shirodhara Hair Spa), and up to 180 minutes when combined with a face massage."),
  ("How much is a head spa in Bali?", "At THE FACES prices start at IDR 750,000 for the Ayurvedic head massage. The Water spa therapy with detox hair spa is IDR 1,100,000 and the Shirodhara Hair Spa is IDR 1,650,000."),
  ("Is head spa good for hair loss?", "A head spa improves the condition of the scalp and the circulation and helps you relax, which many people with stressed hair appreciate. It is not a medical treatment: for hair loss, consult a dermatologist."),
 ],
 html=f"""<p>If you have scrolled Instagram or TikTok in Bali this year, you have seen it: a guest lying back, warm water falling over the scalp, foam, steam and a face that slowly relaxes. The head spa has become one of the most wanted treatments on the island. Here is what it really is, what happens during a session and how to choose the right one at THE FACES in Ubud or Sanur.</p>

<h2>What is a head spa?</h2>
<p>A head spa is a ritual for the scalp and the hair. It borrows from Japanese scalp care and from Ayurveda and combines four steps:</p>
<ol>
<li><strong>Diagnosis and cleansing.</strong> The therapist looks at the scalp and gently removes the build-up of sweat, sunscreen, salt water and styling products.</li>
<li><strong>Warm water therapy.</strong> A slow stream of warm water relaxes the scalp and the nervous system.</li>
<li><strong>Massage.</strong> Head, neck and shoulders, where most of us hold our tension.</li>
<li><strong>Nourishing care.</strong> A mask or oil adapted to your hair, then a gentle dry.</li>
</ol>
<p>The result: a light head, soft hair and a deep feeling of calm that many guests compare to a long night of sleep.</p>

<h2>Why a head spa makes sense in Bali</h2>
<p>Sun, humidity, salt water, chlorine and daily sunscreen are hard on the scalp. Many travellers notice dry lengths and an oily or itchy scalp after a few weeks on the island. A head spa resets both. It is also a perfect treatment for jet lag and for the last day before a long flight.</p>

<h2>Head spa treatments at THE FACES</h2>

<h3>Ayurvedic head massage · 60 min · IDR 750,000</h3>
<p>The short version: a deep massage of the head, neck and shoulders with warm oil, inspired by Indian tradition. Ideal if you have an hour and want to switch off.</p>

<h3>Water spa therapy with detox hair spa · 90 min · IDR 1,100,000</h3>
<p>Our most booked head spa. Detox cleansing, a long warm water ritual and a massage that reaches the neck and shoulders. Perfect for a first head spa.</p>

<h3>Shirodhara Hair Spa · 120 min · IDR 1,650,000</h3>
<p>The deepest of all. A thin, continuous stream of warm oil flows over the forehead, the "third eye" in Ayurveda, while the hair receives a full spa. It is the treatment we recommend for stress, poor sleep and an overloaded mind.</p>

<h3>Let Your Hair Shine · 120 min · IDR 1,500,000 · Ubud</h3>
<p>Focused on the beauty of the hair: nourishing care for lengths damaged by sun and sea, with a relaxing head massage.</p>

<h3>Hair spa for kids · 60 min · IDR 750,000 · Ubud</h3>
<p>A gentle, playful version for children, so that the whole family can enjoy the spa.</p>

<h2>Head spa combined with face massage</h2>
<p>The combination of head spa and face massage is our favourite: the scalp and the face are connected by the same fascia, so working on both doubles the effect.</p>
<ul>
<li>Hair spa &amp; water detox + face massage, 120 min: IDR 1,500,000</li>
<li>3 in 1 (head, face massage, hair spa): IDR 1,900,000</li>
<li>Detox hair spa + myofascial facial massage, 150 min: IDR 1,850,000 (Sanur)</li>
<li>Detox hair spa + sculptural face massage, 180 min: IDR 1,850,000 (Sanur)</li>
<li>Water spa therapy with detox hair spa + Airkiss Detox Ritual, 120 min: IDR 1,900,000</li>
</ul>

<h2>How to choose your head spa</h2>
<ul>
<li><strong>First time, one afternoon:</strong> Water spa therapy with detox hair spa.</li>
<li><strong>Stress, insomnia, jet lag:</strong> Shirodhara Hair Spa.</li>
<li><strong>Short on time:</strong> Ayurvedic head massage.</li>
<li><strong>You want to look rested for an event or photos:</strong> a head spa + face massage combination.</li>
<li><strong>Before a long flight:</strong> our Before Flight Ritual (IDR 2,200,000), which includes care for the head, face and legs.</li>
</ul>

<h2>Tips before and after your head spa</h2>
<ul>
<li>Come with your hair as it is: no need to wash it before.</li>
<li>Plan no swimming pool or sea for the rest of the day, so the care can work.</li>
<li>Drink water after the treatment and keep the evening calm.</li>
<li>Tell the therapist if you have a sensitive scalp or a recent colour.</li>
</ul>

<h2>Book your head spa</h2>
<p>All the details are on the <a href="/head-spa/">head spa page</a> and in the <a href="/menu/">full menu</a>. You can {book()}, or write to us on WhatsApp: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
"""),

dict(
 slug="face-massage-bali-guide",
 catkey="face", cat="Face · 8 min read", img="g01-face.webp",
 title="Face Massage in Bali: Myofascial, Sculptural, Buccal or Gua Sha?",
 seo_title="Face Massage Bali: Myofascial, Buccal, Sculptural & Gua Sha | THE FACES",
 metadesc="Which face massage to choose in Bali? Myofascial, sculptural, buccal and gua sha compared: what each one does, results, duration and prices at THE FACES.",
 excerpt="A complete comparison of the face massages at THE FACES: how they work, who they are for, how many sessions you need and what they cost.",
 faq=[
  ("Which face massage gives the most visible lift?", "The myofascial facial massage gives the most visible lift after one session, because it releases the fascia of the face, the neck and the upper back."),
  ("How many face massage sessions do I need?", "One session already shows a fresher, lifted face. For a lasting effect we recommend a course of five or six sessions, every three days."),
  ("How much is a face massage at THE FACES?", "Face massages cost IDR 750,000 (buccal or gua sha, 60 min), IDR 850,000 (sculptural, 90 min) and IDR 900,000 (myofascial or signature, 90 min)."),
  ("Is face massage suitable before a wedding or photos?", "Yes. Book it one or two days before: the face looks rested and the contour more defined. Avoid strong techniques for the first time on the day itself."),
 ],
 html=f"""<p>Face massage is where THE FACES began, and it is still the treatment our guests travel across Bali for. It is not a classic facial with creams and steam: it is a manual technique that works with the muscles, the fascia and the lymph of the face. The result is visible: a lifted contour, a relaxed jaw, brighter skin and a face that looks rested. Here is how to choose between our techniques.</p>

<h2>Why face massage works</h2>
<p>We use more than forty muscles of the face every day: to speak, chew, frown at the screen and squint in the sun. Over time they become tense and the fascia, the thin tissue that wraps them, loses its elasticity. The face looks tired and the contour drops. A professional face massage releases that tension, improves circulation and lymphatic drainage and gives the face its natural shape back.</p>

<h2>The four main techniques</h2>

<h3>Myofascial facial massage · 90 min · IDR 900,000</h3>
<p>The therapist works deep in the fascia of the face and continues to the neck, the décolleté and the upper back, where many face problems start. Tension in the jaw and the forehead melts, the oval looks lifted and the skin brighter.</p>
<p><strong>For whom:</strong> you clench your teeth, work at a screen, want a visible lift after one visit.</p>

<h3>Sculptural face massage · 90 min · IDR 850,000</h3>
<p>It combines French osteopathic methods with natural rejuvenation techniques and works with the whole body, not only the face. It is slower and more holistic, and the contour changes gradually over a course.</p>
<p><strong>For whom:</strong> long-term well-ageing, guests who want a deep, calm treatment.</p>

<h3>Buccal facial massage · 60 min · IDR 750,000</h3>
<p>Part of the massage is done from inside the mouth, with gloves, to reach the deep muscles of the cheeks and the jaw that cannot be reached from outside. It is intense and very effective for the lower face.</p>
<p><strong>For whom:</strong> jaw tension, asymmetry, a softer lower contour.</p>

<h3>Gua sha massage · 60 min · IDR 750,000</h3>
<p>A traditional Chinese technique with a smooth stone tool. It drains, de-puffs and leaves the skin glowing.</p>
<p><strong>For whom:</strong> puffiness, morning swelling, a quick glow before an evening out.</p>

<h2>Our signature face massages</h2>
<ul>
<li>Signature massage «The FACES», 90 min: IDR 900,000, the best of our techniques in one session</li>
<li>Signature massage «Element of Love», 90 min: IDR 900,000</li>
<li>Signature massage «Author», 90 min: IDR 850,000</li>
<li>Signature technique: Air Kiss Sculpt &amp; Detox, 120 min: IDR 1,800,000</li>
</ul>
<p>In Sanur you can also book Hydrolift (60 min, IDR 850,000), Hydrolift + face massage (90 min, IDR 1,100,000) and 4 hands, a face massage with foot reflexology at the same time (IDR 950,000).</p>

<h2>Quick comparison</h2>
<table>
<thead><tr><th>Technique</th><th>Duration</th><th>Price (IDR)</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>Myofascial</td><td>90 min</td><td>900,000</td><td>Visible lift, jaw tension</td></tr>
<tr><td>Sculptural</td><td>90 min</td><td>850,000</td><td>Long-term contour</td></tr>
<tr><td>Buccal</td><td>60 min</td><td>750,000</td><td>Cheeks and jaw</td></tr>
<tr><td>Gua sha</td><td>60 min</td><td>750,000</td><td>Puffiness, glow</td></tr>
</tbody>
</table>

<h2>How many sessions?</h2>
<p>After one session the face already looks fresher and lifted. For a result that lasts, we recommend a course of five or six sessions, every three days, which fits perfectly into a two-week holiday in Bali.</p>

<h2>Combine it with skin care or head spa</h2>
<p>Face massage works even better on clean, hydrated skin. Combine it with a cleansing or Deep skin hydration (80 min, IDR 1,000,000) from our <a href="/skin-care/">skin care menu</a>, or with a head spa: see our <a href="/head-spa/">head spa guide</a>.</p>

<h2>Before and after</h2>
<ul>
<li>Come without make-up if you can, or we will remove it.</li>
<li>Avoid strong sun for the rest of the day.</li>
<li>Drink water: massage stimulates lymphatic drainage.</li>
<li>Tell us about recent injections, fillers or skin procedures: the therapist will adapt the technique.</li>
</ul>

<h2>Book your face massage</h2>
<p>More details on the <a href="/face-massage/">face massage page</a>. You can {book()}, or ask us on WhatsApp which technique suits you: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
"""),

dict(
 slug="spa-in-sanur-guide",
 catkey="rituals", cat="Rituals · 7 min read", img="g07-interior-s.webp",
 title="Spa in Sanur: Treatments, Prices and Tips for a Perfect Spa Day",
 seo_title="Spa in Sanur Bali: Treatments, Prices & Spa Day Tips | THE FACES Sanur",
 metadesc="Planning a spa in Sanur? THE FACES Sanur on Jl. Danau Buyan: face massage, Hydrolift, head spa, Airkiss and honeymoon rituals. Open 10:00–20:00. Prices inside.",
 excerpt="A complete guide to THE FACES Sanur: the treatments you can only find here, prices, how to combine them and how to plan a slow spa day by the sea.",
 faq=[
  ("Where is THE FACES Sanur?", "THE FACES Sanur is at Jl. Danau Buyan No. 34a, Sanur, Denpasar Selatan, Bali 80227, a few minutes from the beach."),
  ("What are the opening hours in Sanur?", "THE FACES Sanur is open every day from 10:00 to 20:00."),
  ("Which treatments are only available in Sanur?", "Hydrolift, Hydrolift + face massage, 4 hands (face massage + foot reflexology), the Aqua Glow Ritual, the Sacred Honeymoon ritual and the detox hair spa combined with a myofascial or sculptural face massage."),
  ("Is Sanur a good place for a spa day?", "Yes. Sanur is calm, close to the airport and to the sea, so it is ideal for a slow spa day or for the last day before your flight."),
 ],
 html=f"""<p>Sanur is the calm side of Bali: a long beach path, sunrise over the sea, families and slow mornings. It is also a wonderful place for a spa day, especially at the start or at the end of a trip, because the airport is close. Our salon <a href="/sanur/">THE FACES Sanur</a> is on Jl. Danau Buyan, a few minutes from the beach. Here is everything you need to plan your visit.</p>

<h2>Why choose a spa in Sanur</h2>
<ul>
<li><strong>Calm.</strong> Less traffic and noise than in Seminyak or Canggu.</li>
<li><strong>Close to the airport.</strong> Perfect for a treatment on arrival or before a night flight.</li>
<li><strong>Sea and spa in one day.</strong> Swim in the morning, spa in the afternoon, dinner by the beach.</li>
</ul>

<h2>Treatments you will only find in Sanur</h2>

<h3>Hydrolift · 60 min · IDR 850,000</h3>
<p>Intensive hydration and a lifting effect for skin tired by sun and air conditioning. Combine it with a face massage: Hydrolift + face massage, 90 min, IDR 1,100,000.</p>

<h3>4 hands · IDR 950,000</h3>
<p>Two therapists at the same time: a face massage and a foot reflexology. One of the most relaxing experiences on our menu.</p>

<h3>Aqua Glow Ritual · 100 min · IDR 800,000</h3>
<p>A body ritual focused on hydration and glow, perfect after days of sun and sea.</p>

<h3>Sacred Honeymoon ritual · 200 min · IDR 3,800,000</h3>
<p>Our longest ritual for two, created for honeymoons and anniversaries. Read our <a href="/couples-spa/">couples spa guide</a>.</p>

<h3>Head spa and face massage in one session</h3>
<ul>
<li>Detox hair spa + myofascial facial massage, 150 min: IDR 1,850,000</li>
<li>Detox hair spa + sculptural face massage, 180 min: IDR 1,850,000</li>
</ul>

<h2>The favourites of our Sanur guests</h2>
<ul>
<li><strong>Airkiss Detox Ritual</strong>, 60 min: IDR 1,300,000 in Sanur. Our airy foam ritual, light and deeply relaxing.</li>
<li><strong>Foamy Dream Ritual</strong>, 120 min: IDR 2,300,000. A cloud of foam for the whole body.</li>
<li><strong>Full body massage</strong>, 90 min: IDR 850,000 in Sanur.</li>
<li><strong>Reflexology foot massage</strong>, 30 / 60 / 90 min: IDR 300,000 / 500,000 / 600,000. Ideal after walking the beach path.</li>
<li><strong>Myofascial facial massage</strong>, 90 min: IDR 900,000. Our signature face massage.</li>
</ul>

<h2>A perfect slow spa day in Sanur</h2>
<ol>
<li><strong>Sunrise on the beach</strong>, around 6:00, then breakfast.</li>
<li><strong>A swim and a walk</strong> on the beach path in the morning.</li>
<li><strong>Light lunch</strong> at least two hours before your treatment.</li>
<li><strong>Spa in the afternoon</strong>: a head spa + face massage combination or a Foamy Dream Ritual.</li>
<li><strong>Dinner by the sea</strong> and an early night.</li>
</ol>

<h2>The Before Flight Ritual</h2>
<p>Flying home tonight? Our Before Flight Ritual (IDR 2,200,000, about three hours in Sanur) prepares the body for a long flight: care for the head, face and legs, so that you board relaxed and land less swollen. Book it for the afternoon of your departure day, and keep your luggage in the car.</p>

<h2>Prices at a glance</h2>
<table>
<thead><tr><th>Treatment</th><th>Duration</th><th>Price (IDR)</th></tr></thead>
<tbody>
<tr><td>Full body massage</td><td>90 min</td><td>850,000</td></tr>
<tr><td>Myofascial facial massage</td><td>90 min</td><td>900,000</td></tr>
<tr><td>Hydrolift</td><td>60 min</td><td>850,000</td></tr>
<tr><td>Airkiss Detox Ritual</td><td>60 min</td><td>1,300,000</td></tr>
<tr><td>Foamy Dream Ritual</td><td>120 min</td><td>2,300,000</td></tr>
<tr><td>Before Flight Ritual</td><td>about 180 min</td><td>2,200,000</td></tr>
</tbody>
</table>
<p>The full list is in our <a href="/menu/">menu</a>.</p>

<h2>Book in Sanur</h2>
<p>Address: Jl. Danau Buyan No. 34a, Sanur, Denpasar Selatan, Bali 80227. Open every day, 10:00–20:00. You can {book("sanur")} or write to the Sanur team on <a href="{WA_S}" target="_blank" rel="noopener">WhatsApp</a>.</p>
"""),

dict(
 slug="couples-spa-bali-honeymoon",
 catkey="rituals", cat="Rituals · 7 min read", img="g08-interior.webp",
 title="Couples Spa in Bali: Honeymoon and Romantic Rituals for Two",
 seo_title="Couples Spa Bali: Honeymoon & Romantic Spa Rituals | THE FACES",
 metadesc="Best couples spa in Bali for a honeymoon or anniversary: Element of Love for a couple, Sacred Eternal Love and Sacred Honeymoon rituals in Ubud and Sanur.",
 excerpt="How to choose a couples spa in Bali, what happens during our rituals for two, prices and ideas to make your honeymoon or anniversary unforgettable.",
 faq=[
  ("What is the best couples spa treatment in Bali?", "At THE FACES we offer three rituals for two: Element of Love for a couple (180 min), the Sacred Eternal Love ritual (175 min) and the Sacred Honeymoon ritual (200 min, Sanur)."),
  ("How much is a couples spa in Bali?", "Our couples rituals cost IDR 3,200,000 (Element of Love for a couple), IDR 3,300,000 (Sacred Eternal Love) and IDR 3,800,000 (Sacred Honeymoon) for two people."),
  ("Can we have treatments side by side?", "Yes, our couples rituals are designed for two people at the same time in the same room."),
  ("Should we book a couples spa in advance?", "Yes. Couples rituals need two therapists at the same time, so we recommend booking two or three days ahead, especially for weekends and evenings."),
 ],
 html=f"""<p>Bali is one of the most romantic places on Earth, and a spa ritual for two is one of the moments couples remember most from their trip. Whether it is your honeymoon, an anniversary or simply time together away from the screens, here is how to choose a couples spa in Bali and what to expect from our rituals at THE FACES in Ubud and Sanur.</p>

<h2>What makes a good couples spa</h2>
<ul>
<li><strong>One room, two therapists, the same rhythm.</strong> You start and finish together, so the experience is shared, not parallel.</li>
<li><strong>Enough time.</strong> A real ritual for two lasts at least two and a half hours, with a welcome, the treatment and time to rest together.</li>
<li><strong>A story.</strong> The best rituals are not just two massages: they have a beginning, a heart and a closing moment.</li>
</ul>

<h2>Our rituals for two</h2>

<h3>Element of Love for a couple · 180 min · IDR 3,200,000</h3>
<p>Inspired by the fifth of our <a href="/five-elements/">Five Elements</a>, Love. A three-hour journey that combines body, face and head care, side by side. It is our most chosen ritual for anniversaries.</p>

<h3>Sacred Eternal Love ritual · 175 min · IDR 3,300,000</h3>
<p>A ritual built around connection and presence, with warm oils, slow massage and a closing moment for the two of you. Perfect for a proposal trip or a vow renewal.</p>

<h3>Sacred Honeymoon ritual · 200 min · IDR 3,800,000 · Sanur</h3>
<p>Our longest ritual, created for honeymooners. More than three hours of care for two, in our calm salon by the sea in <a href="/sanur/">Sanur</a>.</p>

<h2>More ideas for two</h2>
<ul>
<li><strong>Book the same treatment at the same time:</strong> for example two Airkiss Detox Rituals (IDR 1,200,000 each in Ubud, IDR 1,300,000 in Sanur) or two Foamy Dream Rituals (IDR 2,300,000 each).</li>
<li><strong>One head spa, one face massage:</strong> if you have different needs, book side by side treatments of the same length.</li>
<li><strong>Five Elements for two:</strong> each partner chooses their element (180 min, IDR 1,800,000 per person).</li>
</ul>

<h2>Ubud or Sanur for a couples spa?</h2>
<p><a href="/ubud/">Ubud</a> is the jungle and the rice fields, and our salon is open until 22:00, ideal for an evening ritual after a day of exploring. <a href="/sanur/">Sanur</a> is the sea and calm, and the only place to book the Sacred Honeymoon ritual. Many couples split their stay: a few nights in Ubud, a few by the sea.</p>

<h2>How to make it unforgettable</h2>
<ol>
<li><strong>Book in advance</strong>: two or three days, as two therapists are needed at the same time.</li>
<li><strong>Tell us the occasion</strong> when you book: honeymoon, anniversary, birthday. We love preparing small surprises.</li>
<li><strong>Plan nothing after</strong>: no scooter rides or busy dinners. Go for a quiet dinner and an early night.</li>
<li><strong>Leave the phones</strong> in the changing room. The ritual starts when the screens go off.</li>
</ol>

<h2>Prices for two at a glance</h2>
<table>
<thead><tr><th>Ritual</th><th>Duration</th><th>Price for two (IDR)</th><th>Where</th></tr></thead>
<tbody>
<tr><td>Element of Love for a couple</td><td>180 min</td><td>3,200,000</td><td>Ubud &amp; Sanur</td></tr>
<tr><td>Sacred Eternal Love ritual</td><td>175 min</td><td>3,300,000</td><td>Ubud &amp; Sanur</td></tr>
<tr><td>Sacred Honeymoon ritual</td><td>200 min</td><td>3,800,000</td><td>Sanur</td></tr>
</tbody>
</table>

<h2>Book your couples ritual</h2>
<p>All the details are on the <a href="/couples-spa/">couples spa page</a>. You can {book()}, or write to us on WhatsApp and tell us the occasion: <a href="{WA_U}" target="_blank" rel="noopener">Ubud</a>, <a href="{WA_S}" target="_blank" rel="noopener">Sanur</a>.</p>
"""),
]

for _a in ARTICLES:
    _i = _a["html"].rfind("<h2>")
    _a["html"] = _a["html"][:_i] + EXTRA[_a["slug"]].strip() + "\n\n" + _a["html"][_i:]
