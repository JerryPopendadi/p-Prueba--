# THE FACES menu, copied from Altegio (n831884.alteg.io) on 14 Nov 2026: The FACES Ubud (780725) and The FACES Sanur (762669).
# Change prices here, then run: python3 thefaces/src/build.py
# (category, id, name, minutes, price IDR, only_in_salons, differences_by_salon)
# differences_by_salon: {"sanur": (minutes, price)} when Sanur differs from Ubud. minutes 0 = not set in Altegio.
# Treatment names stay in English in every language (as in Altegio).
U, S = ["ubud"], ["sanur"]
MENU = [
 ("face", "myo", "Myofascial facial massage", 90, 900000, None, None),
 ("face", "sculpt", "Sculptural face massage", 90, 850000, None, None),
 ("face", "buccal", "Buccal facial massage", 60, 750000, None, None),
 ("face", "guasha", "Gua sha massage", 60, 750000, None, None),
 ("face", "love-sig", "Signature massage «Element of Love»", 90, 900000, None, None),
 ("face", "faces-sig", "Signature massage «The FACES»", 90, 900000, None, None),
 ("face", "author", "Signature massage «Author»", 90, 850000, None, None),
 ("face", "hydrolift", "Hydrolift", 60, 850000, S, None),
 ("face", "hydro-face", "Hydrolift + face massage", 90, 1100000, S, None),
 ("face", "four-hands", "4 hands (face massage + foot reflexology)", 0, 950000, S, None),
 ("face", "candle", "Candle treatment", 10, 200000, None, None),
 ("air", "airkiss", "Airkiss Detox Ritual", 60, 1200000, None, {"sanur": (60, 1300000)}),
 ("air", "airkiss-sculpt", "Signature technique: Air Kiss Sculpt & Detox", 120, 1800000, None, None),
 ("air", "foamy-back", "Foamy back & leg massage", 60, 1400000, None, None),
 ("air", "foamy-dream", "Foamy Dream Ritual", 120, 2300000, None, None),
 ("head", "water-spa", "Water spa therapy with detox hair spa", 90, 1100000, None, None),
 ("head", "ayur", "Ayurvedic head massage", 60, 750000, None, None),
 ("head", "shiro", "Shirodhara Hair Spa", 120, 1650000, None, None),
 ("head", "shine", "Let Your Hair Shine", 120, 1500000, U, None),
 ("head", "hair-face", "Hair spa & water detox + face massage", 120, 1500000, None, None),
 ("head", "detox-myo", "Detox hair spa + myofascial facial massage", 150, 1850000, S, None),
 ("head", "detox-sculpt", "Detox hair spa + sculptural face massage", 180, 1850000, S, None),
 ("head", "kids", "Hair spa for kids", 60, 750000, U, None),
 ("skin", "atraumatic", "Atraumatic facial cleansing", 110, 1200000, None, None),
 ("skin", "vacuum", "Vacuum facial cleansing", 120, 1200000, None, None),
 ("skin", "ultra", "Ultrasonic facial cleansing", 120, 1200000, None, None),
 ("skin", "combo", "Combination facial cleansing", 150, 1350000, None, None),
 ("skin", "hydra", "Deep skin hydration", 80, 1000000, None, None),
 ("skin", "oxy", "Oxygen pen", 75, 900000, None, None),
 ("skin", "cryo", "Cryomassage", 75, 970000, None, None),
 ("skin", "lymph-glow", "Lymphatic Glow", 90, 1000000, U, None),
 ("prog", "el-air", "Element of Air", 180, 1800000, None, None),
 ("prog", "el-fire", "Element of Fire", 180, 1800000, None, None),
 ("prog", "el-water", "Element of Water", 180, 1800000, None, None),
 ("prog", "el-earth", "Element of Earth", 180, 1800000, None, None),
 ("prog", "el-love", "Element of Love", 180, 1800000, None, None),
 ("pack", "before-flight", "Before Flight Ritual", 150, 2200000, None, {"sanur": (180, 2200000)}),
 ("pack", "water-airkiss", "Water spa therapy with detox hair spa + Airkiss Detox Ritual", 120, 1900000, None, None),
 ("pack", "3in1", "3 in 1 (head, face massage, hair spa)", 180, 1900000, None, {"sanur": (90, 1900000)}),
 ("pack", "beauty-detox", "Beauty and Detox Rituals Package", 180, 2500000, None, None),
 ("men", "power", "Power Reset", 130, 1400000, U, None),
 ("men", "stressfree", "Stress Free", 120, 2100000, U, None),
 ("two", "love-two", "Element of Love for a couple", 180, 3200000, None, None),
 ("two", "eternal", "Sacred Eternal Love ritual", 175, 3300000, None, None),
 ("two", "honeymoon", "Sacred Honeymoon ritual", 200, 3800000, S, None),
 ("body", "body60", "Full body massage · 60 min", 60, 650000, None, None),
 ("body", "body90", "Full body massage · 90 min", 90, 900000, None, {"sanur": (90, 850000)}),
 ("body", "body120", "Full body massage · 120 min", 120, 950000, None, None),
 ("body", "fire", "Fire Massage", 90, 1100000, None, None),
 ("body", "aqua", "Aqua Glow Ritual", 100, 800000, S, None),
 ("body", "refl30", "Reflexology foot massage · 30 min", 30, 300000, None, None),
 ("body", "refl60", "Reflexology foot massage · 60 min", 60, 500000, None, None),
 ("body", "refl90", "Reflexology foot massage · 90 min", 90, 600000, None, None),
 ("body", "leg30", "Lymphatic drainage / relaxing leg massage · 30 min", 30, 300000, None, None),
 ("body", "leg60", "Lymphatic drainage / relaxing leg massage · 60 min", 60, 500000, None, None),
 ("body", "leg90", "Lymphatic drainage / relaxing leg massage · 90 min", 90, 600000, None, None),
]
ALTEGIO = "https://n831884.alteg.io/"

SIGNATURES = [("myo", "tag_face", "g01-face.webp"), ("shiro", "tag_head", "g10-proc-s.webp"),
              ("airkiss", "tag_skin", "g12-proc-s.webp"), ("airkiss-sculpt", "tag_skin", "g11-proc-s.webp"),
              ("sculpt", "tag_face", "g03-face-s.webp"), ("beauty-detox", "tag_package", "g09-proc-s.webp")]

GIFTS = [(1200000, 1500000), (4000000, 5000000), (12750000, 15000000), (25500000, 30000000)]

SALONS = {
 "ubud": {"name": "Ubud", "wa": "6282266999965", "tel": "+62 822 6699 9965", "opens": "10:00", "closes": "22:00", "online": "https://n831884.alteg.io/",
          "addr": "Jl. Sanggingan, Jl. Raya Lungsiakan, Kedewatan, Ubud, Bali 80571",
          "street": "Jl. Raya Lungsiakan, Kedewatan", "locality": "Ubud", "postal": "80571",
          "maps": "https://www.google.com/maps/search/?api=1&query=The+Faces+Spa+Ubud+Jl.+Raya+Lungsiakan",
          "img": "g06-interior.webp", "alt": "sa_ubud_alt"},
 "sanur": {"name": "Sanur", "wa": "6281337709190", "tel": "+62 813 3770 9190", "opens": "10:00", "closes": "20:00", "online": "https://n831884.alteg.io/",
           "addr": "Jl. Danau Buyan No. 34a, Sanur, Denpasar Selatan, Bali 80227",
           "street": "Jl. Danau Buyan No. 34a", "locality": "Sanur, Denpasar", "postal": "80227",
           "maps": "https://www.google.com/maps/search/?api=1&query=The+Faces+Spa+Sanur+Jl.+Danau+Buyan+34a",
           "img": "g07-interior-s.webp", "alt": "sa_sanur_alt"},
}

LINKS = {
 "instagram": "https://www.instagram.com/thefacesubud/",
 "instagram_spa": "https://www.instagram.com/thefacesspaubud/",
 "tiktok": "https://www.tiktok.com/@thefaces.bali",
 "linkedin": "https://www.linkedin.com/company/the-faces",
 "email": "thefacesworld@gmail.com",
 "network": "https://thefacespeace.com",
 "partner_call": "https://thefacespeace.com/#contacto",
 "legal": "https://thefacesspa.com/en/legal/",
}

GALLERY = ["g01-face", "g04-interior", "g09-proc-s", "g02-face-s", "g08-interior", "g12-proc-s", "g06-interior",
           "dsc", "g10-proc-s", "g03-face-s", "g05-interior-s", "g11-proc-s", "g07-interior-s"]
