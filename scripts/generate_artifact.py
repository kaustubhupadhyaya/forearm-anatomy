# -*- coding: utf-8 -*-
"""
Generator for forearm_mass_anatomy.html
Interactive, mathematically grounded forearm anatomy, exercise-mapping, and mass prioritization guide.
"""

import json

muscles_data = [
    {
        "id": "brachioradialis",
        "name": "Brachioradialis",
        "compartment": "Lateral (Mobile Wad of Henry)",
        "layer": "Superficial",
        "volume": 65.4,
        "volume_pct": 14.9,
        "pcsa": 5.2,
        "fiber_len": 17.0,
        "pennation": 2.0,
        "origin": "Upper 2/3 of lateral supracondylar ridge of humerus",
        "insertion": "Lateral base of styloid process of radius",
        "primary_action": "Primary elbow flexion in neutral/pronated forearm; stabilizes elbow during rapid movement",
        "moment_arm": "Elbow flexion moment arm: 5.0 - 7.5 cm (peaks at ~90-100 deg flexion). Dwarfs biceps moment arm in full pronation.",
        "rank": 1,
        "tier": "Tier 1: Core Mass Driver",
        "score": 9.8,
        "exercises": [
            {"name": "Reverse Barbell / EZ-Bar Curl", "impact": "Primary", "desc": "Neutral/pronated grip eliminates biceps peak torque via radial tuberosity rotation; loads BR under heavy tensile mechanical tension (40-65 kg)."},
            {"name": "Dumbbell Hammer Curl", "impact": "Primary", "desc": "Neutral alignment maximizes BR line of pull with joint-friendly mechanics."},
            {"name": "Cable Cross-Body Hammer Curl", "impact": "High", "desc": "Continuous resistance through entire elbow flexion arc."}
        ],
        "mass_notes": "Single largest individual muscle in the forearm (65.4 cm3). Located on the anterolateral margin of the proximal forearm, its hypertrophy directly creates the outer upper forearm 'sweep' and widens forearm diameter in both frontal and sagittal planes.",
        "color": "#ef4444"
    },
    {
        "id": "fdp",
        "name": "Flexor Digitorum Profundus (FDP)",
        "compartment": "Anterior Compartment",
        "layer": "Deep",
        "volume": 57.8,
        "volume_pct": 13.2,
        "pcsa": 14.5,
        "fiber_len": 4.5,
        "pennation": 9.0,
        "origin": "Upper 3/4 of anterior & medial ulna, interosseous membrane",
        "insertion": "Bases of distal phalanges of medial 4 digits (split through FDS tendons)",
        "primary_action": "Flexion of Distal Interphalangeal (DIP), PIP, MCP joints and wrist flexion",
        "moment_arm": "DIP/PIP flexion: ~0.8-1.0 cm; Wrist flexion: ~1.2-1.4 cm",
        "rank": 2,
        "tier": "Tier 1: Core Mass Driver",
        "score": 9.6,
        "exercises": [
            {"name": "Finger-Roll Barbell Wrist Curl", "impact": "Primary", "desc": "Allowing bar to roll to fingertips loads FDP under full active stretch across DIP joints before concentric wrist flexion."},
            {"name": "Axle / Fat Grip Heavy Holds", "impact": "Primary", "desc": "Massive isometric crush/support grip tension recruiting high-threshold motor units across large PCSA."},
            {"name": "Arm Wrestling Hand Cup / Rolling Handle", "impact": "High", "desc": "Dynamic flexion under severe load through full finger closure."}
        ],
        "mass_notes": "Highest PCSA in the entire forearm (14.5 cm2) and second largest volume (57.8 cm3). When combined with FDS, forms a 103.7 cm3 flexor engine (23.7% of total forearm mass). Dictates inner forearm depth and palm-to-forearm thickness.",
        "color": "#f97316"
    },
    {
        "id": "fds",
        "name": "Flexor Digitorum Superficialis (FDS)",
        "compartment": "Anterior Compartment",
        "layer": "Intermediate",
        "volume": 45.9,
        "volume_pct": 10.5,
        "pcsa": 10.8,
        "fiber_len": 5.0,
        "pennation": 7.0,
        "origin": "Humeroulnar head (medial epicondyle, coronoid) & Radial head (anterior oblique line)",
        "insertion": "Shafts of middle phalanges of medial 4 digits (slips split for FDP)",
        "primary_action": "Flexion of Proximal Interphalangeal (PIP) and Metacarpophalangeal (MCP) joints, secondary wrist flexion",
        "moment_arm": "PIP/MCP flexion: ~1.1-1.3 cm; Wrist flexion: ~1.4 cm",
        "rank": 3,
        "tier": "Tier 1: Core Mass Driver",
        "score": 9.3,
        "exercises": [
            {"name": "Heavy Barbell Wrist Curls (Palms Up)", "impact": "Primary", "desc": "Direct load through PIP flexion and wrist flexion moment arms."},
            {"name": "Thick Bar / Towel Pull-Ups & Hangs", "impact": "Primary", "desc": "Demands continuous high-force middle-phalanx isometric clamp."},
            {"name": "Gripper Training / Hand Crush", "impact": "High", "desc": "Progressive spring resistance through PIP closure arc."}
        ],
        "mass_notes": "Third largest individual muscle volume (45.9 cm3) and massive PCSA (10.8 cm2). Sits directly beneath the superficial flexor layer, pushing superficial muscles outward and expanding mid-forearm circumference.",
        "color": "#f59e0b"
    },
    {
        "id": "ecrl",
        "name": "Extensor Carpi Radialis Longus (ECRL)",
        "compartment": "Lateral (Mobile Wad of Henry)",
        "layer": "Superficial",
        "volume": 38.2,
        "volume_pct": 8.7,
        "pcsa": 4.5,
        "fiber_len": 9.5,
        "pennation": 5.0,
        "origin": "Lower 1/3 of lateral supracondylar ridge of humerus",
        "insertion": "Dorsal surface of base of 2nd metacarpal",
        "primary_action": "Wrist extension and radial deviation; assists weak elbow flexion",
        "moment_arm": "Wrist extension: ~1.5 cm; Radial deviation: ~1.8 cm; Elbow flexion: ~1.5-2.0 cm",
        "rank": 4,
        "tier": "Tier 2: Ridge & Posterior Shell",
        "score": 8.6,
        "exercises": [
            {"name": "Heavy Reverse Barbell Curl", "impact": "Primary", "desc": "Acts as dynamic stabilizer holding wrist extended against gravity moment arm while assisting elbow flexion."},
            {"name": "Rising / Radial Deviation with Strap/Lever", "impact": "Primary", "desc": "Direct line of pull for radial abduction; dominant driver of wrist rising strength."},
            {"name": "Reverse Wrist Curls (Barbell/Cable)", "impact": "High", "desc": "Direct concentric and eccentric wrist extension loading."}
        ],
        "mass_notes": "Large volume (38.2 cm3) located on the upper outer ridge right next to Brachioradialis. Together with ECRB, creates the upper posterolateral forearm 'shelf' that is instantly visible in short sleeves.",
        "color": "#10b981"
    },
    {
        "id": "fcu",
        "name": "Flexor Carpi Ulnaris (FCU)",
        "compartment": "Anterior Compartment",
        "layer": "Superficial",
        "volume": 37.1,
        "volume_pct": 8.5,
        "pcsa": 7.9,
        "fiber_len": 5.2,
        "pennation": 14.0,
        "origin": "Humeral head (medial epicondyle) & Ulnar head (olecranon & posterior ulna border)",
        "insertion": "Pisiform bone, hook of hamate, and base of 5th metacarpal",
        "primary_action": "Wrist flexion and ulnar deviation (adduction)",
        "moment_arm": "Wrist flexion: 1.8 cm (largest wrist flexion moment arm in human anatomy due to pisiform sesamoid elevation!); Ulnar deviation: 1.5 cm",
        "rank": 5,
        "tier": "Tier 1: Core Mass Driver",
        "score": 8.9,
        "exercises": [
            {"name": "Heavy Seated Barbell Wrist Curl", "impact": "Primary", "desc": "Takes maximum advantage of FCU's 1.8 cm moment arm and 7.9 cm2 PCSA to move 40-60 kg loads."},
            {"name": "Behind-the-Back Standing Barbell Wrist Curl", "impact": "Primary", "desc": "Positions wrist in slight ulnar bias, isolating FCU under deep stretch."},
            {"name": "Ulnar Deviation Lever / Arm Wrestling Cup", "impact": "High", "desc": "Direct resistance against ulnar adduction torque."}
        ],
        "mass_notes": "Largest PCSA among all wrist-only flexors (7.9 cm2). Sits along the medial edge of the forearm; when flexed, forms the prominent medial muscle ridge from elbow to wrist.",
        "color": "#06b6d4"
    },
    {
        "id": "ed",
        "name": "Extensor Digitorum (ED / EDC)",
        "compartment": "Posterior Compartment",
        "layer": "Superficial",
        "volume": 34.2,
        "volume_pct": 7.8,
        "pcsa": 6.2,
        "fiber_len": 6.2,
        "pennation": 6.0,
        "origin": "Lateral epicondyle of humerus via common extensor tendon",
        "insertion": "Extensor expansions of medial 4 digits",
        "primary_action": "Extension of MCP, PIP, DIP joints of digits 2-5; assists wrist extension",
        "moment_arm": "Finger extension: ~0.8-1.2 cm; Wrist extension: ~1.3 cm",
        "rank": 6,
        "tier": "Tier 2: Ridge & Posterior Shell",
        "score": 7.9,
        "exercises": [
            {"name": "Reverse Wrist Curls (Barbell / DB)", "impact": "Primary", "desc": "Drives wrist extension and builds posterior dorsal bulk."},
            {"name": "Wrist Roller (Extension Direction)", "impact": "Primary", "desc": "High continuous time-under-tension across entire dorsal forearm."},
            {"name": "Forearm Finisher / Resistance Band Finger Extensions", "impact": "High", "desc": "Isolates digit extension to produce Roger C's 'piano strings' dorsal definition."}
        ],
        "mass_notes": "Covers the entire center of the posterior forearm (34.2 cm3). Hypertrophy of ED fills the flat dorsal aspect of the forearm, giving 3D roundness and visible striations upon extension.",
        "color": "#3b82f6"
    },
    {
        "id": "ecrb",
        "name": "Extensor Carpi Radialis Brevis (ECRB)",
        "compartment": "Lateral (Mobile Wad of Henry)",
        "layer": "Superficial",
        "volume": 32.8,
        "volume_pct": 7.5,
        "pcsa": 5.8,
        "fiber_len": 6.0,
        "pennation": 9.0,
        "origin": "Lateral epicondyle of humerus via common extensor tendon",
        "insertion": "Dorsal surface of base of 3rd metacarpal",
        "primary_action": "Primary wrist extension and weak radial deviation",
        "moment_arm": "Wrist extension: 1.6 cm (most direct central line of pull for pure wrist extension)",
        "rank": 7,
        "tier": "Tier 2: Ridge & Posterior Shell",
        "score": 8.3,
        "exercises": [
            {"name": "Reverse Barbell / Dumbbell Wrist Curl", "impact": "Primary", "desc": "ECRB is the true prime mover of pure wrist extension, aligning directly through joint axis."},
            {"name": "Reverse Curl Isometric Hold", "impact": "High", "desc": "Maintains wrist in neutral against heavy flexion torque."},
            {"name": "Rising Drills with Arm Wrestling Strap", "impact": "High", "desc": "Co-contracts with ECRL to lock the wrist radially."}
        ],
        "mass_notes": "Sits deep and medial to ECRL. Combined with ECRL and BR, the Mobile Wad accounts for 136.4 cm3 (31.1% of total forearm mass). Essential for dorsal-lateral thickness.",
        "color": "#6366f1"
    },
    {
        "id": "pt",
        "name": "Pronator Teres (PT)",
        "compartment": "Anterior Compartment",
        "layer": "Superficial",
        "volume": 32.1,
        "volume_pct": 7.3,
        "pcsa": 6.8,
        "fiber_len": 5.0,
        "pennation": 10.0,
        "origin": "Humeral head (medial epicondyle) & Ulnar head (coronoid process)",
        "insertion": "Middle of lateral surface of radius (pronator tubercle)",
        "primary_action": "Forearm pronation; assists elbow flexion",
        "moment_arm": "Pronation moment arm: ~1.2-1.5 cm; Elbow flexion: ~1.0-1.4 cm",
        "rank": 8,
        "tier": "Tier 2: Ridge & Posterior Shell",
        "score": 7.7,
        "exercises": [
            {"name": "Judo Belt / Strap Pronation Drill", "impact": "Primary", "desc": "As utilized by Roger C and arm wrestlers: wraps across back of hand, pulling into dynamic pronation against heavy resistance."},
            {"name": "Off-Center Dumbbell / Hammer Pronation", "impact": "Primary", "desc": "Pronating a sledgehammer or dumbbell loaded on one head creates maximal torque at horizontal."},
            {"name": "Pronated Incline Reverse Curls", "impact": "High", "desc": "Loads PT simultaneously as an elbow flexor and pronation stabilizer."}
        ],
        "mass_notes": "Forms the medial border of the cubital fossa in the proximal upper forearm (32.1 cm3, 6.8 cm2 PCSA). Hypertrophy of PT fills out the inner elbow pocket, making the upper arm and forearm merge seamlessly.",
        "color": "#8b5cf6"
    },
    {
        "id": "fcr",
        "name": "Flexor Carpi Radialis (FCR)",
        "compartment": "Anterior Compartment",
        "layer": "Superficial",
        "volume": 25.4,
        "volume_pct": 5.8,
        "pcsa": 4.7,
        "fiber_len": 5.8,
        "pennation": 7.0,
        "origin": "Medial epicondyle of humerus via common flexor tendon",
        "insertion": "Base of 2nd and 3rd metacarpals",
        "primary_action": "Wrist flexion and radial deviation",
        "moment_arm": "Wrist flexion: 1.5 cm; Radial deviation: 1.0 cm",
        "rank": 9,
        "tier": "Tier 3: Balance & Joint Integrity",
        "score": 6.9,
        "exercises": [
            {"name": "Dumbbell Wrist Curl with Radial Tilt", "impact": "Primary", "desc": "Curling with slight outward radial deviation directly follows FCR fiber line."},
            {"name": "Standard Barbell Wrist Curl", "impact": "High", "desc": "Shares wrist flexion load with FCU and finger flexors."},
            {"name": "Radial Deviation Rising Drills", "impact": "Medium", "desc": "Co-contracts anteriorly to prevent wrist extension during rising."}
        ],
        "mass_notes": "Runs obliquely down the anterior radial side of the forearm (25.4 cm3). Its tendon is one of the most prominent landmarks on the palmar wrist.",
        "color": "#ec4899"
    },
    {
        "id": "supinator",
        "name": "Supinator",
        "compartment": "Posterior Compartment",
        "layer": "Deep",
        "volume": 23.6,
        "volume_pct": 5.4,
        "pcsa": 4.8,
        "fiber_len": 5.1,
        "pennation": 10.0,
        "origin": "Lateral epicondyle of humerus, supinator crest of ulna, radial collateral ligament",
        "insertion": "Proximal 1/3 of anterior and lateral surfaces of radius",
        "primary_action": "Pure forearm supination (unassisted by elbow position, unlike biceps brachii)",
        "moment_arm": "Supination moment arm: ~1.0-1.3 cm",
        "rank": 10,
        "tier": "Tier 3: Balance & Joint Integrity",
        "score": 6.6,
        "exercises": [
            {"name": "Offset Dumbbell / Sledgehammer Supination", "impact": "Primary", "desc": "Resisting pronation torque with arm bent at 90 deg isolates the supinator."},
            {"name": "Resistance Band Supination", "impact": "Primary", "desc": "Roger C's prescribed antagonist drill to cure medial epicondylitis and restore arm wrestling balance."},
            {"name": "Dumbbell Zottman Curl (Supinating Eccentric)", "impact": "High", "desc": "Dynamic rotation through full supination arc under load."}
        ],
        "mass_notes": "Deep muscle wrapping tightly around the proximal radius (23.6 cm3). Crucial antagonist to Pronator Teres; neglecting it causes severe elbow torque imbalances and pain.",
        "color": "#14b8a6"
    },
    {
        "id": "ecu",
        "name": "Extensor Carpi Ulnaris (ECU)",
        "compartment": "Posterior Compartment",
        "layer": "Superficial",
        "volume": 20.3,
        "volume_pct": 4.6,
        "pcsa": 4.1,
        "fiber_len": 5.5,
        "pennation": 11.0,
        "origin": "Lateral epicondyle via common extensor tendon & posterior border of ulna",
        "insertion": "Medial side of base of 5th metacarpal",
        "primary_action": "Wrist extension and ulnar deviation",
        "moment_arm": "Wrist extension: ~1.2 cm; Ulnar deviation: ~1.6 cm",
        "rank": 11,
        "tier": "Tier 3: Balance & Joint Integrity",
        "score": 6.3,
        "exercises": [
            {"name": "Ulnar Deviation Lever / Band Drills", "impact": "Primary", "desc": "Essential antagonist drill mentioned by Roger C to balance high-volume rising/radial deviation."},
            {"name": "Reverse Wrist Curls with Ulnar Flare", "impact": "High", "desc": "Emphasizes the ulnar posterior border."},
            {"name": "Hammer Levering (Behind the Back)", "impact": "High", "desc": "Loaded levering through ulnar deviation plane."}
        ],
        "mass_notes": "Forms the posterior ulnar margin of the forearm (20.3 cm3). Balances FCU on the ulnar border and prevents wrist instability.",
        "color": "#a855f7"
    },
    {
        "id": "deep_distal",
        "name": "Pronator Quadratus & Thumb Outcroppings (APL / EPB / EPL)",
        "compartment": "Deep Anterior & Deep Posterior",
        "layer": "Deep",
        "volume": 35.0,
        "volume_pct": 8.0,
        "pcsa": 10.7,
        "fiber_len": 3.8,
        "pennation": 8.0,
        "origin": "PQ: Distal 1/4 anterior ulna; APL/EPB: Posterior radius/ulna/interosseous membrane",
        "insertion": "PQ: Distal 1/4 anterior radius; APL: Base of 1st metacarpal; EPB/EPL: Proximal & distal phalanges of thumb",
        "primary_action": "PQ: Initiates pronation, binds radius & ulna; APL/EPB/EPL: Thumb abduction, extension, radial deviation",
        "moment_arm": "PQ pronation: ~1.0 cm; APL radial deviation: ~1.2 cm",
        "rank": 12,
        "tier": "Tier 3: Balance & Joint Integrity",
        "score": 5.8,
        "exercises": [
            {"name": "High-Rep Rising Drills (Roger C Method)", "impact": "Primary", "desc": "5 sets of 60 reps with 10 kg strap loads APL, EPB and radial tendons continuously, stimulating collagen synthesis."},
            {"name": "Heavy Plate Pinch Holds", "impact": "Primary", "desc": "Demands maximum isometric thumb adduction and abduction stability."},
            {"name": "Pronation Band Drills at Distal Wrist", "impact": "High", "desc": "Forces PQ to resist distal radioulnar separation shear."}
        ],
        "mass_notes": "Pronator Quadratus is the ONLY true muscle belly situated in the distal 1/4 of the forearm. Hypertrophy of PQ combined with tendon sheath expansion accounts for the direct muscular component of wrist growth.",
        "color": "#eab308"
    }
]

exercises_master = [
    {
        "id": "reverse_curl",
        "name": "Heavy Reverse Barbell / EZ-Bar Curl",
        "category": "Compound Elbow Flexion",
        "tier": "Tier 1 Priority",
        "primary_muscles": ["Brachioradialis", "ECRL", "ECRB"],
        "secondary_muscles": ["Pronator Teres", "Extensor Digitorum", "Brachialis"],
        "biomechanics": "Pronated forearm position wraps biceps tendon around radius, mechanically disadvantageous for biceps. Brachioradialis moment arm peaks at 90-100 deg flexion (5.0-7.5 cm). Requires static isometric contraction of ECRL/ECRB to prevent wrist collapse into flexion.",
        "roger_c_protocol": "Roger C curls 60 kg for 4 sets of 12 reps. Notes that the static extensor hold creates dense, thick wrist tendons and forearm ridges.",
        "optimal_prescription": "3 - 4 sets of 8 - 12 reps, 2.5 min rest, strict 2-second eccentric phase."
    },
    {
        "id": "wrist_curl",
        "name": "Heavy Finger-Roll Barbell Wrist Curl",
        "category": "Dynamic Wrist & Finger Flexion",
        "tier": "Tier 1 Priority",
        "primary_muscles": ["Flexor Digitorum Profundus (FDP)", "Flexor Digitorum Superficialis (FDS)", "Flexor Carpi Ulnaris (FCU)"],
        "secondary_muscles": ["Flexor Carpi Radialis (FCR)", "Pronator Teres"],
        "biomechanics": "Rolling bar down to distal phalanges places FDP and FDS into extreme stretch. Initiating movement with finger flexion engages high-PCSA digit flexors (25.3 cm2 combined). FCU provides peak wrist flexion torque with 1.8 cm moment arm via pisiform sesamoid.",
        "roger_c_protocol": "Roger C works up to 50 kg wrist curls for 6 reps. Attributes the outward popping of palmar wrist tendons and massive medial forearm belly directly to this movement.",
        "optimal_prescription": "4 sets of 10 - 15 reps, full range of motion from fingertips to full wrist flexion, 1-second pause at contraction."
    },
    {
        "id": "reverse_wrist_curl",
        "name": "Reverse Wrist Curl / Forearm Finisher (Wrist Extension)",
        "category": "Isolated Wrist Extension",
        "tier": "Tier 2 Priority",
        "primary_muscles": ["ECRB", "ECRL", "Extensor Digitorum (ED)"],
        "secondary_muscles": ["Extensor Carpi Ulnaris (ECU)", "Extensor Pollicis Longus"],
        "biomechanics": "Pure sagittal extension of carpus against gravity or cable vector. ECRB provides central line of pull. Essential for building the visible posterior 'piano strings' and counteracting hyper-toned flexors.",
        "roger_c_protocol": "Roger C recommends isolation wrist extensions or the 'Forearm Finisher' tool to create deep extensor striations and protect against wrist flexion imbalance.",
        "optimal_prescription": "3 - 4 sets of 15 - 20 reps with light-to-moderate load or cable constant tension."
    },
    {
        "id": "pronation_strap",
        "name": "Arm Wrestling Strap Pronation Drill",
        "category": "Rotational Joint Torque",
        "tier": "Tier 2 Priority",
        "primary_muscles": ["Pronator Teres (PT)", "Pronator Quadratus (PQ)"],
        "secondary_muscles": ["Brachioradialis", "Flexor Carpi Radialis"],
        "biomechanics": "Strap routes across dorsal hand into thumb crease, applying external supination torque. Pronator Teres operates at maximal mechanical leverage with elbow at 90 deg flexion.",
        "roger_c_protocol": "Roger C used 5 sets of 60 reps with 10 kg strap daily for 300+ days. Notes that high-rep tensile loading drove connective tissue, bone remodeling, and tendon thickening.",
        "optimal_prescription": "Hypertrophy mode: 3 - 4 sets of 12 - 15 reps; Tendon conditioning mode: 3 sets of 30 - 50 reps with controlled cadence."
    },
    {
        "id": "rising_strap",
        "name": "Rising / Radial Deviation Strap Drill",
        "category": "Frontal Plane Abduction",
        "tier": "Tier 2 Priority",
        "primary_muscles": ["ECRL", "ECRB", "Abductor Pollicis Longus (APL)", "Extensor Pollicis Brevis (EPB)"],
        "secondary_muscles": ["Flexor Carpi Radialis"],
        "biomechanics": "Applies downward ulnar deviation torque across the index knuckle. ECRL and ECRB fire to elevate the wrist vertically in neutral plane, thickening the radial styloid region.",
        "roger_c_protocol": "Roger C paired 5 sets of 60 reps rising with pronation daily. Emphasizes that this movement attacks the joint structure and radial tendon insertion directly.",
        "optimal_prescription": "3 - 4 sets of 15 - 20 reps or loaded static holds with judo belt/strap."
    },
    {
        "id": "supination_antagonist",
        "name": "Resisted Supination (Antagonist Balancer)",
        "category": "Rotational Joint Torque",
        "tier": "Tier 3 Priority (Mandatory for Joint Health)",
        "primary_muscles": ["Supinator", "Biceps Brachii"],
        "secondary_muscles": ["ECRL"],
        "biomechanics": "Isolates the deep supinator muscle. Crucial antagonist to Pronator Teres to prevent medial epicondylitis (golfer's elbow) and restore normal radioulnar arthrokinematics.",
        "roger_c_protocol": "Roger C admits completely ignoring supination for months, resulting in severe elbow pain. Added band supination to eliminate pain and restore hook capability.",
        "optimal_prescription": "2 - 3 sets of 15 - 20 reps with elastic band or offset dumbbell 2-3x per week."
    },
    {
        "id": "ulnar_deviation",
        "name": "Ulnar Deviation Levering (Antagonist Balancer)",
        "category": "Frontal Plane Adduction",
        "tier": "Tier 3 Priority (Mandatory for Joint Health)",
        "primary_muscles": ["Flexor Carpi Ulnaris (FCU)", "Extensor Carpi Ulnaris (ECU)"],
        "secondary_muscles": ["FDP"],
        "biomechanics": "Antagonist movement to rising. Clamps FCU and ECU synchronously, stabilizing the triangular fibrocartilage complex (TFCC) on the ulnar side of the wrist.",
        "roger_c_protocol": "Prescribed alongside supination to counter the 60-rep rising drills and balance the wrist circumference symmetrically.",
        "optimal_prescription": "2 - 3 sets of 15 - 20 reps with light lever or band."
    },
    {
        "id": "fat_grip_holds",
        "name": "Axle / Fat Grip Dead Hangs & Holds",
        "category": "Isometric Support & Crush Grip",
        "tier": "Tier 1 Priority",
        "primary_muscles": ["Flexor Digitorum Profundus", "Flexor Digitorum Superficialis", "Flexor Pollicis Longus"],
        "secondary_muscles": ["Extensor Carpi Radialis (stabilizing)", "Brachioradialis"],
        "biomechanics": "Large diameter (2 to 2.5 inches) forces hand open, preventing passive mechanical finger locking. Requires continuous maximal voluntary contraction of FDP and FDS muscle bellies.",
        "roger_c_protocol": "Recommends fat grips on dumbbells and barbells as an essential base for hand and wrist adaptation.",
        "optimal_prescription": "3 - 4 sets of 20 - 40 second holds to near failure."
    }
]

print("Muscles and exercises dataset ready.")
