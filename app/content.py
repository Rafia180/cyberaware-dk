"""
content.py - ALL the words on the website live in this file.

This version has NO database. The content is written once, here, as
normal Python lists and dictionaries. main.py imports them and hands
them to the HTML templates. Change a word here, restart the server,
and the website shows the change.

Why no database? The site only SHOWS fixed content. Nobody logs in,
nothing is typed in, nothing is saved. A database would add code
(creating tables, copying content in, reading it back out) without
adding anything the reader can see.

The file has four parts:
  1) TOPICS           the five scam topics on the Learn page
  2) CORE_RULES       the eight rules at the top of the Learn page
  3) EMERGENCY_STEPS  the seven steps on the Get Help page
  4) HELP_CHANNELS    the official contacts on the Get Help page
  plus one small helper function, get_topic(), at the bottom.

IMPORTANT: every example message in this file is INVENTED for teaching.
Each one follows a pattern described in the official Danish guidance
listed under that topic's "sources", but no message here was copied
from a real victim or a real scam.
"""


# ---------------------------------------------------------------------
# 1) The five topics.
#
# Each topic is one main area of scams. A fake text, a fake email and a
# fake phone call get the same advice, so they share one topic instead
# of having one each. The "covers" line on each card lists the names a
# reader might be looking for, such as "SKAT" or "QR codes".
#
# Every topic is a dictionary with exactly the same keys. The first one
# is labelled so you can see what each key is for.
# ---------------------------------------------------------------------

TOPICS = [
    {
        # The end of the web address: /learn/fake-messages
        # Lowercase, words joined by "-", different for every topic.
        "slug": "fake-messages",

        # The card title, the one-line summary under it, and the names
        # a reader might be looking for ("Is my SMS in here?").
        "title": "Fake messages, calls and impersonation",
        "short": "A message, call or QR code from someone pretending to be a company, a friend or technical support.",
        "covers": "Email, SMS, phone calls, QR codes, 'new number' messages, fake technical support",


        # "What is it?" on the topic page. The brackets ( ) let one long
        # piece of text run over several lines. Python joins them up.
        "definition": (
            "Scammers contact you by email, text message, phone call or QR "
            "code, pretending to be someone you trust: a delivery company, a "
            "well-known business, technical support, or even a friend with a "
            "new number. The channel changes, but the trick is the same: get "
            "you to click, scan, pay or let them into your computer before "
            "you check. The sender's name and the number on your screen can "
            "both be faked."
        ),

        # Invented examples. Each has a short label (how it arrived) and
        # the text. A topic can have one, two or three examples.
        "examples": [
            {"label": "Text message",
             "text": "PostNord: Your package cannot be delivered. Pay 29 DKK "
                     "to arrange delivery. [link]"},
            {"label": "Phone call",
             "text": "We have detected a virus on your computer. Let us "
                     "connect remotely and we will remove it for you."},
            {"label": "Message from a new number",
             "text": "Hi, I lost my phone, this is my new number. I need to "
                     "pay something urgently. Can you transfer it for me?"},
        ],

        # Three short lists. Each line becomes one bullet point.
        # Kept to four or five lines each, so the page stays short.
        "red_flags": [
            "You were not expecting it",
            "It is urgent: a deadline, a threat or an emergency",
            "It asks you to click a link, scan a QR code or pay a small fee",
            "It asks for a password, a code, your CPR number or card details",
            "A friend writes from a new number, or a caller wants to connect to your computer",
        ],
        "do_steps": [
            "Stop. A real company will let you take your time",
            "Open the company's own app or website yourself",
            "Call back on a number from the official website, not the one you were given",
            "If it is a friend, call them on the number you already have",
        ],
        "dont_steps": [
            "Do not click links or scan QR codes you were sent",
            "Do not read out codes or approve MitID during a call",
            "Do not install software or let a caller connect to your computer",
            "Do not trust the sender's name or the number on your screen",
        ],

        # "Who can help" on the topic page.
        "help": (
            "If you clicked, paid or shared details, contact your bank to "
            "block your card, then call the Cyberhotline on 33 37 00 37. If "
            "someone connected to your computer, disconnect it from the "
            "internet first."
        ),

        # Official links: the text to show ("label") and the address ("url").
        "sources": [
                        {"label": "sikkerdigital.dk - how to spot fake emails",
             "url": "https://www.sikkerdigital.dk/borger/spot-svindel/saadan-spotter-du-falske-mails"},
            {"label": "sikkerdigital.dk - how to spot fake messages",
             "url": "https://www.sikkerdigital.dk/borger/spot-svindel/saadan-spotter-du-falske-beskeder"},
            {"label": "borger.dk - spot fake emails, messages and calls",
             "url": "https://www.borger.dk/internet-og-sikkerhed/digitale-trusler/spot-falske-e-mails--beskeder-og-opkald"},
        ],
    },
    {
        "slug": "danish-services",
        "title": "Danish services and identity",
        "short": "Someone pretends to be MitID, SKAT, SIRI, Digital Post or the police.",
        "covers": "MitID, CPR number, SKAT, SIRI and the Immigration Service, Digital Post, the police",
        "definition": (
            "Scammers copy the Danish services you depend on, because people "
            "trust them and worry about getting something wrong. They try to "
            "make you approve a MitID login they started, hand over your CPR "
            "number and ID, pay a fake fee to keep your residence permit, or "
            "move your money 'to keep it safe'. Real authorities send case "
            "messages through Digital Post, and never ask for your MitID "
            "details, your card details, or for you to move money."
        ),
        "examples": [
            {"label": "MitID message",
             "text": "Your MitID has been compromised. You must verify your "
                     "account immediately or it will be blocked."},
            {"label": "Tax refund",
             "text": "You have a tax refund of 4,250 DKK waiting. Enter your "
                     "card details to receive your money."},
            {"label": "Residence permit",
             "text": "There is a problem with your residence permit. You must "
                     "pay 2,000 DKK today or your permit will be cancelled."},
        ],
        "red_flags": [
            "A MitID request appears that you did not start",
            "A refund that needs your card details",
            "A threat to your residence permit unless you pay today",
            "An unexpected request for your CPR number or a photo of your ID",
            "A caller says they are the police and asks you to move money to a 'safe account'",
        ],
        "do_steps": [
            "Only approve a MitID request you started yourself, seconds earlier",
            "Open Digital Post, skat.dk or nyidanmark.dk yourself and check there",
            "End the call and phone the authority on a number from its website",
            "If your CPR number and ID have been exposed, consider a credit "
            "warning (kreditadvarsel)",
        ],
        "dont_steps": [
            "Never approve MitID while someone is on the phone with you",
            "Never share your MitID details, not even with your bank or the police",
            "Do not enter card details to receive a refund",
            "Do not pay or move money because a caller says they are an authority",
        ],
        "help": (
            "Call the Cyberhotline on 33 37 00 37 straight away. They can "
            "block your MitID, also outside their normal opening hours. "
            "Contact the real authority through its own website."
        ),
        "sources": [
            {"label": "MitID - official security and phishing guidance",
             "url": "https://www.mitid.dk/sikkerhed/phishing/"},
            {"label": "SIRI and the Immigration Service - warning about phone and email fraud (July 2026)",
             "url": "https://nyidanmark.dk/da/Nyheder/2026/07/SIRI-og-Udlaendingestyrelsen-advarer-mod-telefonsvindel-og-falske-mails"},
            {"label": "borger.dk - credit warning (kreditadvarsel)",
             "url": "https://www.borger.dk/internet-og-sikkerhed/digitale-trusler/Kreditadvarsel"},
            {"label": "Digital Post - information in English",
             "url": "https://lifeindenmark.borger.dk/apps-and-digital-services/Digital-Post"},
        ],
    },
    {
        "slug": "money-and-buying",
        "title": "Money, banking and online buying",
        "short": "A fake bank, buyer, seller or investment that wants your money.",
        "covers": "Your bank, 'safe accounts', DBA and Facebook Marketplace, investment and crypto",
        "definition": (
            "Some scams go straight for your money. A caller pretends to be "
            "your bank and asks you to approve something or move money. A "
            "seller on DBA or Facebook Marketplace takes payment for something "
            "that does not exist, or a 'buyer' sends a fake payment "
            "confirmation. An investment promises guaranteed returns, then "
            "asks for fees. A transfer you make yourself is very hard to get "
            "back."
        ),
        "examples": [
            {"label": "Bank call",
             "text": "There has been suspicious activity on your account. "
                     "Please confirm with MitID so we can secure it."},
            {"label": "Online seller",
             "text": "Many people want this phone. Send the money now and I "
                     "will post it tomorrow."},
            {"label": "Investment",
             "text": "Invest 1,000 DKK today and our trading system will "
                     "double your money within a month. Guaranteed."},
        ],
        "red_flags": [
            "You are asked to approve with MitID, or to move money to a 'safe account'",
            "A price far below normal, and pressure to pay now",
            "You are sent a payment confirmation instead of the money arriving",
            "The other person wants to move the chat or payment off the platform",
            "Guaranteed returns, or a fee before you can take out your own money",
        ],
        "do_steps": [
            "Hang up and call your bank on the number in its app",
            "Keep messages and payment on the platform",
            "Check money has really arrived in your account before you send anything",
            "Talk to someone you trust before you invest",
            "If money has gone, contact your bank immediately. Speed matters",
        ],
        "dont_steps": [
            "Never share your PIN, full password or MitID with a caller",
            "Do not pay by bank transfer to a seller you cannot check",
            "Do not send an item because of a payment confirmation message",
            "Do not pay a fee to release your own money",
        ],
        "help": (
            "Contact your bank first, then the Cyberhotline on 33 37 00 37, "
            "then report it to the police."
        ),
        "sources": [
            {"label": "sikkerdigital.dk - Cyberhotline",
             "url": "https://www.sikkerdigital.dk/cyberhotline"},
            {"label": "sikkerdigital.dk - digital fraud",
             "url": "https://www.sikkerdigital.dk/borger/digital-svindel/falske-mails-beskeder-og-opkald"},
            {"label": "Danish Police - report online financial crime",
             "url": "https://politi.dk/anmeld-kriminalitet/digital-kriminalitet/anmeld-oekonomisk-svindel-paa-nettet-og-digital-kriminalitet"},
        ],
    },
    {
        "slug": "housing-and-jobs",
        "title": "Housing and job scams",
        "short": "A room that does not exist, or a job that costs you money.",
        "covers": "Rental adverts, deposits, job offers, money mules",
        "definition": (
            "When you first arrive, you need a home and often a job, and "
            "scammers know it. A housing scam is a fake rental advert, or "
            "someone renting out a home they have no right to rent, who asks "
            "for a deposit before you have seen it. A job scam is a fake offer "
            "that asks you to pay a fee, or to receive money into your account "
            "and send it on. That is called money muling. It is money "
            "laundering, and you can be prosecuted even if you did not know, "
            "which can affect your right to stay."
        ),
        "examples": [
            {"label": "Rental advert",
             "text": "Beautiful room in central Copenhagen, very cheap. I am "
                     "abroad so I cannot show it, but many students are "
                     "interested. Send the deposit today to reserve it."},
            {"label": "Job offer",
             "text": "Congratulations, you have been selected as a Financial "
                     "Agent. No interview needed. Receive payments into your "
                     "account, keep 10 percent and send on the rest."},
        ],
        "red_flags": [
            "The rent is clearly below other homes in the same area",
            "The landlord is abroad and cannot show you the home",
            "A deposit is asked for before any viewing",
            "A job you never applied for, with high pay and no real interview",
            "You are asked to receive money into your account and send it on",
        ],
        "do_steps": [
            "View the home in person, or on a live video call where you ask "
            "to see specific things",
            "Get a written contract, and keep every message and receipt",
            "Check that you will be able to register your address there",
            "Look up the company yourself and check its CVR number",
            "Ask your university's housing office or careers service if you are unsure",
        ],
        "dont_steps": [
            "Do not pay a deposit before viewing, and do not pay in cash",
            "Never pay to get a job",
            "Never let anyone use your bank account to move money",
            "Do not let pressure decide for you",
        ],
        "help": (
            "If you have paid a deposit or moved money for someone, stop, "
            "contact your bank and report it to the Danish Police. Acting "
            "quickly matters. Your university can also advise you."
        ),
        "sources": [
            {"label": "Aarhus University - avoiding housing scams",
             "url": "https://international.au.dk/life/locations/housing/auhousing/info/avoiding-housing-scams-1"},
            {"label": "Danish Police - report online financial crime",
             "url": "https://politi.dk/anmeld-kriminalitet/digital-kriminalitet/anmeld-oekonomisk-svindel-paa-nettet-og-digital-kriminalitet"},
            {"label": "sikkerdigital.dk - digital fraud",
             "url": "https://www.sikkerdigital.dk/borger/digital-svindel/falske-mails-beskeder-og-opkald"},
        ],
    },
    {
        "slug": "relationship-scams",
        "title": "Relationship and trust scams",
        "short": "Someone builds a friendship or romance online, then asks for money.",
        "covers": "Dating apps, social media, new online friends and partners",
        "definition": (
            "A scammer builds a romance or a close friendship online over "
            "weeks or months, then creates an emergency that only money can "
            "solve, or offers to help you invest. Being new in a country, "
            "away from your usual friends and family, is exactly the "
            "situation these scams are designed for. They are common, and "
            "there is no reason to feel embarrassed."
        ),
        "examples": [
            {"label": "Emergency",
             "text": "I really trust you. I have an emergency and need 5,000 "
                     "DKK. I will pay you back next week, I promise."},
            {"label": "After weeks of chatting",
             "text": "I have been making good money with this trading app. "
                     "I can help you start, you just need to send 2,000 DKK first."},
        ],
        "red_flags": [
            "They always have a reason not to meet or video call",
            "The relationship becomes very intense very quickly",
            "An emergency appears that only money can solve",
            "They ask you to invest, or to receive or send money for them",
            "They ask you not to tell your friends or family",
        ],
        "do_steps": [
            "Tell someone you trust, and listen to what they say",
            "Ask for a video call, and notice how they react",
            "Stop sending money the moment you have doubts",
            "Keep the messages if you think you are being scammed",
        ],
        "dont_steps": [
            "Do not send money to someone you have not met in person",
            "Do not share bank details or let anyone use your account",
            "Do not send intimate photos, which can be used to blackmail you",
            "Do not keep it secret because you were asked to",
        ],
        "help": (
            "Call the Cyberhotline on 33 37 00 37, and report it to the police."
        ),
        "sources": [
            {"label": "sikkerdigital.dk - digital fraud",
             "url": "https://www.sikkerdigital.dk/borger/digital-svindel/falske-mails-beskeder-og-opkald"},
            {"label": "Danish Police - report online financial crime",
             "url": "https://politi.dk/anmeld-kriminalitet/digital-kriminalitet/anmeld-oekonomisk-svindel-paa-nettet-og-digital-kriminalitet"},
        ],
    },
]


# ---------------------------------------------------------------------
# 2) The eight rules shown at the top of the Learn page.
#
# Each rule has a short "title" (always visible) and a "text" that
# appears when the reader clicks the rule.
# ---------------------------------------------------------------------

CORE_RULES = [
    {"title": "Slow down when someone creates urgency",
     "text": "Pressure to act immediately is the most reliable warning sign there "
             "is. A genuine organisation will let you take your time."},
    {"title": "Do not trust unexpected links",
     "text": "Open the organisation's website or app yourself instead of "
             "following a link you were sent."},
    {"title": "Protect your MitID",
     "text": "Never share MitID details, and never approve a request you did not "
             "start yourself moments earlier."},
    {"title": "Protect your CPR number",
     "text": "Do not give your CPR number or ID photos in response to an "
             "unexpected message or call."},
    {"title": "Protect your bank details",
     "text": "No genuine bank will ask for your PIN, full password, or for you to "
             "move money to a safe account."},
    {"title": "Make contact yourself",
     "text": "Find the official phone number or website independently rather than "
             "using the details in the suspicious message."},
    {"title": "Ask someone you trust",
     "text": "A classmate, a friend or your university can give you a second "
             "opinion. Scammers rely on you deciding alone."},
    {"title": "Keep the evidence",
     "text": "Take screenshots before you delete anything. You will need them if "
             "you report the incident."},
]


# ---------------------------------------------------------------------
# 3) The steps on the Get Help page: what to do if you think you have
#    been scammed. Shown in this order. CSS adds the numbers 1 to 7.
# ---------------------------------------------------------------------

EMERGENCY_STEPS = [
    {"title": "Stop",
     "text": "Send no more money and give no more information, even if you are "
             "told that doing so will fix the problem."},
    {"title": "Break contact",
     "text": "Stop replying. Do not answer further calls from the same number."},
    {"title": "Protect what was exposed",
     "text": "Card details: contact your bank and block the card. MitID: call the "
             "Cyberhotline to block it. CPR number: consider a credit warning. "
             "A password: change it now, and anywhere else you reused it."},
    {"title": "Save the evidence",
     "text": "Screenshots, emails, text messages, phone numbers, web addresses "
             "and payment receipts. Save these before deleting anything."},
    {"title": "Contact your bank",
     "text": "If money or card details are involved, call your bank immediately. "
             "The sooner you call, the better the chance of stopping a payment."},
    {"title": "Call the Cyberhotline",
     "text": "33 37 00 37. Open weekdays 08:00-20:00, and 10:00-16:00 at weekends "
             "and on public holidays. MitID blocking is available outside these "
             "hours."},
    {"title": "Report it to the police",
     "text": "Report online financial crime through politi.dk. Reporting also "
             "helps build the picture of what is happening to other students."},
]


# ---------------------------------------------------------------------
# 4) The official contacts on the Get Help page, one card each:
#    "problem" - the card's heading, the reader's situation
#    "contact" - who to contact
#    "note"    - one short line of advice
#    "label" and "url" - the link at the bottom of the card. A contact
#                        with an empty "url" shows no link.
# ---------------------------------------------------------------------

HELP_CHANNELS = [
    {"problem": "Any digital scam, and general guidance",
     "contact": "Cyberhotline, 33 37 00 37",
     "label": "sikkerdigital.dk - Cyberhotline",
     "url": "https://www.sikkerdigital.dk/cyberhotline",
     "note": "Weekdays 08:00-20:00, weekends and holidays 10:00-16:00. "
             "MitID blocking outside these hours."},
    {"problem": "MitID compromised or misused",
     "contact": "MitID support, or the Cyberhotline to block",
     "label": "MitID - security guidance",
     "url": "https://www.mitid.dk/sikkerhed/phishing/",
     "note": "Block MitID first, then investigate."},
    {"problem": "Money or card details lost",
     "contact": "Your own bank, immediately",
     "label": "",
     "url": "",          # no link: every bank is different (see get_help.html)
     "note": "Speed matters most here. Call before anything else."},
    {"problem": "CPR number exposed, or identity theft",
     "contact": "Cyberhotline, plus a credit warning",
     "label": "borger.dk - credit warning (kreditadvarsel)",
     "url": "https://www.borger.dk/internet-og-sikkerhed/digitale-trusler/Kreditadvarsel",
     "note": "A credit warning tells lenders to take extra care in your name."},
    {"problem": "Reporting fraud",
     "contact": "Danish Police",
     "label": "politi.dk - report online financial crime",
     "url": "https://politi.dk/anmeld-kriminalitet/digital-kriminalitet/anmeld-oekonomisk-svindel-paa-nettet-og-digital-kriminalitet",
     "note": "Have your evidence ready before you start."},
    {"problem": "Tax related messages",
     "contact": "SKAT",
     "label": "skat.dk",
     "url": "https://www.skat.dk/",
     "note": "Real refunds are paid to your NemKonto automatically."},
    {"problem": "Residence permit and immigration",
     "contact": "SIRI or the Danish Immigration Service",
     "label": "nyidanmark.dk",
     "url": "https://www.nyidanmark.dk/en-GB",
     "note": "Real case messages arrive in Digital Post."},
    {"problem": "Digital Post problems",
     "contact": "Digital Post support, 33 98 00 33",
     "label": "borger.dk - Digital Post support",
     "url": "https://www.borger.dk/hjaelp-og-vejledning/kontakt/kontakt-digital-post-supporten",
     "note": "Weekdays 08:00-20:00, weekends and holidays 10:00-16:00."},
    {"problem": "Consumer advice",
     "contact": "Forbrugerrådet Tænk",
     "label": "taenk.dk",
     "url": "https://taenk.dk/",
     "note": "Independent Danish consumer organisation."},
]


# ---------------------------------------------------------------------
# A small helper used by main.py.
# ---------------------------------------------------------------------

def get_topic(slug):
    """
    Find one topic by its slug, e.g. get_topic("housing-scams").

    It goes through TOPICS one by one and returns the first topic whose
    "slug" matches. If none matches (someone typed a wrong address), it
    returns None, and main.py shows a "page not found" error.
    """
    for topic in TOPICS:
        if topic["slug"] == slug:
            return topic
    return None