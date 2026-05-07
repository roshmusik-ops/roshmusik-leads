"""Configuration for roshmusik Music Lead Agent."""

BRAND = {
    "company": "roshmusik",
    "founder": "Roshith R Menon",
    "phone": "+91 94473 36560",
    "email": "rosh.musik@gmail.com",
    "website": "https://www.roshmusik.com",
    "tagline": "Born to Resonate.",
    "artist_bio": (
        "Indie singer-songwriter & composer. Original releases in Malayalam, Tamil, "
        "and English. Latest: 'Neermathalam Kozhinja Sandhya' (Malayalam romantic poem). "
        "Discography includes 'Neeyen Sakhi', 'En Swaasame', 'Oru Kaadhal Kadhai', "
        "'Déjà Vu'. Available for film, ad, album & collaboration work."
    ),
    "past_work": [
        "Neermathalam Kozhinja Sandhya (Malayalam single)",
        "Neeyen Sakhi (Malayalam)",
        "En Swaasame & Oru Kaadhal Kadhai (Tamil)",
        "Déjà Vu (English indie)",
    ],
    "links": {
        "spotify": "https://open.spotify.com/artist/66GvSYuJ8ks3iouoFicDo7",
        "youtube": "https://youtube.com/@Roshmusik",
        "instagram": "https://instagram.com/roshmusikofficial",
        "bandcamp": "https://roshmusik.bandcamp.com",
        "linktree": "https://linktr.ee/roshmusik",
    },
    "services": [
        "Composing & singing original songs for films",
        "Album / EP production",
        "Brand jingles & ad music",
        "Background score for films / shorts / ads",
        "Playback singing (Malayalam, Tamil, English)",
        "Custom songs for events & weddings",
    ],
}

# Music-industry leads: people/places who hire singers, composers, producers
# or run businesses that need original music.
CATEGORIES = [
    # Film & TV production
    "film production house",
    "movie production company",
    "tv serial production",
    "documentary film makers",
    "ad film makers",
    "video production company",
    "post production studio",
    "dubbing studio",
    # Music industry
    "recording studio",
    "music studio",
    "music label",
    "music academy",
    "music school",
    "music director office",
    "audio engineer",
    "live band",
    "wedding band",
    "orchestra group",
    "DJ services",
    # Advertising / brand
    "advertising agency",
    "creative agency",
    "branding agency",
    "digital marketing agency",
    "media production",
    # Events & live
    "event management company",
    "wedding planner",
    "corporate event company",
    "concert organiser",
    # Content creators
    "youtube studio",
    "podcast studio",
    "content creation studio",
    # Performance venues
    "live music venue",
    "auditorium",
    "concert hall",
]

# 5 South Indian states
KERALA_CITIES = [
    "Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alappuzha", "Kottayam",
    "Idukki", "Ernakulam", "Thrissur", "Palakkad", "Malappuram",
    "Kozhikode", "Wayanad", "Kannur", "Kasaragod",
]

TAMILNADU_CITIES = [
    "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem",
    "Tirunelveli", "Tiruppur", "Vellore", "Erode", "Thoothukudi",
    "Dindigul", "Thanjavur", "Ranipet", "Sivaganga", "Karur",
    "Namakkal", "Kanchipuram", "Tiruvannamalai", "Pudukkottai", "Nagapattinam",
    "Cuddalore", "Villupuram", "Krishnagiri", "Dharmapuri", "Theni",
    "Virudhunagar", "Ramanathapuram", "Kanyakumari", "Nilgiris", "Ariyalur",
    "Perambalur", "Tenkasi", "Chengalpattu", "Tirupathur", "Mayiladuthurai",
    "Kallakurichi", "Tiruvallur", "Tiruvarur",
]

KARNATAKA_CITIES = [
    "Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi",
    "Kalaburagi", "Davangere", "Ballari", "Tumakuru", "Shivamogga",
    "Vijayapura", "Udupi", "Hassan", "Raichur", "Kolar",
    "Chitradurga", "Chikkamagaluru", "Hospet", "Bidar", "Madikeri",
    "Mandya", "Chamarajanagar", "Karwar", "Bagalkot", "Gadag",
    "Haveri", "Yadgir", "Koppal", "Ramanagara", "Chikkaballapur",
]

TELANGANA_CITIES = [
    "Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam",
    "Ramagundam", "Mahbubnagar", "Nalgonda", "Adilabad", "Suryapet",
    "Miryalaguda", "Siddipet", "Jagtial", "Mancherial", "Bhongir",
    "Sangareddy", "Vikarabad", "Medak", "Kothagudem", "Kamareddy",
]

ANDHRA_CITIES = [
    "Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Nellore",
    "Kurnool", "Rajahmundry", "Kakinada", "Anantapur", "Kadapa",
    "Eluru", "Vizianagaram", "Srikakulam", "Ongole", "Chittoor",
    "Machilipatnam", "Tenali", "Proddatur", "Adoni", "Bhimavaram",
    "Nandyal", "Madanapalle", "Hindupur", "Dharmavaram", "Gudivada",
]

ALL_CITIES = (KERALA_CITIES + TAMILNADU_CITIES + KARNATAKA_CITIES
              + TELANGANA_CITIES + ANDHRA_CITIES)
