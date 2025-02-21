import sys
from app.models.card import Card

sys.stdout.reconfigure(encoding="utf-8")

hiragana_mapping = [
    ("あ", "a"),
    ("い", "i"),
    ("う", "u"),
    ("え", "e"),
    ("お", "o"),
    ("か", "ka"),
    ("き", "ki"),
    ("く", "ku"),
    ("け", "ke"),
    ("こ", "ko"),
    ("さ", "sa"),
    ("し", "shi"),
    ("す", "su"),
    ("せ", "se"),
    ("そ", "so"),
    ("た", "ta"),
    ("ち", "chi"),
    ("つ", "tsu"),
    ("て", "te"),
    ("と", "to"),
    ("な", "na"),
    ("に", "ni"),
    ("ぬ", "nu"),
    ("ね", "ne"),
    ("の", "no"),
    ("は", "ha"),
    ("ひ", "hi"),
    ("ふ", "fu"),
    ("へ", "he"),
    ("ほ", "ho"),
    ("ま", "ma"),
    ("み", "mi"),
    ("む", "mu"),
    ("め", "me"),
    ("も", "mo"),
    ("や", "ya"),
    ("ゆ", "yu"),
    ("よ", "yo"),
    ("ら", "ra"),
    ("り", "ri"),
    ("る", "ru"),
    ("れ", "re"),
    ("ろ", "ro"),
    ("わ", "wa"),
    ("を", "wo"),
    ("ん", "n"),
]

katakana_mapping = [
    ("ア", "a"),
    ("イ", "i"),
    ("ウ", "u"),
    ("エ", "e"),
    ("オ", "o"),
    ("カ", "ka"),
    ("キ", "ki"),
    ("ク", "ku"),
    ("ケ", "ke"),
    ("コ", "ko"),
    ("サ", "sa"),
    ("シ", "shi"),
    ("ス", "su"),
    ("セ", "se"),
    ("ソ", "so"),
    ("タ", "ta"),
    ("チ", "chi"),
    ("ツ", "tsu"),
    ("テ", "te"),
    ("ト", "to"),
    ("ナ", "na"),
    ("ニ", "ni"),
    ("ヌ", "nu"),
    ("ネ", "ne"),
    ("ノ", "no"),
    ("ハ", "ha"),
    ("ヒ", "hi"),
    ("フ", "fu"),
    ("ヘ", "he"),
    ("ホ", "ho"),
    ("マ", "ma"),
    ("ミ", "mi"),
    ("ム", "mu"),
    ("メ", "me"),
    ("モ", "mo"),
    ("ヤ", "ya"),
    ("ユ", "yu"),
    ("ヨ", "yo"),
    ("ラ", "ra"),
    ("リ", "ri"),
    ("ル", "ru"),
    ("レ", "re"),
    ("ロ", "ro"),
    ("ワ", "wa"),
    ("ヲ", "wo"),
    ("ン", "n"),
]

mixed_mapping = [
    ("あ", "a"),
    ("い", "i"),
    ("う", "u"),
    ("え", "e"),
    ("お", "o"),
    ("か", "ka"),
    ("き", "ki"),
    ("く", "ku"),
    ("け", "ke"),
    ("こ", "ko"),
    ("さ", "sa"),
    ("し", "shi"),
    ("す", "su"),
    ("せ", "se"),
    ("そ", "so"),
    ("た", "ta"),
    ("ち", "chi"),
    ("つ", "tsu"),
    ("て", "te"),
    ("と", "to"),
    ("な", "na"),
    ("に", "ni"),
    ("ぬ", "nu"),
    ("ね", "ne"),
    ("の", "no"),
    ("は", "ha"),
    ("ひ", "hi"),
    ("ふ", "fu"),
    ("へ", "he"),
    ("ほ", "ho"),
    ("ま", "ma"),
    ("み", "mi"),
    ("む", "mu"),
    ("め", "me"),
    ("も", "mo"),
    ("や", "ya"),
    ("ゆ", "yu"),
    ("よ", "yo"),
    ("ら", "ra"),
    ("り", "ri"),
    ("る", "ru"),
    ("れ", "re"),
    ("ろ", "ro"),
    ("わ", "wa"),
    ("を", "wo"),
    ("ん", "n"),
    ("ア", "a"),
    ("イ", "i"),
    ("ウ", "u"),
    ("エ", "e"),
    ("オ", "o"),
    ("カ", "ka"),
    ("キ", "ki"),
    ("ク", "ku"),
    ("ケ", "ke"),
    ("コ", "ko"),
    ("サ", "sa"),
    ("シ", "shi"),
    ("ス", "su"),
    ("セ", "se"),
    ("ソ", "so"),
    ("タ", "ta"),
    ("チ", "chi"),
    ("ツ", "tsu"),
    ("テ", "te"),
    ("ト", "to"),
    ("ナ", "na"),
    ("ニ", "ni"),
    ("ヌ", "nu"),
    ("ネ", "ne"),
    ("ノ", "no"),
    ("ハ", "ha"),
    ("ヒ", "hi"),
    ("フ", "fu"),
    ("ヘ", "he"),
    ("ホ", "ho"),
    ("マ", "ma"),
    ("ミ", "mi"),
    ("ム", "mu"),
    ("メ", "me"),
    ("モ", "mo"),
    ("ヤ", "ya"),
    ("ユ", "yu"),
    ("ヨ", "yo"),
    ("ラ", "ra"),
    ("リ", "ri"),
    ("ル", "ru"),
    ("レ", "re"),
    ("ロ", "ro"),
    ("ワ", "wa"),
    ("ヲ", "wo"),
    ("ン", "n"),
]

elements_mapping = [
    ("H\r\n\r\n1", "Hydrogen\r\n\r\nNonmetal"),
    ("He\r\n\r\n2", "Helium\r\n\r\nNoble Gas"),
    ("Li\r\n\r\n3", "Lithium\r\n\r\nAlkali Metal"),
    ("Be\r\n\r\n4", "Beryllium\r\n\r\nAlkaline Earth Metal"),
    ("B\r\n\r\n5", "Boron\r\n\r\nMetalloid"),
    ("C\r\n\r\n6", "Carbon\r\n\r\nNonmetal"),
    ("N\r\n\r\n7", "Nitrogen\r\n\r\nNonmetal"),
    ("O\r\n\r\n8", "Oxygen\r\n\r\nNonmetal"),
    ("F\r\n\r\n9", "Fluorine\r\n\r\nHalogen"),
    ("Ne\r\n\r\n10", "Neon\r\n\r\nNoble Gas"),
    ("Na\r\n\r\n11", "Sodium\r\n\r\nAlkali Metal"),
    ("Mg\r\n\r\n12", "Magnesium\r\n\r\nAlkaline Earth Metal"),
    ("Al\r\n\r\n13", "Aluminum\r\n\r\nPost-transition Metal"),
    ("Si\r\n\r\n14", "Silicon\r\n\r\nMetalloid"),
    ("P\r\n\r\n15", "Phosphorus\r\n\r\nNonmetal"),
    ("S\r\n\r\n16", "Sulfur\r\n\r\nNonmetal"),
    ("Cl\r\n\r\n17", "Chlorine\r\n\r\nHalogen"),
    ("Ar\r\n\r\n18", "Argon\r\n\r\nNoble Gas"),
    ("K\r\n\r\n19", "Potassium\r\n\r\nAlkali Metal"),
    ("Ca\r\n\r\n20", "Calcium\r\n\r\nAlkaline Earth Metal"),
    ("Sc\r\n\r\n21", "Scandium\r\n\r\nTransition Metal"),
    ("Ti\r\n\r\n22", "Titanium\r\n\r\nTransition Metal"),
    ("V\r\n\r\n23", "Vanadium\r\n\r\nTransition Metal"),
    ("Cr\r\n\r\n24", "Chromium\r\n\r\nTransition Metal"),
    ("Mn\r\n\r\n25", "Manganese\r\n\r\nTransition Metal"),
    ("Fe\r\n\r\n26", "Iron\r\n\r\nTransition Metal"),
    ("Co\r\n\r\n27", "Cobalt\r\n\r\nTransition Metal"),
    ("Ni\r\n\r\n28", "Nickel\r\n\r\nTransition Metal"),
    ("Cu\r\n\r\n29", "Copper\r\n\r\nTransition Metal"),
    ("Zn\r\n\r\n30", "Zinc\r\n\r\nTransition Metal"),
    ("Ga\r\n\r\n31", "Gallium\r\n\r\nPost-transition Metal"),
    ("Ge\r\n\r\n32", "Germanium\r\n\r\nMetalloid"),
    ("As\r\n\r\n33", "Arsenic\r\n\r\nMetalloid"),
    ("Se\r\n\r\n34", "Selenium\r\n\r\nNonmetal"),
    ("Br\r\n\r\n35", "Bromine\r\n\r\nHalogen"),
    ("Kr\r\n\r\n36", "Krypton\r\n\r\nNoble Gas"),
    ("Rb\r\n\r\n37", "Rubidium\r\n\r\nAlkali Metal"),
    ("Sr\r\n\r\n38", "Strontium\r\n\r\nAlkaline Earth Metal"),
    ("Y\r\n\r\n39", "Yttrium\r\n\r\nTransition Metal"),
    ("Zr\r\n\r\n40", "Zirconium\r\n\r\nTransition Metal"),
    ("Nb\r\n\r\n41", "Niobium\r\n\r\nTransition Metal"),
    ("Mo\r\n\r\n42", "Molybdenum\r\n\r\nTransition Metal"),
    ("Tc\r\n\r\n43", "Technetium\r\n\r\nTransition Metal"),
    ("Ru\r\n\r\n44", "Ruthenium\r\n\r\nTransition Metal"),
    ("Rh\r\n\r\n45", "Rhodium\r\n\r\nTransition Metal"),
    ("Pd\r\n\r\n46", "Palladium\r\n\r\nTransition Metal"),
    ("Ag\r\n\r\n47", "Silver\r\n\r\nTransition Metal"),
    ("Cd\r\n\r\n48", "Cadmium\r\n\r\nTransition Metal"),
    ("In\r\n\r\n49", "Indium\r\n\r\nPost-transition Metal"),
    ("Sn\r\n\r\n50", "Tin\r\n\r\nPost-transition Metal"),
    ("Sb\r\n\r\n51", "Antimony\r\n\r\nMetalloid"),
    ("Te\r\n\r\n52", "Tellurium\r\n\r\nMetalloid"),
    ("I\r\n\r\n53", "Iodine\r\n\r\nHalogen"),
    ("Xe\r\n\r\n54", "Xenon\r\n\r\nNoble Gas"),
    ("Cs\r\n\r\n55", "Cesium\r\n\r\nAlkali Metal"),
    ("Ba\r\n\r\n56", "Barium\r\n\r\nAlkaline Earth Metal"),
    ("La\r\n\r\n57", "Lanthanum\r\n\r\nLanthanide"),
    ("Ce\r\n\r\n58", "Cerium\r\n\r\nLanthanide"),
    ("Pr\r\n\r\n59", "Praseodymium\r\n\r\nLanthanide"),
    ("Nd\r\n\r\n60", "Neodymium\r\n\r\nLanthanide"),
    ("Pm\r\n\r\n61", "Promethium\r\n\r\nLanthanide"),
    ("Sm\r\n\r\n62", "Samarium\r\n\r\nLanthanide"),
    ("Eu\r\n\r\n63", "Europium\r\n\r\nLanthanide"),
    ("Gd\r\n\r\n64", "Gadolinium\r\n\r\nLanthanide"),
    ("Tb\r\n\r\n65", "Terbium\r\n\r\nLanthanide"),
    ("Dy\r\n\r\n66", "Dysprosium\r\n\r\nLanthanide"),
    ("Ho\r\n\r\n67", "Holmium\r\n\r\nLanthanide"),
    ("Er\r\n\r\n68", "Erbium\r\n\r\nLanthanide"),
    ("Tm\r\n\r\n69", "Thulium\r\n\r\nLanthanide"),
    ("Yb\r\n\r\n70", "Ytterbium\r\n\r\nLanthanide"),
    ("Lu\r\n\r\n71", "Lutetium\r\n\r\nLanthanide"),
    ("Hf\r\n\r\n72", "Hafnium\r\n\r\nTransition Metal"),
    ("Ta\r\n\r\n73", "Tantalum\r\n\r\nTransition Metal"),
    ("W\r\n\r\n74", "Tungsten\r\n\r\nTransition Metal"),
    ("Re\r\n\r\n75", "Rhenium\r\n\r\nTransition Metal"),
    ("Os\r\n\r\n76", "Osmium\r\n\r\nTransition Metal"),
    ("Ir\r\n\r\n77", "Iridium\r\n\r\nTransition Metal"),
    ("Pt\r\n\r\n78", "Platinum\r\n\r\nTransition Metal"),
    ("Au\r\n\r\n79", "Gold\r\n\r\nTransition Metal"),
    ("Hg\r\n\r\n80", "Mercury\r\n\r\nTransition Metal"),
    ("Tl\r\n\r\n81", "Thallium\r\n\r\nPost-transition Metal"),
    ("Pb\r\n\r\n82", "Lead\r\n\r\nPost-transition Metal"),
    ("Bi\r\n\r\n83", "Bismuth\r\n\r\nPost-transition Metal"),
    ("Po\r\n\r\n84", "Polonium\r\n\r\nMetalloid"),
    ("At\r\n\r\n85", "Astatine\r\n\r\nHalogen"),
    ("Rn\r\n\r\n86", "Radon\r\n\r\nNoble Gas"),
    ("Fr\r\n\r\n87", "Francium\r\n\r\nAlkali Metal"),
    ("Ra\r\n\r\n88", "Radium\r\n\r\nAlkaline Earth Metal"),
    ("Ac\r\n\r\n89", "Actinium\r\n\r\nActinide"),
    ("Th\r\n\r\n90", "Thorium\r\n\r\nActinide"),
    ("Pa\r\n\r\n91", "Protactinium\r\n\r\nActinide"),
    ("U\r\n\r\n92", "Uranium\r\n\r\nActinide"),
    ("Np\r\n\r\n93", "Neptunium\r\n\r\nActinide"),
    ("Pu\r\n\r\n94", "Plutonium\r\n\r\nActinide"),
    ("Am\r\n\r\n95", "Americium\r\n\r\nActinide"),
    ("Cm\r\n\r\n96", "Curium\r\n\r\nActinide"),
    ("Bk\r\n\r\n97", "Berkelium\r\n\r\nActinide"),
    ("Cf\r\n\r\n98", "Californium\r\n\r\nActinide"),
    ("Es\r\n\r\n99", "Einsteinium\r\n\r\nActinide"),
    ("Fm\r\n\r\n100", "Fermium\r\n\r\nActinide"),
    ("Md\r\n\r\n101", "Mendelevium\r\n\r\nActinide"),
    ("No\r\n\r\n102", "Nobelium\r\n\r\nActinide"),
    ("Lr\r\n\r\n103", "Lawrencium\r\n\r\nActinide"),
    ("Rf\r\n\r\n104", "Rutherfordium\r\n\r\nTransition Metal"),
    ("Db\r\n\r\n105", "Dubnium\r\n\r\nTransition Metal"),
    ("Sg\r\n\r\n106", "Seaborgium\r\n\r\nTransition Metal"),
    ("Bh\r\n\r\n107", "Bohrium\r\n\r\nTransition Metal"),
    ("Hs\r\n\r\n108", "Hassium\r\n\r\nTransition Metal"),
    ("Mt\r\n\r\n109", "Meitnerium\r\n\r\nUnknown"),
    ("Ds\r\n\r\n110", "Darmstadtium\r\n\r\nUnknown"),
    ("Rg\r\n\r\n111", "Roentgenium\r\n\r\nUnknown"),
    ("Cn\r\n\r\n112", "Copernicium\r\n\r\nUnknown"),
    ("Nh\r\n\r\n113", "Nihonium\r\n\r\nUnknown"),
    ("Fl\r\n\r\n114", "Flerovium\r\n\r\nUnknown"),
    ("Mc\r\n\r\n115", "Moscovium\r\n\r\nUnknown"),
    ("Lv\r\n\r\n116", "Livermorium\r\n\r\nUnknown"),
    ("Ts\r\n\r\n117", "Tennessine\r\n\r\nUnknown"),
    ("Og\r\n\r\n118", "Oganesson\r\n\r\nUnknown"),
]


def create_hiragana_deck(deck_id):
    cards = []
    for kana, romaji in hiragana_mapping:
        card = Card(front=kana, back=romaji, deck_id=deck_id)
        cards.append(card)
    return cards


def create_katakana_deck(deck_id):
    cards = []
    for kana, romaji in katakana_mapping:
        card = Card(front=kana, back=romaji, deck_id=deck_id)
        cards.append(card)
    return cards


def create_mixed_deck(deck_id):
    cards = []
    for kana, romaji in mixed_mapping:
        card = Card(front=kana, back=romaji, deck_id=deck_id)
        cards.append(card)
    return cards


def created_elements_deck(deck_id):
    cards = []
    for symbol, name in elements_mapping:
        card = Card(front=symbol, back=name, deck_id=deck_id)
        cards.append(card)
    return cards
