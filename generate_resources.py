import csv
import random

random.seed(42)

# 1. india_emergency_call_logs.csv
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal", "Jammu and Kashmir", "Ladakh",
    "Puducherry", "Chandigarh", "Andaman and Nicobar Islands", "Lakshadweep"
]
with open('india_emergency_call_logs.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['state','month','year','count'])
    for _ in range(300):
        writer.writerow([
            random.choice(states),
            random.randint(1,12),
            random.randint(2023,2025),
            random.randint(100,2000)
        ])

# 2. general_tourist_faqs.md
first_entries = [
    ("What should I do if I lose my passport in India?",
     "Contact your country's embassy immediately and file a police report at the nearest station."),
    ("Are Indian tourist spots safe for solo travelers?",
     "Most popular spots are safe, but stay aware of surroundings and avoid isolated areas at night."),
    ("What steps should I take if my luggage is lost?",
     "Report it to the airline and fill out a Property Irregularity Report before leaving the airport."),
    ("How can I stay safe during hikes in India?",
     "Inform someone about your route and carry a basic first aid kit."),
    ("What are some key local customs in India?",
     "Remove your shoes before entering homes and dress modestly in religious places."),
    ("Who should I contact in an emergency?",
     "Dial 112 for immediate assistance or visit the nearest police station."),
    ("Do I need travel insurance for India?",
     "Yes, travel insurance can cover medical expenses and trip disruptions."),
    ("Is tap water safe to drink in India?",
     "It's safer to drink bottled or purified water, especially in rural areas."),
    ("Any tips for women traveling alone in India?",
     "Use trusted transport services and avoid traveling alone late at night."),
    ("How do I find a hospital while traveling?",
     "Use online maps or ask locals; major cities have hospitals with English-speaking staff."),
]

lost_items = ["passport", "luggage", "wallet"]
places = ["airport", "train station", "bus station", "hotel", "market", "temple"]
regions = ["Himalayas", "Western Ghats", "Thar Desert", "Nilgiri Hills", "Sahyadri range"]
custom_places = ["homes", "temples", "rural villages", "urban neighborhoods"]
emergencies = ["a medical emergency", "a theft", "an accident", "a fire"]
food_places = ["street stalls", "small cafes", "market vendors", "train canteens"]
cities = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Kolkata", "Hyderabad", "Jaipur"]
issues = ["a fever", "a minor injury", "food poisoning", "dehydration"]

with open('general_tourist_faqs.md','w',encoding='utf-8') as f:
    for idx,(q,a) in enumerate(first_entries, start=1):
        f.write(f"Q{idx}: {q}\n")
        f.write(f"A{idx}: {a}\n\n")
    for idx in range(11,301):
        topic = random.choice(['lost','hike','custom','contact','insurance','food','women'])
        if topic == 'lost':
            item = random.choice(lost_items)
            place = random.choice(places)
            q = f"What should I do if I lose my {item} at a {place} in India?"
            a = f"Report the lost {item} to the nearest authority at the {place} and keep a written record."
        elif topic == 'hike':
            region = random.choice(regions)
            q = f"How can I stay safe while hiking in the {region}?"
            a = f"Carry sufficient water and inform someone about your route in the {region}."
        elif topic == 'custom':
            place = random.choice(custom_places)
            q = f"What local customs should I follow when visiting {place}?"
            a = f"Be respectful, remove your shoes, and dress modestly when visiting {place}."
        elif topic == 'contact':
            emergency = random.choice(emergencies)
            q = f"Who should I contact during {emergency} in India?"
            a = f"Dial 112 to reach emergency services and explain the situation clearly."
        elif topic == 'insurance':
            issue = random.choice(issues)
            q = f"Why should I have travel insurance for {issue} in India?"
            a = f"Insurance helps cover treatment costs if you face {issue}."
        elif topic == 'food':
            place = random.choice(food_places)
            q = f"How can I ensure food safety when eating at {place}?"
            a = f"Choose busy {place} and opt for freshly cooked food to stay safe."
        else:  # women
            city = random.choice(cities)
            q = f"What safety tips help women traveling solo in {city}?"
            a = f"Use licensed transport and stay in well-reviewed accommodations in {city}."
        f.write(f"Q{idx}: {q}\n")
        f.write(f"A{idx}: {a}\n\n")

# 3. forest_alert_protocols.txt
animals = ["tiger","elephant","bear","wild boar","leopard"]
hazards = ["flash floods","landslides","sudden storms","falling rocks","rising rivers"]
signals = ["three short whistle blasts","two long flashlight flashes","a series of three shouts"]
with open('forest_alert_protocols.txt','w',encoding='utf-8') as f:
    for i in range(1,301):
        choice = i % 15
        if choice == 0:
            line = f"Blow your whistle every {5 + (i%6)*5} minutes to alert rescuers."
        elif choice == 1:
            line = f"Mark your trail with ribbons every {10 + (i%9)*10} meters to avoid getting lost."
        elif choice == 2:
            line = f"If you encounter a {random.choice(animals)}, remain calm and slowly back away."
        elif choice == 3:
            line = f"Boil collected water for {2 + (i%5)} minutes before drinking."
        elif choice == 4:
            line = f"Check for leeches on your legs every {10 + (i%5)*5} minutes during rainy hikes."
        elif choice == 5:
            line = f"Store food at least {20 + (i%8)*5} meters away from your camp to deter animals."
        elif choice == 6:
            line = f"Cross streams only where water is below {30 + (i%5)*10} centimeters."
        elif choice == 7:
            line = f"During {random.choice(hazards)}, move to higher ground immediately."
        elif choice == 8:
            line = f"Use {random.choice(signals)} to signal search teams at night."
        elif choice == 9:
            line = f"Build shelters at least {15 + (i%7)*5} meters away from dead trees."
        elif choice == 10:
            line = f"Wrap injuries with clean cloth and seek help within {15 + (i%6)*5} minutes."
        elif choice == 11:
            line = f"Follow a river downstream but keep {10 + (i%6)*10} meters away from the bank."
        elif choice == 12:
            line = f"Apply insect repellent every {2 + (i%4)} hours to prevent bites."
        elif choice == 13:
            line = f"Clear {5 + (i%5)*5} meters around your fire pit to prevent spread."
        else:
            line = f"Use bright cloth to mark your camp, visible from {50 + (i%6)*10} meters away."
        f.write(f"{i}. {line}\n")

# 4. multi_lang_safety_guide.csv with translation placeholders
places = ["mountain paths", "busy markets", "crowded trains", "beach resorts", "remote villages", "heritage sites", "national parks", "river ferries", "city streets", "desert trails"]
with open('multi_lang_safety_guide.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id','English','Hindi','Kannada','Tamil','Bengali','Assamese'])
    for i in range(1,301):
        place = random.choice(places)
        template = i % 10
        if template == 0:
            sentence = f"Carry at least {2 + i%4} liters of water when hiking in {place}"
        elif template == 1:
            sentence = f"Inform a friend before exploring {place} alone"
        elif template == 2:
            sentence = f"Avoid flashing valuables in {place} to prevent theft"
        elif template == 3:
            sentence = f"Wear protective gear when riding bikes on {place}"
        elif template == 4:
            sentence = f"Keep emergency contacts saved before entering {place}"
        elif template == 5:
            sentence = f"Check weather alerts before traveling to {place}"
        elif template == 6:
            sentence = f"Use only registered guides in {place}"
        elif template == 7:
            sentence = f"Stay on marked paths while visiting {place}"
        elif template == 8:
            sentence = f"Respect wildlife and keep {5 + i%10} meters away in {place}"
        else:
            sentence = f"Dispose of trash properly to protect {place}"
        writer.writerow([
            i,
            sentence,
            f"[Hindi translation needed: {sentence}]",
            f"[Kannada translation needed: {sentence}]",
            f"[Tamil translation needed: {sentence}]",
            f"[Bengali translation needed: {sentence}]",
            f"[Assamese translation needed: {sentence}]",
        ])


# 5. sos_response_steps.csv
features = ["river", "cliff", "waterfall", "dense grove", "rocky ridge"]
locations = ["forest trail", "city market", "suburban street", "mountain pass", "village road"]
landmarks = ["old fort", "abandoned hut", "watchtower", "campsite", "bridge"]
roads = ["highway 48", "coastal road", "desert highway", "hill route", "forest road"]
spots = ["stream", "clearing", "cave", "ridge", "valley"]
with open('sos_response_steps.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id','situation','response'])
    for i in range(1,301):
        choice = (i-1) % 10
        if choice == 0:
            feature = random.choice(features)
            situation = f"Lost in forest near a {feature}"
            response = f"Stay put near the {feature} and signal with a whistle every {5 + i%6} minutes."
        elif choice == 1:
            km = i
            situation = f"Injured during trek around kilometer {km}"
            response = f"Apply pressure to the wound at kilometer {km} and await rescue."
        elif choice == 2:
            time = f"{6 + (i%12)}pm"
            situation = f"Phone battery dead while camping at {time}"
            response = f"Remain at your campsite until help arrives; your last ping was at {time}."
        elif choice == 3:
            location = random.choice(locations)
            situation = f"Stranger following me through a {location}"
            response = f"Head toward a crowded area away from the {location} and contact authorities."
        elif choice == 4:
            river = random.choice(features)
            situation = f"Floodwaters rising near the {river}"
            response = f"Move to higher ground away from the {river} and wait for rescue."
        elif choice == 5:
            landmark = random.choice(landmarks)
            situation = f"Caught in wildfire close to a {landmark}"
            response = f"Cover your nose and move opposite the wind near the {landmark}."
        elif choice == 6:
            hour = 1 + (i%12)
            road = random.choice(roads)
            situation = f"Vehicle breakdown at {hour}am on {road}"
            response = f"Stay inside the vehicle on {road} and call roadside assistance."
        elif choice == 7:
            hours = 3 + i%6
            situation = f"Severe dehydration after {hours} hours of hiking"
            response = f"Sip water slowly after hiking {hours} hours and rest in shade."
        elif choice == 8:
            temp = 35 + i%10
            situation = f"Heatstroke symptoms while walking in {temp}C heat"
            response = f"Cool your body in the {temp}C heat with damp cloths and await medical support."
        else:
            spot = random.choice(spots)
            situation = f"Wild animal nearby while resting near a {spot}"
            response = f"Back away from the {spot} slowly and alert rangers immediately."
        writer.writerow([i, situation, response])
