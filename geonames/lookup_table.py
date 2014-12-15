#!/usr/bin/python
# coding: utf8

"""
Library Geonames
================

* continent_code
* country_code
* feature_class
* feature_code
"""

continent_code = {
    'AF': 'Africa',
    'AS': 'Asia',
    'EU': 'Europe',
    'NA': 'North America',
    'OC': 'Oceania',
    'SA': 'South America',
    'AN': 'Antarctica',
}

country_code = {
    "BD":{
        "Country":"Bangladesh",
        "ISO":"BD",
        "Continent":"Asia"
    },
    "BE":{
        "Country":"Belgium",
        "ISO":"BE",
        "Continent":"Europe"
    },
    "BF":{
        "Country":"Burkina Faso",
        "ISO":"BF",
        "Continent":"Africa"
    },
    "BG":{
        "Country":"Bulgaria",
        "ISO":"BG",
        "Continent":"Europe"
    },
    "BA":{
        "Country":"Bosnia and Herzegovina",
        "ISO":"BA",
        "Continent":"Europe"
    },
    "BB":{
        "Country":"Barbados",
        "ISO":"BB",
        "Continent":"North America"
    },
    "WF":{
        "Country":"Wallis and Futuna",
        "ISO":"WF",
        "Continent":"Oceania"
    },
    "BL":{
        "Country":"Saint Barthelemy",
        "ISO":"BL",
        "Continent":"North America"
    },
    "BM":{
        "Country":"Bermuda",
        "ISO":"BM",
        "Continent":"North America"
    },
    "BN":{
        "Country":"Brunei",
        "ISO":"BN",
        "Continent":"Asia"
    },
    "BO":{
        "Country":"Bolivia",
        "ISO":"BO",
        "Continent":"South America"
    },
    "BH":{
        "Country":"Bahrain",
        "ISO":"BH",
        "Continent":"Asia"
    },
    "BI":{
        "Country":"Burundi",
        "ISO":"BI",
        "Continent":"Africa"
    },
    "BJ":{
        "Country":"Benin",
        "ISO":"BJ",
        "Continent":"Africa"
    },
    "BT":{
        "Country":"Bhutan",
        "ISO":"BT",
        "Continent":"Asia"
    },
    "JM":{
        "Country":"Jamaica",
        "ISO":"JM",
        "Continent":"North America"
    },
    "BV":{
        "Country":"Bouvet Island",
        "ISO":"BV",
        "Continent":"Antarctica"
    },
    "BW":{
        "Country":"Botswana",
        "ISO":"BW",
        "Continent":"Africa"
    },
    "WS":{
        "Country":"Samoa",
        "ISO":"WS",
        "Continent":"Oceania"
    },
    "BQ":{
        "Country":"Bonaire, Saint Eustatius and Saba ",
        "ISO":"BQ",
        "Continent":"North America"
    },
    "BR":{
        "Country":"Brazil",
        "ISO":"BR",
        "Continent":"South America"
    },
    "BS":{
        "Country":"Bahamas",
        "ISO":"BS",
        "Continent":"North America"
    },
    "JE":{
        "Country":"Jersey",
        "ISO":"JE",
        "Continent":"Europe"
    },
    "BY":{
        "Country":"Belarus",
        "ISO":"BY",
        "Continent":"Europe"
    },
    "BZ":{
        "Country":"Belize",
        "ISO":"BZ",
        "Continent":"North America"
    },
    "RU":{
        "Country":"Russia",
        "ISO":"RU",
        "Continent":"Europe"
    },
    "RW":{
        "Country":"Rwanda",
        "ISO":"RW",
        "Continent":"Africa"
    },
    "RS":{
        "Country":"Serbia",
        "ISO":"RS",
        "Continent":"Europe"
    },
    "TL":{
        "Country":"East Timor",
        "ISO":"TL",
        "Continent":"Oceania"
    },
    "RE":{
        "Country":"Reunion",
        "ISO":"RE",
        "Continent":"Africa"
    },
    "TM":{
        "Country":"Turkmenistan",
        "ISO":"TM",
        "Continent":"Asia"
    },
    "TJ":{
        "Country":"Tajikistan",
        "ISO":"TJ",
        "Continent":"Asia"
    },
    "RO":{
        "Country":"Romania",
        "ISO":"RO",
        "Continent":"Europe"
    },
    "TK":{
        "Country":"Tokelau",
        "ISO":"TK",
        "Continent":"Oceania"
    },
    "GW":{
        "Country":"Guinea-Bissau",
        "ISO":"GW",
        "Continent":"Africa"
    },
    "GU":{
        "Country":"Guam",
        "ISO":"GU",
        "Continent":"Oceania"
    },
    "GT":{
        "Country":"Guatemala",
        "ISO":"GT",
        "Continent":"North America"
    },
    "GS":{
        "Country":"South Georgia and the South Sandwich Islands",
        "ISO":"GS",
        "Continent":"Antarctica"
    },
    "GR":{
        "Country":"Greece",
        "ISO":"GR",
        "Continent":"Europe"
    },
    "GQ":{
        "Country":"Equatorial Guinea",
        "ISO":"GQ",
        "Continent":"Africa"
    },
    "GP":{
        "Country":"Guadeloupe",
        "ISO":"GP",
        "Continent":"North America"
    },
    "JP":{
        "Country":"Japan",
        "ISO":"JP",
        "Continent":"Asia"
    },
    "GY":{
        "Country":"Guyana",
        "ISO":"GY",
        "Continent":"South America"
    },
    "GG":{
        "Country":"Guernsey",
        "ISO":"GG",
        "Continent":"Europe"
    },
    "GF":{
        "Country":"French Guiana",
        "ISO":"GF",
        "Continent":"South America"
    },
    "GE":{
        "Country":"Georgia",
        "ISO":"GE",
        "Continent":"Asia"
    },
    "GD":{
        "Country":"Grenada",
        "ISO":"GD",
        "Continent":"North America"
    },
    "GB":{
        "Country":"United Kingdom",
        "ISO":"GB",
        "Continent":"Europe"
    },
    "GA":{
        "Country":"Gabon",
        "ISO":"GA",
        "Continent":"Africa"
    },
    "SV":{
        "Country":"El Salvador",
        "ISO":"SV",
        "Continent":"North America"
    },
    "GN":{
        "Country":"Guinea",
        "ISO":"GN",
        "Continent":"Africa"
    },
    "GM":{
        "Country":"Gambia",
        "ISO":"GM",
        "Continent":"Africa"
    },
    "GL":{
        "Country":"Greenland",
        "ISO":"GL",
        "Continent":"North America"
    },
    "GI":{
        "Country":"Gibraltar",
        "ISO":"GI",
        "Continent":"Europe"
    },
    "GH":{
        "Country":"Ghana",
        "ISO":"GH",
        "Continent":"Africa"
    },
    "OM":{
        "Country":"Oman",
        "ISO":"OM",
        "Continent":"Asia"
    },
    "TN":{
        "Country":"Tunisia",
        "ISO":"TN",
        "Continent":"Africa"
    },
    "JO":{
        "Country":"Jordan",
        "ISO":"JO",
        "Continent":"Asia"
    },
    "HR":{
        "Country":"Croatia",
        "ISO":"HR",
        "Continent":"Europe"
    },
    "HT":{
        "Country":"Haiti",
        "ISO":"HT",
        "Continent":"North America"
    },
    "HU":{
        "Country":"Hungary",
        "ISO":"HU",
        "Continent":"Europe"
    },
    "HK":{
        "Country":"Hong Kong",
        "ISO":"HK",
        "Continent":"Asia"
    },
    "HN":{
        "Country":"Honduras",
        "ISO":"HN",
        "Continent":"North America"
    },
    "HM":{
        "Country":"Heard Island and McDonald Islands",
        "ISO":"HM",
        "Continent":"Antarctica"
    },
    "VE":{
        "Country":"Venezuela",
        "ISO":"VE",
        "Continent":"South America"
    },
    "PR":{
        "Country":"Puerto Rico",
        "ISO":"PR",
        "Continent":"North America"
    },
    "PS":{
        "Country":"Palestinian Territory",
        "ISO":"PS",
        "Continent":"Asia"
    },
    "PW":{
        "Country":"Palau",
        "ISO":"PW",
        "Continent":"Oceania"
    },
    "PT":{
        "Country":"Portugal",
        "ISO":"PT",
        "Continent":"Europe"
    },
    "SJ":{
        "Country":"Svalbard and Jan Mayen",
        "ISO":"SJ",
        "Continent":"Europe"
    },
    "PY":{
        "Country":"Paraguay",
        "ISO":"PY",
        "Continent":"South America"
    },
    "IQ":{
        "Country":"Iraq",
        "ISO":"IQ",
        "Continent":"Asia"
    },
    "PA":{
        "Country":"Panama",
        "ISO":"PA",
        "Continent":"North America"
    },
    "PF":{
        "Country":"French Polynesia",
        "ISO":"PF",
        "Continent":"Oceania"
    },
    "PG":{
        "Country":"Papua New Guinea",
        "ISO":"PG",
        "Continent":"Oceania"
    },
    "PE":{
        "Country":"Peru",
        "ISO":"PE",
        "Continent":"South America"
    },
    "PK":{
        "Country":"Pakistan",
        "ISO":"PK",
        "Continent":"Asia"
    },
    "PH":{
        "Country":"Philippines",
        "ISO":"PH",
        "Continent":"Asia"
    },
    "PN":{
        "Country":"Pitcairn",
        "ISO":"PN",
        "Continent":"Oceania"
    },
    "PL":{
        "Country":"Poland",
        "ISO":"PL",
        "Continent":"Europe"
    },
    "PM":{
        "Country":"Saint Pierre and Miquelon",
        "ISO":"PM",
        "Continent":"North America"
    },
    "ZM":{
        "Country":"Zambia",
        "ISO":"ZM",
        "Continent":"Africa"
    },
    "EH":{
        "Country":"Western Sahara",
        "ISO":"EH",
        "Continent":"Africa"
    },
    "EE":{
        "Country":"Estonia",
        "ISO":"EE",
        "Continent":"Europe"
    },
    "EG":{
        "Country":"Egypt",
        "ISO":"EG",
        "Continent":"Africa"
    },
    "ZA":{
        "Country":"South Africa",
        "ISO":"ZA",
        "Continent":"Africa"
    },
    "EC":{
        "Country":"Ecuador",
        "ISO":"EC",
        "Continent":"South America"
    },
    "IT":{
        "Country":"Italy",
        "ISO":"IT",
        "Continent":"Europe"
    },
    "VN":{
        "Country":"Vietnam",
        "ISO":"VN",
        "Continent":"Asia"
    },
    "SB":{
        "Country":"Solomon Islands",
        "ISO":"SB",
        "Continent":"Oceania"
    },
    "ET":{
        "Country":"Ethiopia",
        "ISO":"ET",
        "Continent":"Africa"
    },
    "SO":{
        "Country":"Somalia",
        "ISO":"SO",
        "Continent":"Africa"
    },
    "ZW":{
        "Country":"Zimbabwe",
        "ISO":"ZW",
        "Continent":"Africa"
    },
    "SA":{
        "Country":"Saudi Arabia",
        "ISO":"SA",
        "Continent":"Asia"
    },
    "ES":{
        "Country":"Spain",
        "ISO":"ES",
        "Continent":"Europe"
    },
    "ER":{
        "Country":"Eritrea",
        "ISO":"ER",
        "Continent":"Africa"
    },
    "ME":{
        "Country":"Montenegro",
        "ISO":"ME",
        "Continent":"Europe"
    },
    "MD":{
        "Country":"Moldova",
        "ISO":"MD",
        "Continent":"Europe"
    },
    "MG":{
        "Country":"Madagascar",
        "ISO":"MG",
        "Continent":"Africa"
    },
    "MF":{
        "Country":"Saint Martin",
        "ISO":"MF",
        "Continent":"North America"
    },
    "MA":{
        "Country":"Morocco",
        "ISO":"MA",
        "Continent":"Africa"
    },
    "MC":{
        "Country":"Monaco",
        "ISO":"MC",
        "Continent":"Europe"
    },
    "UZ":{
        "Country":"Uzbekistan",
        "ISO":"UZ",
        "Continent":"Asia"
    },
    "MM":{
        "Country":"Myanmar",
        "ISO":"MM",
        "Continent":"Asia"
    },
    "ML":{
        "Country":"Mali",
        "ISO":"ML",
        "Continent":"Africa"
    },
    "MO":{
        "Country":"Macao",
        "ISO":"MO",
        "Continent":"Asia"
    },
    "MN":{
        "Country":"Mongolia",
        "ISO":"MN",
        "Continent":"Asia"
    },
    "MH":{
        "Country":"Marshall Islands",
        "ISO":"MH",
        "Continent":"Oceania"
    },
    "MK":{
        "Country":"Macedonia",
        "ISO":"MK",
        "Continent":"Europe"
    },
    "MU":{
        "Country":"Mauritius",
        "ISO":"MU",
        "Continent":"Africa"
    },
    "MT":{
        "Country":"Malta",
        "ISO":"MT",
        "Continent":"Europe"
    },
    "MW":{
        "Country":"Malawi",
        "ISO":"MW",
        "Continent":"Africa"
    },
    "MV":{
        "Country":"Maldives",
        "ISO":"MV",
        "Continent":"Asia"
    },
    "MQ":{
        "Country":"Martinique",
        "ISO":"MQ",
        "Continent":"North America"
    },
    "MP":{
        "Country":"Northern Mariana Islands",
        "ISO":"MP",
        "Continent":"Oceania"
    },
    "MS":{
        "Country":"Montserrat",
        "ISO":"MS",
        "Continent":"North America"
    },
    "MR":{
        "Country":"Mauritania",
        "ISO":"MR",
        "Continent":"Africa"
    },
    "IM":{
        "Country":"Isle of Man",
        "ISO":"IM",
        "Continent":"Europe"
    },
    "UG":{
        "Country":"Uganda",
        "ISO":"UG",
        "Continent":"Africa"
    },
    "TZ":{
        "Country":"Tanzania",
        "ISO":"TZ",
        "Continent":"Africa"
    },
    "MY":{
        "Country":"Malaysia",
        "ISO":"MY",
        "Continent":"Asia"
    },
    "MX":{
        "Country":"Mexico",
        "ISO":"MX",
        "Continent":"North America"
    },
    "IL":{
        "Country":"Israel",
        "ISO":"IL",
        "Continent":"Asia"
    },
    "FR":{
        "Country":"France",
        "ISO":"FR",
        "Continent":"Europe"
    },
    "IO":{
        "Country":"British Indian Ocean Territory",
        "ISO":"IO",
        "Continent":"Asia"
    },
    "SH":{
        "Country":"Saint Helena",
        "ISO":"SH",
        "Continent":"Africa"
    },
    "FI":{
        "Country":"Finland",
        "ISO":"FI",
        "Continent":"Europe"
    },
    "FJ":{
        "Country":"Fiji",
        "ISO":"FJ",
        "Continent":"Oceania"
    },
    "FK":{
        "Country":"Falkland Islands",
        "ISO":"FK",
        "Continent":"South America"
    },
    "FM":{
        "Country":"Micronesia",
        "ISO":"FM",
        "Continent":"Oceania"
    },
    "FO":{
        "Country":"Faroe Islands",
        "ISO":"FO",
        "Continent":"Europe"
    },
    "NI":{
        "Country":"Nicaragua",
        "ISO":"NI",
        "Continent":"North America"
    },
    "NL":{
        "Country":"Netherlands",
        "ISO":"NL",
        "Continent":"Europe"
    },
    "NO":{
        "Country":"Norway",
        "ISO":"NO",
        "Continent":"Europe"
    },
    "NA":{
        "Country":"Namibia",
        "ISO":"NA",
        "Continent":"Africa"
    },
    "VU":{
        "Country":"Vanuatu",
        "ISO":"VU",
        "Continent":"Oceania"
    },
    "NC":{
        "Country":"New Caledonia",
        "ISO":"NC",
        "Continent":"Oceania"
    },
    "NE":{
        "Country":"Niger",
        "ISO":"NE",
        "Continent":"Africa"
    },
    "NF":{
        "Country":"Norfolk Island",
        "ISO":"NF",
        "Continent":"Oceania"
    },
    "NG":{
        "Country":"Nigeria",
        "ISO":"NG",
        "Continent":"Africa"
    },
    "NZ":{
        "Country":"New Zealand",
        "ISO":"NZ",
        "Continent":"Oceania"
    },
    "NP":{
        "Country":"Nepal",
        "ISO":"NP",
        "Continent":"Asia"
    },
    "NR":{
        "Country":"Nauru",
        "ISO":"NR",
        "Continent":"Oceania"
    },
    "NU":{
        "Country":"Niue",
        "ISO":"NU",
        "Continent":"Oceania"
    },
    "CK":{
        "Country":"Cook Islands",
        "ISO":"CK",
        "Continent":"Oceania"
    },
    "XK":{
        "Country":"Kosovo",
        "ISO":"XK",
        "Continent":"Europe"
    },
    "CI":{
        "Country":"Ivory Coast",
        "ISO":"CI",
        "Continent":"Africa"
    },
    "CH":{
        "Country":"Switzerland",
        "ISO":"CH",
        "Continent":"Europe"
    },
    "CO":{
        "Country":"Colombia",
        "ISO":"CO",
        "Continent":"South America"
    },
    "CN":{
        "Country":"China",
        "ISO":"CN",
        "Continent":"Asia"
    },
    "CM":{
        "Country":"Cameroon",
        "ISO":"CM",
        "Continent":"Africa"
    },
    "CL":{
        "Country":"Chile",
        "ISO":"CL",
        "Continent":"South America"
    },
    "CC":{
        "Country":"Cocos Islands",
        "ISO":"CC",
        "Continent":"Asia"
    },
    "CA":{
        "Country":"Canada",
        "ISO":"CA",
        "Continent":"North America"
    },
    "CG":{
        "Country":"Republic of the Congo",
        "ISO":"CG",
        "Continent":"Africa"
    },
    "CF":{
        "Country":"Central African Republic",
        "ISO":"CF",
        "Continent":"Africa"
    },
    "CD":{
        "Country":"Democratic Republic of the Congo",
        "ISO":"CD",
        "Continent":"Africa"
    },
    "CZ":{
        "Country":"Czech Republic",
        "ISO":"CZ",
        "Continent":"Europe"
    },
    "CY":{
        "Country":"Cyprus",
        "ISO":"CY",
        "Continent":"Europe"
    },
    "CX":{
        "Country":"Christmas Island",
        "ISO":"CX",
        "Continent":"Asia"
    },
    "CS":{
        "Country":"Serbia and Montenegro",
        "ISO":"CS",
        "Continent":"Europe"
    },
    "CR":{
        "Country":"Costa Rica",
        "ISO":"CR",
        "Continent":"North America"
    },
    "CW":{
        "Country":"Curacao",
        "ISO":"CW",
        "Continent":"North America"
    },
    "CV":{
        "Country":"Cape Verde",
        "ISO":"CV",
        "Continent":"Africa"
    },
    "CU":{
        "Country":"Cuba",
        "ISO":"CU",
        "Continent":"North America"
    },
    "SZ":{
        "Country":"Swaziland",
        "ISO":"SZ",
        "Continent":"Africa"
    },
    "SY":{
        "Country":"Syria",
        "ISO":"SY",
        "Continent":"Asia"
    },
    "SX":{
        "Country":"Sint Maarten",
        "ISO":"SX",
        "Continent":"North America"
    },
    "KG":{
        "Country":"Kyrgyzstan",
        "ISO":"KG",
        "Continent":"Asia"
    },
    "KE":{
        "Country":"Kenya",
        "ISO":"KE",
        "Continent":"Africa"
    },
    "SS":{
        "Country":"South Sudan",
        "ISO":"SS",
        "Continent":"Africa"
    },
    "SR":{
        "Country":"Suriname",
        "ISO":"SR",
        "Continent":"South America"
    },
    "KI":{
        "Country":"Kiribati",
        "ISO":"KI",
        "Continent":"Oceania"
    },
    "KH":{
        "Country":"Cambodia",
        "ISO":"KH",
        "Continent":"Asia"
    },
    "KN":{
        "Country":"Saint Kitts and Nevis",
        "ISO":"KN",
        "Continent":"North America"
    },
    "KM":{
        "Country":"Comoros",
        "ISO":"KM",
        "Continent":"Africa"
    },
    "ST":{
        "Country":"Sao Tome and Principe",
        "ISO":"ST",
        "Continent":"Africa"
    },
    "SK":{
        "Country":"Slovakia",
        "ISO":"SK",
        "Continent":"Europe"
    },
    "KR":{
        "Country":"South Korea",
        "ISO":"KR",
        "Continent":"Asia"
    },
    "SI":{
        "Country":"Slovenia",
        "ISO":"SI",
        "Continent":"Europe"
    },
    "KP":{
        "Country":"North Korea",
        "ISO":"KP",
        "Continent":"Asia"
    },
    "KW":{
        "Country":"Kuwait",
        "ISO":"KW",
        "Continent":"Asia"
    },
    "SN":{
        "Country":"Senegal",
        "ISO":"SN",
        "Continent":"Africa"
    },
    "SM":{
        "Country":"San Marino",
        "ISO":"SM",
        "Continent":"Europe"
    },
    "SL":{
        "Country":"Sierra Leone",
        "ISO":"SL",
        "Continent":"Africa"
    },
    "SC":{
        "Country":"Seychelles",
        "ISO":"SC",
        "Continent":"Africa"
    },
    "KZ":{
        "Country":"Kazakhstan",
        "ISO":"KZ",
        "Continent":"Asia"
    },
    "KY":{
        "Country":"Cayman Islands",
        "ISO":"KY",
        "Continent":"North America"
    },
    "SG":{
        "Country":"Singapore",
        "ISO":"SG",
        "Continent":"Asia"
    },
    "SE":{
        "Country":"Sweden",
        "ISO":"SE",
        "Continent":"Europe"
    },
    "SD":{
        "Country":"Sudan",
        "ISO":"SD",
        "Continent":"Africa"
    },
    "DO":{
        "Country":"Dominican Republic",
        "ISO":"DO",
        "Continent":"North America"
    },
    "DM":{
        "Country":"Dominica",
        "ISO":"DM",
        "Continent":"North America"
    },
    "DJ":{
        "Country":"Djibouti",
        "ISO":"DJ",
        "Continent":"Africa"
    },
    "DK":{
        "Country":"Denmark",
        "ISO":"DK",
        "Continent":"Europe"
    },
    "VG":{
        "Country":"British Virgin Islands",
        "ISO":"VG",
        "Continent":"North America"
    },
    "DE":{
        "Country":"Germany",
        "ISO":"DE",
        "Continent":"Europe"
    },
    "YE":{
        "Country":"Yemen",
        "ISO":"YE",
        "Continent":"Asia"
    },
    "DZ":{
        "Country":"Algeria",
        "ISO":"DZ",
        "Continent":"Africa"
    },
    "US":{
        "Country":"United States",
        "ISO":"US",
        "Continent":"North America"
    },
    "UY":{
        "Country":"Uruguay",
        "ISO":"UY",
        "Continent":"South America"
    },
    "YT":{
        "Country":"Mayotte",
        "ISO":"YT",
        "Continent":"Africa"
    },
    "UM":{
        "Country":"United States Minor Outlying Islands",
        "ISO":"UM",
        "Continent":"Oceania"
    },
    "LB":{
        "Country":"Lebanon",
        "ISO":"LB",
        "Continent":"Asia"
    },
    "LC":{
        "Country":"Saint Lucia",
        "ISO":"LC",
        "Continent":"North America"
    },
    "LA":{
        "Country":"Laos",
        "ISO":"LA",
        "Continent":"Asia"
    },
    "TV":{
        "Country":"Tuvalu",
        "ISO":"TV",
        "Continent":"Oceania"
    },
    "TW":{
        "Country":"Taiwan",
        "ISO":"TW",
        "Continent":"Asia"
    },
    "TT":{
        "Country":"Trinidad and Tobago",
        "ISO":"TT",
        "Continent":"North America"
    },
    "TR":{
        "Country":"Turkey",
        "ISO":"TR",
        "Continent":"Asia"
    },
    "LK":{
        "Country":"Sri Lanka",
        "ISO":"LK",
        "Continent":"Asia"
    },
    "LI":{
        "Country":"Liechtenstein",
        "ISO":"LI",
        "Continent":"Europe"
    },
    "LV":{
        "Country":"Latvia",
        "ISO":"LV",
        "Continent":"Europe"
    },
    "TO":{
        "Country":"Tonga",
        "ISO":"TO",
        "Continent":"Oceania"
    },
    "LT":{
        "Country":"Lithuania",
        "ISO":"LT",
        "Continent":"Europe"
    },
    "LU":{
        "Country":"Luxembourg",
        "ISO":"LU",
        "Continent":"Europe"
    },
    "LR":{
        "Country":"Liberia",
        "ISO":"LR",
        "Continent":"Africa"
    },
    "LS":{
        "Country":"Lesotho",
        "ISO":"LS",
        "Continent":"Africa"
    },
    "TH":{
        "Country":"Thailand",
        "ISO":"TH",
        "Continent":"Asia"
    },
    "TF":{
        "Country":"French Southern Territories",
        "ISO":"TF",
        "Continent":"Antarctica"
    },
    "TG":{
        "Country":"Togo",
        "ISO":"TG",
        "Continent":"Africa"
    },
    "TD":{
        "Country":"Chad",
        "ISO":"TD",
        "Continent":"Africa"
    },
    "TC":{
        "Country":"Turks and Caicos Islands",
        "ISO":"TC",
        "Continent":"North America"
    },
    "LY":{
        "Country":"Libya",
        "ISO":"LY",
        "Continent":"Africa"
    },
    "VA":{
        "Country":"Vatican",
        "ISO":"VA",
        "Continent":"Europe"
    },
    "VC":{
        "Country":"Saint Vincent and the Grenadines",
        "ISO":"VC",
        "Continent":"North America"
    },
    "AE":{
        "Country":"United Arab Emirates",
        "ISO":"AE",
        "Continent":"Asia"
    },
    "AD":{
        "Country":"Andorra",
        "ISO":"AD",
        "Continent":"Europe"
    },
    "AG":{
        "Country":"Antigua and Barbuda",
        "ISO":"AG",
        "Continent":"North America"
    },
    "AF":{
        "Country":"Afghanistan",
        "ISO":"AF",
        "Continent":"Asia"
    },
    "AI":{
        "Country":"Anguilla",
        "ISO":"AI",
        "Continent":"North America"
    },
    "VI":{
        "Country":"U.S. Virgin Islands",
        "ISO":"VI",
        "Continent":"North America"
    },
    "IS":{
        "Country":"Iceland",
        "ISO":"IS",
        "Continent":"Europe"
    },
    "IR":{
        "Country":"Iran",
        "ISO":"IR",
        "Continent":"Asia"
    },
    "AM":{
        "Country":"Armenia",
        "ISO":"AM",
        "Continent":"Asia"
    },
    "AL":{
        "Country":"Albania",
        "ISO":"AL",
        "Continent":"Europe"
    },
    "AO":{
        "Country":"Angola",
        "ISO":"AO",
        "Continent":"Africa"
    },
    "AN":{
        "Country":"Netherlands Antilles",
        "ISO":"AN",
        "Continent":"North America"
    },
    "AQ":{
        "Country":"Antarctica",
        "ISO":"AQ",
        "Continent":"Antarctica"
    },
    "AS":{
        "Country":"American Samoa",
        "ISO":"AS",
        "Continent":"Oceania"
    },
    "AR":{
        "Country":"Argentina",
        "ISO":"AR",
        "Continent":"South America"
    },
    "AU":{
        "Country":"Australia",
        "ISO":"AU",
        "Continent":"Oceania"
    },
    "AT":{
        "Country":"Austria",
        "ISO":"AT",
        "Continent":"Europe"
    },
    "AW":{
        "Country":"Aruba",
        "ISO":"AW",
        "Continent":"North America"
    },
    "IN":{
        "Country":"India",
        "ISO":"IN",
        "Continent":"Asia"
    },
    "AX":{
        "Country":"Aland Islands",
        "ISO":"AX",
        "Continent":"Europe"
    },
    "AZ":{
        "Country":"Azerbaijan",
        "ISO":"AZ",
        "Continent":"Asia"
    },
    "IE":{
        "Country":"Ireland",
        "ISO":"IE",
        "Continent":"Europe"
    },
    "ID":{
        "Country":"Indonesia",
        "ISO":"ID",
        "Continent":"Asia"
    },
    "UA":{
        "Country":"Ukraine",
        "ISO":"UA",
        "Continent":"Europe"
    },
    "QA":{
        "Country":"Qatar",
        "ISO":"QA",
        "Continent":"Asia"
    },
    "MZ":{
        "Country":"Mozambique",
        "ISO":"MZ",
        "Continent":"Africa"
    }
}


feature_class = {
    'A': 'Administrative Boundary',
    'H': 'Hydrographic',
    'L': 'Area',
    'P': 'Populated Place',
    'R': 'Road / Railroad',
    'S': 'Spot',
    'T': 'Hypsographic',
    'U': 'Undersea',
    'V': 'Vegetation',
}

feature_code = {
    "SHSE":{
        "description":"a building for storing goods, especially provisions",
        "code":"SHSE",
        "class":"Spot",
        "name":"storehouse"
    },
    "RYD":{
        "description":"a system of tracks used for the making up of trains, and switching and storing freight cars",
        "code":"RYD",
        "class":"Road / Railroad",
        "name":"railroad yard"
    },
    "CSNO":{
        "description":"a building used for entertainment, especially gambling",
        "code":"CSNO",
        "class":"Spot",
        "name":"casino"
    },
    "SHSU":{
        "description":"hazards to surface navigation composed of unconsolidated material",
        "code":"SHSU",
        "class":"Undersea",
        "name":"shoals"
    },
    "WLL":{
        "description":"a cylindrical hole, pit, or tunnel drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface",
        "code":"WLL",
        "class":"Hydrographic",
        "name":"well"
    },
    "CRKT":{
        "description":"a meandering channel in a coastal wetland subject to bi-directional tidal currents",
        "code":"CRKT",
        "class":"Hydrographic",
        "name":"tidal creek(s)"
    },
    "MSSN":{
        "description":"a place characterized by dwellings, school, church, hospital and other facilities operated by a religious group for the purpose of providing charitable services and to propagate religion",
        "code":"MSSN",
        "class":"Spot",
        "name":"mission"
    },
    "PRNQ":{
        "description":"",
        "code":"PRNQ",
        "class":"Spot",
        "name":"abandoned prison"
    },
    "STKR":{
        "description":"a route taken by livestock herds",
        "code":"STKR",
        "class":"Road / Railroad",
        "name":"stock route"
    },
    "RDSU":{
        "description":"long narrow elevations with steep sides",
        "code":"RDSU",
        "class":"Undersea",
        "name":"ridges"
    },
    "PRNJ":{
        "description":"a facility for confining, training, and reforming young law offenders",
        "code":"PRNJ",
        "class":"Spot",
        "name":"reformatory"
    },
    "PPLA2":{
        "description":"",
        "code":"PPLA2",
        "class":"Populated Place",
        "name":"seat of a second-order administrative division"
    },
    "PPLA3":{
        "description":"",
        "code":"PPLA3",
        "class":"Populated Place",
        "name":"seat of a third-order administrative division"
    },
    "PPLA4":{
        "description":"",
        "code":"PPLA4",
        "class":"Populated Place",
        "name":"seat of a fourth-order administrative division"
    },
    "VAL":{
        "description":"an elongated depression usually traversed by a stream",
        "code":"VAL",
        "class":"Hypsographic",
        "name":"valley"
    },
    "LKOI":{
        "description":"",
        "code":"LKOI",
        "class":"Hydrographic",
        "name":"intermittent oxbow lake"
    },
    "COVE":{
        "description":"a small coastal indentation, smaller than a bay",
        "code":"COVE",
        "class":"Hydrographic",
        "name":"cove(s)"
    },
    "MRSHN":{
        "description":"a flat area, subject to periodic salt water inundation, dominated by grassy salt-tolerant plants",
        "code":"MRSHN",
        "class":"Hydrographic",
        "name":"salt marsh"
    },
    "BUTE":{
        "description":"a small, isolated, usually flat-topped hill with steep sides",
        "code":"BUTE",
        "class":"Hypsographic",
        "name":"butte(s)"
    },
    "SYSI":{
        "description":"a network of ditches and one or more of the following elements: water supply, reservoir, canal, pump, well, drain, etc.",
        "code":"SYSI",
        "class":"Hydrographic",
        "name":"irrigation system"
    },
    "MFGQ":{
        "description":"",
        "code":"MFGQ",
        "class":"Spot",
        "name":"abandoned factory"
    },
    "SPUR":{
        "description":"a subordinate ridge projecting outward from a hill, mountain or other elevation",
        "code":"SPUR",
        "class":"Hypsographic",
        "name":"spur(s)"
    },
    "MAR":{
        "description":"a harbor facility for small boats, yachts, etc.",
        "code":"MAR",
        "class":"Spot",
        "name":"marina"
    },
    "PTS":{
        "description":"tapering pieces of land projecting into a body of water, less prominent than a cape",
        "code":"PTS",
        "class":"Hypsographic",
        "name":"points"
    },
    "RUIN":{
        "description":"a destroyed or decayed structure which is no longer functional",
        "code":"RUIN",
        "class":"Spot",
        "name":"ruin(s)"
    },
    "PSTC":{
        "description":"a building at an international boundary where customs and duties are paid on goods",
        "code":"PSTC",
        "class":"Spot",
        "name":"customs post"
    },
    "PSTB":{
        "description":"a post or station at an international boundary for the regulation of movement of people and goods",
        "code":"PSTB",
        "class":"Spot",
        "name":"border post"
    },
    "OVF":{
        "description":"an area of breaking waves caused by the meeting of currents or by waves moving against the current",
        "code":"OVF",
        "class":"Hydrographic",
        "name":"overfalls"
    },
    "SPLY":{
        "description":"a passage or outlet through which surplus water flows over, around or through a dam",
        "code":"SPLY",
        "class":"Spot",
        "name":"spillway"
    },
    "PLATX":{
        "description":"",
        "code":"PLATX",
        "class":"Hypsographic",
        "name":"section of plateau"
    },
    "CMN":{
        "description":"a park or pasture for community use",
        "code":"CMN",
        "class":"Area",
        "name":"common"
    },
    "ERG":{
        "description":"an extensive tract of shifting sand and sand dunes",
        "code":"ERG",
        "class":"Hypsographic",
        "name":"sandy desert"
    },
    "PCL":{
        "description":"",
        "code":"PCL",
        "class":"Administrative Boundary",
        "name":"political entity"
    },
    "TNKD":{
        "description":"a small artificial pond used for immersing cattle in chemically treated water for disease control",
        "code":"TNKD",
        "class":"Spot",
        "name":"cattle dipping tank"
    },
    "CRTR":{
        "description":"a generally circular saucer or bowl-shaped depression caused by volcanic or meteorite explosive action",
        "code":"CRTR",
        "class":"Hypsographic",
        "name":"crater(s)"
    },
    "CMPL":{
        "description":"a camp used by loggers",
        "code":"CMPL",
        "class":"Spot",
        "name":"logging camp"
    },
    "CMP":{
        "description":"a site occupied by tents, huts, or other shelters for temporary use",
        "code":"CMP",
        "class":"Spot",
        "name":"camp(s)"
    },
    "PCLS":{
        "description":"",
        "code":"PCLS",
        "class":"Administrative Boundary",
        "name":"semi-independent political entity"
    },
    "VLC":{
        "description":"a conical elevation composed of volcanic materials with a crater at the top",
        "code":"VLC",
        "class":"Hypsographic",
        "name":"volcano"
    },
    "DEVH":{
        "description":"a tract of land on which many houses of similar design are built according to a development plan",
        "code":"DEVH",
        "class":"Area",
        "name":"housing development"
    },
    "HUT":{
        "description":"a small primitive house",
        "code":"HUT",
        "class":"Spot",
        "name":"hut"
    },
    "PCLI":{
        "description":"",
        "code":"PCLI",
        "class":"Administrative Boundary",
        "name":"independent political entity"
    },
    "PCLH":{
        "description":"a former political entity",
        "code":"PCLH",
        "class":"Administrative Boundary",
        "name":"historical political entity"
    },
    "PCLF":{
        "description":"",
        "code":"PCLF",
        "class":"Administrative Boundary",
        "name":"freely associated state"
    },
    "LCTY":{
        "description":"a minor area or place of unspecified or mixed character and indefinite boundaries",
        "code":"LCTY",
        "class":"Area",
        "name":"locality"
    },
    "PCLD":{
        "description":"",
        "code":"PCLD",
        "class":"Administrative Boundary",
        "name":"dependent political entity"
    },
    "ZN":{
        "description":"",
        "code":"ZN",
        "class":"Administrative Boundary",
        "name":"zone"
    },
    "MSTY":{
        "description":"a building and grounds where a community of monks lives in seclusion",
        "code":"MSTY",
        "class":"Spot",
        "name":"monastery"
    },
    "STBL":{
        "description":"a building for the shelter and feeding of farm animals, especially horses",
        "code":"STBL",
        "class":"Spot",
        "name":"stable"
    },
    "RNGA":{
        "description":"a tract of land used for artillery firing practice",
        "code":"RNGA",
        "class":"Area",
        "name":"artillery range"
    },
    "KNSU":{
        "description":"elevations rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summits",
        "code":"KNSU",
        "class":"Undersea",
        "name":"knolls"
    },
    "RLGR":{
        "description":"a place of temporary seclusion, especially for religious groups",
        "code":"RLGR",
        "class":"Spot",
        "name":"retreat"
    },
    "BKSU":{
        "description":"elevations, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation",
        "code":"BKSU",
        "class":"Undersea",
        "name":"banks"
    },
    "PNDNI":{
        "description":"",
        "code":"PNDNI",
        "class":"Hydrographic",
        "name":"intermittent salt pond(s)"
    },
    "BDLU":{
        "description":"a region adjacent to a continent, normally occupied by or bordering a shelf, that is highly irregular with depths well in excess of those typical of a shelf",
        "code":"BDLU",
        "class":"Undersea",
        "name":"borderland"
    },
    "BLOW":{
        "description":"a small depression in sandy terrain, caused by wind erosion",
        "code":"BLOW",
        "class":"Hypsographic",
        "name":"blowout(s)"
    },
    "WTRC":{
        "description":"a natural, well-defined channel produced by flowing water, or an artificial channel designed to carry flowing water",
        "code":"WTRC",
        "class":"Hydrographic",
        "name":"watercourse"
    },
    "ML":{
        "description":"a building housing machines for transforming, shaping, finishing, grinding, or extracting products",
        "code":"ML",
        "class":"Spot",
        "name":"mill(s)"
    },
    "HLT":{
        "description":"a place where caravans stop for rest",
        "code":"HLT",
        "class":"Spot",
        "name":"halting place"
    },
    "WTRH":{
        "description":"a natural hole, hollow, or small depression that contains water, used by man and animals, especially in arid areas",
        "code":"WTRH",
        "class":"Hydrographic",
        "name":"waterhole(s)"
    },
    "WTRW":{
        "description":"a facility for supplying potable water through a water source and a system of pumps and filtration beds",
        "code":"WTRW",
        "class":"Spot",
        "name":"waterworks"
    },
    "MT":{
        "description":"an elevation standing high above the surrounding area with small summit area, steep slopes and local relief of 300m or more",
        "code":"MT",
        "class":"Hypsographic",
        "name":"mountain"
    },
    "HLL":{
        "description":"a rounded elevation of limited extent rising above the surrounding land with local relief of less than 300m",
        "code":"HLL",
        "class":"Hypsographic",
        "name":"hill"
    },
    "NOV":{
        "description":"a religious house or school where novices are trained",
        "code":"NOV",
        "class":"Spot",
        "name":"novitiate"
    },
    "STNS":{
        "description":"a facility for tracking and communicating with orbiting satellites",
        "code":"STNS",
        "class":"Spot",
        "name":"satellite station"
    },
    "FT":{
        "description":"a defensive structure or earthworks",
        "code":"FT",
        "class":"Spot",
        "name":"fort"
    },
    "MLSGQ":{
        "description":"a sugar mill no longer used as a sugar mill",
        "code":"MLSGQ",
        "class":"Spot",
        "name":"former sugar mill"
    },
    "HBRX":{
        "description":"",
        "code":"HBRX",
        "class":"Hydrographic",
        "name":"section of harbor"
    },
    "FY":{
        "description":"a boat or other floating conveyance and terminal facilities regularly used to transport people and vehicles across a waterbody",
        "code":"FY",
        "class":"Spot",
        "name":"ferry"
    },
    "SMU":{
        "description":"an elevation rising generally more than 1,000 meters and of limited extent across the summit",
        "code":"SMU",
        "class":"Undersea",
        "name":"seamount"
    },
    "RET":{
        "description":"a building where goods and/or services are offered for sale",
        "code":"RET",
        "class":"Spot",
        "name":"store"
    },
    "FJD":{
        "description":"a long, narrow, steep-walled, deep-water arm of the sea at high latitudes, usually along mountainous coasts",
        "code":"FJD",
        "class":"Hydrographic",
        "name":"fjord"
    },
    "STPS":{
        "description":"stones or slabs placed for ease in ascending or descending a steep slope",
        "code":"STPS",
        "class":"Spot",
        "name":"steps"
    },
    "TAL":{
        "description":"a steep concave slope formed by an accumulation of loose rock fragments at the base of a cliff or steep slope",
        "code":"TAL",
        "class":"Hypsographic",
        "name":"talus slope"
    },
    "LIBR":{
        "description":"A place in which information resources such as books are kept for reading, reference, or lending.",
        "code":"LIBR",
        "class":"Spot",
        "name":"library"
    },
    "STNR":{
        "description":"a facility for producing and transmitting information by radio waves",
        "code":"STNR",
        "class":"Spot",
        "name":"radio station"
    },
    "SBED":{
        "description":"a channel formerly containing the water of a stream",
        "code":"SBED",
        "class":"Hypsographic",
        "name":"dry stream bed"
    },
    "REG":{
        "description":"a desert plain characterized by a surface veneer of gravel and stones",
        "code":"REG",
        "class":"Hypsographic",
        "name":"stony desert"
    },
    "SCHT":{
        "description":"post-secondary school with a specifically technical or vocational curriculum",
        "code":"SCHT",
        "class":"Spot",
        "name":"technical school"
    },
    "TRR":{
        "description":"a long, narrow alluvial platform bounded by steeper slopes above and below, usually overlooking a waterbody",
        "code":"TRR",
        "class":"Hypsographic",
        "name":"terrace"
    },
    "PKLT":{
        "description":"an area used for parking vehicles",
        "code":"PKLT",
        "class":"Spot",
        "name":"parking lot"
    },
    "RSGNL":{
        "description":"a signal at the entrance of a particular section of track governing the movement of trains",
        "code":"RSGNL",
        "class":"Spot",
        "name":"railroad signal"
    },
    "ASPH":{
        "description":"a small basin containing naturally occurring asphalt",
        "code":"ASPH",
        "class":"Hypsographic",
        "name":"asphalt lake"
    },
    "PNDS":{
        "description":"small standing waterbodies",
        "code":"PNDS",
        "class":"Hydrographic",
        "name":"ponds"
    },
    "PNDN":{
        "description":"a small standing body of salt water often in a marsh or swamp, usually along a seacoast",
        "code":"PNDN",
        "class":"Hydrographic",
        "name":"salt pond"
    },
    "SCHC":{
        "description":"the grounds and buildings of an institution of higher learning",
        "code":"SCHC",
        "class":"Spot",
        "name":"college"
    },
    "PNDI":{
        "description":"",
        "code":"PNDI",
        "class":"Hydrographic",
        "name":"intermittent pond"
    },
    "SCHN":{
        "description":"a school at which maritime sciences form the core of the curriculum",
        "code":"SCHN",
        "class":"Spot",
        "name":"maritime school"
    },
    "SCHL":{
        "description":"Language Schools & Institutions",
        "code":"SCHL",
        "class":"Spot",
        "name":"language school"
    },
    "SCHM":{
        "description":"a school at which military science forms the core of the curriculum",
        "code":"SCHM",
        "class":"Spot",
        "name":"military school"
    },
    "FCL":{
        "description":"a building or buildings housing a center, institute, foundation, hospital, prison, mission, courthouse, etc.",
        "code":"FCL",
        "class":"Spot",
        "name":"facility"
    },
    "MDW":{
        "description":"a small, poorly drained area dominated by grassy vegetation",
        "code":"MDW",
        "class":"Vegetation",
        "name":"meadow"
    },
    "GRVO":{
        "description":"a planting of olive trees",
        "code":"GRVO",
        "class":"Vegetation",
        "name":"olive grove"
    },
    "SPIT":{
        "description":"a narrow, straight or curved continuation of a beach into a waterbody",
        "code":"SPIT",
        "class":"Hypsographic",
        "name":"spit"
    },
    "GRVE":{
        "description":"a burial site",
        "code":"GRVE",
        "class":"Spot",
        "name":"grave"
    },
    "WEIR":{
        "description":"a small dam in a stream, designed to raise the water level or to divert stream flow through a desired channel",
        "code":"WEIR",
        "class":"Spot",
        "name":"weir(s)"
    },
    "GRVC":{
        "description":"a planting of coconut trees",
        "code":"GRVC",
        "class":"Vegetation",
        "name":"coconut grove"
    },
    "RECG":{
        "description":"a recreation field where golf is played",
        "code":"RECG",
        "class":"Spot",
        "name":"golf course"
    },
    "MVA":{
        "description":"a tract of land where military field exercises are carried out",
        "code":"MVA",
        "class":"Area",
        "name":"maneuver area"
    },
    "PRKHQ":{
        "description":"a park administrative facility",
        "code":"PRKHQ",
        "class":"Spot",
        "name":"park headquarters"
    },
    "VINS":{
        "description":"plantings of grapevines",
        "code":"VINS",
        "class":"Vegetation",
        "name":"vineyards"
    },
    "BAY":{
        "description":"a coastal indentation between two capes or headlands, larger than a cove but smaller than a gulf",
        "code":"BAY",
        "class":"Hydrographic",
        "name":"bay"
    },
    "GRVP":{
        "description":"a planting of palm trees",
        "code":"GRVP",
        "class":"Vegetation",
        "name":"palm grove"
    },
    "LEPC":{
        "description":"a settled area inhabited by lepers in relative isolation",
        "code":"LEPC",
        "class":"Spot",
        "name":"leper colony"
    },
    "RDST":{
        "description":"an open anchorage affording less protection than a harbor",
        "code":"RDST",
        "class":"Hydrographic",
        "name":"roadstead"
    },
    "RLG":{
        "description":"an ancient site of significant religious importance",
        "code":"RLG",
        "class":"Spot",
        "name":"religious site"
    },
    "ST":{
        "description":"a paved urban thoroughfare",
        "code":"ST",
        "class":"Road / Railroad",
        "name":"street"
    },
    "NTK":{
        "description":"a rock or mountain peak protruding through glacial ice",
        "code":"NTK",
        "class":"Hypsographic",
        "name":"nunatak"
    },
    "MKT":{
        "description":"a place where goods are bought and sold at regular intervals",
        "code":"MKT",
        "class":"Spot",
        "name":"market"
    },
    "SD":{
        "description":"a long arm of the sea forming a channel between the mainland and an island or islands; or connecting two larger bodies of water",
        "code":"SD",
        "class":"Hydrographic",
        "name":"sound"
    },
    "BSNU":{
        "description":"a depression more or less equidimensional in plan and of variable extent",
        "code":"BSNU",
        "class":"Undersea",
        "name":"basin"
    },
    "WADX":{
        "description":"",
        "code":"WADX",
        "class":"Hydrographic",
        "name":"section of wadi"
    },
    "DPR":{
        "description":"a low area surrounded by higher land and usually characterized by interior drainage",
        "code":"DPR",
        "class":"Hypsographic",
        "name":"depression(s)"
    },
    "BSNP":{
        "description":"an area underlain by an oil-rich structural basin",
        "code":"BSNP",
        "class":"Area",
        "name":"petroleum basin"
    },
    "PEN":{
        "description":"an elongate area of land projecting into a body of water",
        "code":"PEN",
        "class":"Hypsographic",
        "name":"peninsula"
    },
    "NKM":{
        "description":"a narrow strip of land between the two limbs of a meander loop at its narrowest point",
        "code":"NKM",
        "class":"Hypsographic",
        "name":"meander neck"
    },
    "WADS":{
        "description":"valleys or ravines, bounded by relatively steep banks, which in the rainy season become watercourses; found primarily in North Africa and the Middle East",
        "code":"WADS",
        "class":"Hydrographic",
        "name":"wadies"
    },
    "WADM":{
        "description":"the lower terminus of a wadi where it widens into an adjoining floodplain, depression, or waterbody",
        "code":"WADM",
        "class":"Hydrographic",
        "name":"wadi mouth"
    },
    "BSND":{
        "description":"an area drained by a stream",
        "code":"BSND",
        "class":"Area",
        "name":"drainage basin"
    },
    "MOTU":{
        "description":"an annular depression that may not be continuous, located at the base of many seamounts, islands, and other isolated elevations",
        "code":"MOTU",
        "class":"Undersea",
        "name":"moat"
    },
    "WADJ":{
        "description":"a place where two or more wadies join",
        "code":"WADJ",
        "class":"Hydrographic",
        "name":"wadi junction"
    },
    "HTH":{
        "description":"an upland moor or sandy area dominated by low shrubby vegetation including heather",
        "code":"HTH",
        "class":"Vegetation",
        "name":"heath"
    },
    "BNCH":{
        "description":"a long, narrow bedrock platform bounded by steeper slopes above and below, usually overlooking a waterbody",
        "code":"BNCH",
        "class":"Hypsographic",
        "name":"bench"
    },
    "WADB":{
        "description":"a conspicuously curved or bent segment of a wadi",
        "code":"WADB",
        "class":"Hydrographic",
        "name":"wadi bend"
    },
    "MRSH":{
        "description":"a wetland dominated by grass-like vegetation",
        "code":"MRSH",
        "class":"Hydrographic",
        "name":"marsh(es)"
    },
    "DIP":{
        "description":"office, residence, or facility of a foreign government, which may include an embassy, consulate, chancery, office of charge d'affaires, or other diplomatic, economic, military, or cultural mission",
        "code":"DIP",
        "class":"Spot",
        "name":"diplomatic facility"
    },
    "AMUS":{
        "description":"Amusement Park are theme parks, adventure parks offering entertainment, similar to funfairs but with a fix location",
        "code":"AMUS",
        "class":"Area",
        "name":"amusement park"
    },
    "MNDU":{
        "description":"a low, isolated, rounded hill",
        "code":"MNDU",
        "class":"Undersea",
        "name":"mound"
    },
    "LK":{
        "description":"a large inland body of standing water",
        "code":"LK",
        "class":"Hydrographic",
        "name":"lake"
    },
    "DCKY":{
        "description":"a facility for servicing, building, or repairing ships",
        "code":"DCKY",
        "class":"Spot",
        "name":"dockyard"
    },
    "PPLH":{
        "description":"a populated place that no longer exists",
        "code":"PPLH",
        "class":"Populated Place",
        "name":"historical populated place"
    },
    "DCKD":{
        "description":"a dock providing support for a vessel, and means for removing the water so that the bottom of the vessel can be exposed",
        "code":"DCKD",
        "class":"Spot",
        "name":"dry dock"
    },
    "MOOR":{
        "description":"an area of open ground overlaid with wet peaty soils",
        "code":"MOOR",
        "class":"Hydrographic",
        "name":"moor(s)"
    },
    "DCKB":{
        "description":"a part of a harbor where ships dock",
        "code":"DCKB",
        "class":"Hydrographic",
        "name":"docking basin"
    },
    "BLHL":{
        "description":"a hole in coastal rock through which sea water is forced by a rising tide or waves and spurted through an outlet into the air",
        "code":"BLHL",
        "class":"Hypsographic",
        "name":"blowhole(s)"
    },
    "MFGSG":{
        "description":"a facility for converting raw sugar into refined sugar",
        "code":"MFGSG",
        "class":"Spot",
        "name":"sugar refinery"
    },
    "GOVL":{
        "description":"a facility housing local governmental offices, usually a city, town, or village hall",
        "code":"GOVL",
        "class":"Spot",
        "name":"local government office"
    },
    "STNW":{
        "description":"a facility for butchering whales and processing train oil",
        "code":"STNW",
        "class":"Spot",
        "name":"whaling station"
    },
    "STM":{
        "description":"a body of running water moving to a lower level in a channel on land",
        "code":"STM",
        "class":"Hydrographic",
        "name":"stream"
    },
    "RESP":{
        "description":"an area of palm trees where use is controlled",
        "code":"RESP",
        "class":"Area",
        "name":"palm tree reserve"
    },
    "RESV":{
        "description":"a tract of land set aside for aboriginal, tribal, or native populations",
        "code":"RESV",
        "class":"Area",
        "name":"reservation"
    },
    "DIKE":{
        "description":"an earth or stone embankment usually constructed for flood or stream control",
        "code":"DIKE",
        "class":"Spot",
        "name":"dike"
    },
    "REST":{
        "description":"A place where meals are served to the public",
        "code":"REST",
        "class":"Spot",
        "name":"restaurant"
    },
    "FORD":{
        "description":"a shallow part of a stream which can be crossed on foot or by land vehicle",
        "code":"FORD",
        "class":"Hypsographic",
        "name":"ford"
    },
    "RESH":{
        "description":"a tract of land used primarily for hunting",
        "code":"RESH",
        "class":"Area",
        "name":"hunting reserve"
    },
    "DPOF":{
        "description":"an area where fuel is stored",
        "code":"DPOF",
        "class":"Spot",
        "name":"fuel depot"
    },
    "RESN":{
        "description":"an area reserved for the maintenance of a natural habitat",
        "code":"RESN",
        "class":"Area",
        "name":"nature reserve"
    },
    "MLWTR":{
        "description":"a mill powered by running water",
        "code":"MLWTR",
        "class":"Spot",
        "name":"water mill"
    },
    "STNI":{
        "description":"a station at which vehicles, goods, and people are inspected",
        "code":"STNI",
        "class":"Spot",
        "name":"inspection station"
    },
    "STNF":{
        "description":"a collection of buildings and facilities for carrying out forest management",
        "code":"STNF",
        "class":"Spot",
        "name":"forest station"
    },
    "STNE":{
        "description":"a facility for carrying out experiments",
        "code":"STNE",
        "class":"Spot",
        "name":"experiment station"
    },
    "RESA":{
        "description":"a tract of land reserved for agricultural reclamation and/or development",
        "code":"RESA",
        "class":"Area",
        "name":"agricultural reserve"
    },
    "RESF":{
        "description":"a forested area set aside for preservation or controlled use",
        "code":"RESF",
        "class":"Area",
        "name":"forest reserve"
    },
    "STNB":{
        "description":"a scientific facility used as a base from which research is carried out or monitored",
        "code":"STNB",
        "class":"Spot",
        "name":"scientific research base"
    },
    "BANK":{
        "description":"A business establishment in which money is kept for saving or commercial purposes or is invested, supplied for loans, or exchanged. ",
        "code":"BANK",
        "class":"Spot",
        "name":"bank"
    },
    "TUND":{
        "description":"a marshy, treeless, high latitude plain, dominated by mosses, lichens, and low shrub vegetation under permafrost conditions",
        "code":"TUND",
        "class":"Vegetation",
        "name":"tundra"
    },
    "WALLA":{
        "description":"the remains of a linear defensive stone structure",
        "code":"WALLA",
        "class":"Spot",
        "name":"ancient wall"
    },
    "WLLQ":{
        "description":"",
        "code":"WLLQ",
        "class":"Hydrographic",
        "name":"abandoned well"
    },
    "EDGU":{
        "description":"a line along which there is a marked increase of slope at the outer margin of a continental shelf or island shelf",
        "code":"EDGU",
        "class":"Undersea",
        "name":"shelf edge"
    },
    "TRGD":{
        "description":"a long wind-swept trough between parallel longitudinal dunes",
        "code":"TRGD",
        "class":"Hypsographic",
        "name":"interdune trough(s)"
    },
    "RSD":{
        "description":"a short track parallel to and joining the main track",
        "code":"RSD",
        "class":"Spot",
        "name":"railroad siding"
    },
    "NRWS":{
        "description":"a navigable narrow part of a bay, strait, river, etc.",
        "code":"NRWS",
        "class":"Hydrographic",
        "name":"narrows"
    },
    "PPLR":{
        "description":"a populated place whose population is largely engaged in religious occupations",
        "code":"PPLR",
        "class":"Populated Place",
        "name":"religious populated place"
    },
    "LAVA":{
        "description":"an area of solidified lava",
        "code":"LAVA",
        "class":"Hypsographic",
        "name":"lava area"
    },
    "VALX":{
        "description":"",
        "code":"VALX",
        "class":"Hypsographic",
        "name":"section of valley"
    },
    "TRGU":{
        "description":"a long depression of the sea floor characteristically flat bottomed and steep sided, and normally shallower than a trench",
        "code":"TRGU",
        "class":"Undersea",
        "name":"trough"
    },
    "RSV":{
        "description":"an artificial pond or lake",
        "code":"RSV",
        "class":"Hydrographic",
        "name":"reservoir(s)"
    },
    "PND":{
        "description":"a small standing waterbody",
        "code":"PND",
        "class":"Hydrographic",
        "name":"pond"
    },
    "ZNB":{
        "description":"a zone recognized as a buffer between two nations in which military presence is minimal or absent",
        "code":"ZNB",
        "class":"Administrative Boundary",
        "name":"buffer zone"
    },
    "LKNI":{
        "description":"",
        "code":"LKNI",
        "class":"Hydrographic",
        "name":"intermittent salt lake"
    },
    "ZNF":{
        "description":"an area, usually a section of a port, where goods may be received and shipped free of customs duty and of most customs regulations",
        "code":"ZNF",
        "class":"Spot",
        "name":"free trade zone"
    },
    "PASS":{
        "description":"a break in a mountain range or other high obstruction, used for transportation from one side to the other [See also gap]",
        "code":"PASS",
        "class":"Hypsographic",
        "name":"pass"
    },
    "VALS":{
        "description":"elongated depressions usually traversed by a stream",
        "code":"VALS",
        "class":"Hypsographic",
        "name":"valleys"
    },
    "GAP":{
        "description":"a low place in a ridge, not used for transportation",
        "code":"GAP",
        "class":"Hypsographic",
        "name":"gap"
    },
    "LBED":{
        "description":"a dried up or drained area of a former lake",
        "code":"LBED",
        "class":"Hydrographic",
        "name":"lake bed(s)"
    },
    "RR":{
        "description":"a permanent twin steel-rail track on which freight and passenger cars move long distances",
        "code":"RR",
        "class":"Road / Railroad",
        "name":"railroad"
    },
    "MNQR":{
        "description":"a surface mine where building stone or gravel and sand, etc. are extracted",
        "code":"MNQR",
        "class":"Spot",
        "name":"quarry(-ies)"
    },
    "PRN":{
        "description":"a facility for confining prisoners",
        "code":"PRN",
        "class":"Spot",
        "name":"prison"
    },
    "DTCH":{
        "description":"a small artificial watercourse dug for draining or irrigating the land",
        "code":"DTCH",
        "class":"Hydrographic",
        "name":"ditch"
    },
    "PRK":{
        "description":"an area, often of forested land, maintained as a place of beauty, or for recreation",
        "code":"PRK",
        "class":"Area",
        "name":"park"
    },
    "RD":{
        "description":"an open way with improved surface for transportation of animals, people and vehicles",
        "code":"RD",
        "class":"Road / Railroad",
        "name":"road"
    },
    "PRT":{
        "description":"a place provided with terminal and transfer facilities for loading and discharging waterborne cargo or passengers, usually located in a harbor",
        "code":"PRT",
        "class":"Area",
        "name":"port"
    },
    "RF":{
        "description":"a surface-navigation hazard composed of consolidated material",
        "code":"RF",
        "class":"Hydrographic",
        "name":"reef(s)"
    },
    "CNYU":{
        "description":"a relatively narrow, deep depression with steep sides, the bottom of which generally has a continuous slope",
        "code":"CNYU",
        "class":"Undersea",
        "name":"canyon"
    },
    "ASTR":{
        "description":"a point on the earth whose position has been determined by observations of celestial bodies",
        "code":"ASTR",
        "class":"Spot",
        "name":"astronomical station"
    },
    "RK":{
        "description":"a conspicuous, isolated rocky mass",
        "code":"RK",
        "class":"Hypsographic",
        "name":"rock"
    },
    "CMPMN":{
        "description":"a camp used by miners",
        "code":"CMPMN",
        "class":"Spot",
        "name":"mining camp"
    },
    "PRMN":{
        "description":"a place for public walking, usually along a beach front",
        "code":"PRMN",
        "class":"Road / Railroad",
        "name":"promenade"
    },
    "TNLN":{
        "description":"a cave that is open at both ends",
        "code":"TNLN",
        "class":"Road / Railroad",
        "name":"natural tunnel"
    },
    "TNLC":{
        "description":"a tunnel through which a canal passes",
        "code":"TNLC",
        "class":"Hydrographic",
        "name":"canal tunnel"
    },
    "CHN":{
        "description":"the deepest part of a stream, bay, lagoon, or strait, through which the main current flows",
        "code":"CHN",
        "class":"Hydrographic",
        "name":"channel"
    },
    "DPRG":{
        "description":"a comparatively depressed area on an icecap",
        "code":"DPRG",
        "class":"Hydrographic",
        "name":"icecap depression"
    },
    "MRN":{
        "description":"a mound, ridge, or other accumulation of glacial till",
        "code":"MRN",
        "class":"Hypsographic",
        "name":"moraine"
    },
    "PSTP":{
        "description":"a post from which patrols are sent out",
        "code":"PSTP",
        "class":"Spot",
        "name":"patrol post"
    },
    "CRSU":{
        "description":"a gentle slope rising from oceanic depths towards the foot of a continental slope",
        "code":"CRSU",
        "class":"Undersea",
        "name":"continental rise"
    },
    "TNLS":{
        "description":"subterranean passageways for transportation",
        "code":"TNLS",
        "class":"Road / Railroad",
        "name":"tunnels"
    },
    "PIER":{
        "description":"a structure built out into navigable water on piles providing berthing for ships and recreation",
        "code":"PIER",
        "class":"Spot",
        "name":"pier"
    },
    "LKSN":{
        "description":"inland bodies of salt water with no outlet",
        "code":"LKSN",
        "class":"Hydrographic",
        "name":"salt lakes"
    },
    "MTRO":{
        "description":"metro station (Underground, Tube, or Metro) ",
        "code":"MTRO",
        "class":"Spot",
        "name":"metro station"
    },
    "VIN":{
        "description":"a planting of grapevines",
        "code":"VIN",
        "class":"Vegetation",
        "name":"vineyard"
    },
    "FNDY":{
        "description":"a building or works where metal casting is carried out",
        "code":"FNDY",
        "class":"Spot",
        "name":"foundry"
    },
    "LKSNI":{
        "description":"",
        "code":"LKSNI",
        "class":"Hydrographic",
        "name":"intermittent salt lakes"
    },
    "CNFL":{
        "description":"a place where two or more streams or intermittent streams flow together",
        "code":"CNFL",
        "class":"Hydrographic",
        "name":"confluence"
    },
    "BRKS":{
        "description":"a building for lodging military personnel",
        "code":"BRKS",
        "class":"Spot",
        "name":"barracks"
    },
    "BRKW":{
        "description":"a structure erected to break the force of waves at the entrance to a harbor or port",
        "code":"BRKW",
        "class":"Spot",
        "name":"breakwater"
    },
    "MNCU":{
        "description":"a mine where copper ore is extracted",
        "code":"MNCU",
        "class":"Spot",
        "name":"copper mine(s)"
    },
    "MNCR":{
        "description":"a mine where chrome ore is extracted",
        "code":"MNCR",
        "class":"Spot",
        "name":"chrome mine(s)"
    },
    "ARRU":{
        "description":"an area of subdued corrugations off Baja California",
        "code":"ARRU",
        "class":"Undersea",
        "name":"arrugado"
    },
    "OCH":{
        "description":"a planting of fruit or nut trees",
        "code":"OCH",
        "class":"Vegetation",
        "name":"orchard(s)"
    },
    "OCN":{
        "description":"one of the major divisions of the vast expanse of salt water covering part of the earth",
        "code":"OCN",
        "class":"Hydrographic",
        "name":"ocean"
    },
    "PEAT":{
        "description":"an area where peat is harvested",
        "code":"PEAT",
        "class":"Area",
        "name":"peat cutting area"
    },
    "LKSI":{
        "description":"",
        "code":"LKSI",
        "class":"Hydrographic",
        "name":"intermittent lakes"
    },
    "GASF":{
        "description":"an area containing a subterranean store of natural gas of economic value",
        "code":"GASF",
        "class":"Area",
        "name":"gasfield"
    },
    "HSPD":{
        "description":"a building where medical or dental aid is dispensed",
        "code":"HSPD",
        "class":"Spot",
        "name":"dispensary"
    },
    "HSPC":{
        "description":"a medical facility associated with a hospital for outpatients",
        "code":"HSPC",
        "class":"Spot",
        "name":"clinic"
    },
    "WHRL":{
        "description":"a turbulent, rotating movement of water in a stream",
        "code":"WHRL",
        "class":"Hydrographic",
        "name":"whirlpool"
    },
    "COLF":{
        "description":"a region in which coal deposits of possible economic value occur",
        "code":"COLF",
        "class":"Area",
        "name":"coalfield"
    },
    "HSPL":{
        "description":"an asylum or hospital for lepers",
        "code":"HSPL",
        "class":"Spot",
        "name":"leprosarium"
    },
    "WHRF":{
        "description":"a structure of open rather than solid construction along a shore or a bank which provides berthing for ships and cargo-handling facilities",
        "code":"WHRF",
        "class":"Spot",
        "name":"wharf(-ves)"
    },
    "BDLD":{
        "description":"an area characterized by a maze of very closely spaced, deep, narrow, steep-sided ravines, and sharp crests and pinnacles",
        "code":"BDLD",
        "class":"Hypsographic",
        "name":"badlands"
    },
    "RTE":{
        "description":"the route taken by caravans",
        "code":"RTE",
        "class":"Road / Railroad",
        "name":"caravan route"
    },
    "PKS":{
        "description":"pointed elevations atop a mountain, ridge, or other hypsographic features",
        "code":"PKS",
        "class":"Hypsographic",
        "name":"peaks"
    },
    "MLWND":{
        "description":"a mill or water pump powered by wind",
        "code":"MLWND",
        "class":"Spot",
        "name":"windmill"
    },
    "PKU":{
        "description":"a prominent elevation, part of a larger feature, either pointed or of very limited extent across the summit",
        "code":"PKU",
        "class":"Undersea",
        "name":"peak"
    },
    "SILL":{
        "description":"the low part of an underwater gap or saddle separating basins, including a similar feature at the mouth of a fjord",
        "code":"SILL",
        "class":"Hydrographic",
        "name":"sill"
    },
    "BUSTP":{
        "description":"a place lacking station facilities",
        "code":"BUSTP",
        "class":"Spot",
        "name":"bus stop"
    },
    "ESTY":{
        "description":"a funnel-shaped stream mouth or embayment where fresh water mixes with sea water under tidal influences",
        "code":"ESTY",
        "class":"Hydrographic",
        "name":"estuary"
    },
    "PLNX":{
        "description":"",
        "code":"PLNX",
        "class":"Hypsographic",
        "name":"section of plain"
    },
    "BUSTN":{
        "description":"a facility comprising ticket office, platforms, etc. for loading and unloading passengers ",
        "code":"BUSTN",
        "class":"Spot",
        "name":"bus station"
    },
    "LDNG":{
        "description":"a place where boats receive or discharge passengers and freight, but lacking most port facilities",
        "code":"LDNG",
        "class":"Spot",
        "name":"landing"
    },
    "GATE":{
        "description":"a controlled access entrance or exit",
        "code":"GATE",
        "class":"Spot",
        "name":"gate"
    },
    "PLNU":{
        "description":"a flat, gently sloping or nearly level region",
        "code":"PLNU",
        "class":"Undersea",
        "name":"plain"
    },
    "PRVU":{
        "description":"a region identifiable by a group of similar physiographic features whose characteristics are markedly in contrast with surrounding areas",
        "code":"PRVU",
        "class":"Undersea",
        "name":"province"
    },
    "JTY":{
        "description":"a structure built out into the water at a river mouth or harbor entrance to regulate currents and silting",
        "code":"JTY",
        "class":"Spot",
        "name":"jetty"
    },
    "RFU":{
        "description":"a surface-navigation hazard composed of consolidated material",
        "code":"RFU",
        "class":"Undersea",
        "name":"reef"
    },
    "SHRN":{
        "description":"a structure or place memorializing a person or religious concept",
        "code":"SHRN",
        "class":"Spot",
        "name":"shrine"
    },
    "RFX":{
        "description":"",
        "code":"RFX",
        "class":"Hydrographic",
        "name":"section of reef"
    },
    "BTYD":{
        "description":"a waterside facility for servicing, repairing, and building small vessels",
        "code":"BTYD",
        "class":"Spot",
        "name":"boatyard"
    },
    "RESW":{
        "description":"a tract of public land reserved for the preservation of wildlife",
        "code":"RESW",
        "class":"Area",
        "name":"wildlife reserve"
    },
    "RFC":{
        "description":"a surface-navigation hazard composed of coral",
        "code":"RFC",
        "class":"Hydrographic",
        "name":"coral reef(s)"
    },
    "PRKGT":{
        "description":"a controlled access to a park",
        "code":"PRKGT",
        "class":"Spot",
        "name":"park gate"
    },
    "SLCE":{
        "description":"a conduit or passage for carrying off surplus water from a waterbody, usually regulated by means of a sluice gate",
        "code":"SLCE",
        "class":"Spot",
        "name":"sluice"
    },
    "CST":{
        "description":"a zone of variable width straddling the shoreline",
        "code":"CST",
        "class":"Area",
        "name":"coast"
    },
    "STNC":{
        "description":"a facility from which the coast is guarded by armed vessels",
        "code":"STNC",
        "class":"Spot",
        "name":"coast guard station"
    },
    "VLSU":{
        "description":"a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
        "code":"VLSU",
        "class":"Undersea",
        "name":"valleys"
    },
    "CLDA":{
        "description":"a depression measuring kilometers across formed by the collapse of a volcanic mountain",
        "code":"CLDA",
        "class":"Hypsographic",
        "name":"caldera"
    },
    "RSTP":{
        "description":"a place lacking station facilities where trains stop to pick up and unload passengers and freight",
        "code":"RSTP",
        "class":"Spot",
        "name":"railroad stop"
    },
    "STNM":{
        "description":"a station at which weather elements are recorded",
        "code":"STNM",
        "class":"Spot",
        "name":"meteorological station"
    },
    "PROM":{
        "description":"a bluff or prominent hill overlooking or projecting into a lowland",
        "code":"PROM",
        "class":"Hypsographic",
        "name":"promontory(-ies)"
    },
    "DTCHM":{
        "description":"an area where a drainage ditch enters a lagoon, lake or bay",
        "code":"DTCHM",
        "class":"Hydrographic",
        "name":"ditch mouth(s)"
    },
    "MGV":{
        "description":"a tropical tidal mud flat characterized by mangrove vegetation",
        "code":"MGV",
        "class":"Hydrographic",
        "name":"mangrove swamp"
    },
    "DTCHI":{
        "description":"a ditch which serves to distribute irrigation water",
        "code":"DTCHI",
        "class":"Hydrographic",
        "name":"irrigation ditch"
    },
    "BTL":{
        "description":"a site of a land battle of historical importance",
        "code":"BTL",
        "class":"Area",
        "name":"battlefield"
    },
    "DTCHD":{
        "description":"a ditch which serves to drain the land",
        "code":"DTCHD",
        "class":"Hydrographic",
        "name":"drainage ditch"
    },
    "RSTN":{
        "description":"a facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight",
        "code":"RSTN",
        "class":"Spot",
        "name":"railroad station"
    },
    "ITTR":{
        "description":"a facility where research is carried out",
        "code":"ITTR",
        "class":"Spot",
        "name":"research institute"
    },
    "PTGE":{
        "description":"a place where boats, goods, etc., are carried overland between navigable waters",
        "code":"PTGE",
        "class":"Road / Railroad",
        "name":"portage"
    },
    "FANU":{
        "description":"a relatively smooth feature normally sloping away from the lower termination of a canyon or canyon system",
        "code":"FANU",
        "class":"Undersea",
        "name":"fan"
    },
    "MUS":{
        "description":"a building where objects of permanent interest in one or more of the arts and sciences are preserved and exhibited",
        "code":"MUS",
        "class":"Spot",
        "name":"museum"
    },
    "CMPQ":{
        "description":"",
        "code":"CMPQ",
        "class":"Spot",
        "name":"abandoned camp"
    },
    "ATM":{
        "description":"An unattended electronic machine in a public place, connected to a data system and related equipment and activated by a bank customer to obtain cash withdrawals and other banking services. ",
        "code":"ATM",
        "class":"Spot",
        "name":"automatic teller machine"
    },
    "CRQ":{
        "description":"a bowl-like hollow partially surrounded by cliffs or steep slopes at the head of a glaciated valley",
        "code":"CRQ",
        "class":"Hypsographic",
        "name":"cirque"
    },
    "ESCU":{
        "description":"an elongated and comparatively steep slope separating flat or gently sloping areas",
        "code":"ESCU",
        "class":"Undersea",
        "name":"escarpment (or scarp)"
    },
    "ISL":{
        "description":"a tract of land, smaller than a continent, surrounded by water at high water",
        "code":"ISL",
        "class":"Hypsographic",
        "name":"island"
    },
    "LGNS":{
        "description":"shallow coastal waterbodies, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature",
        "code":"LGNS",
        "class":"Hydrographic",
        "name":"lagoons"
    },
    "LAND":{
        "description":"a tract of land in the Arctic",
        "code":"LAND",
        "class":"Area",
        "name":"arctic land"
    },
    "AREA":{
        "description":"a tract of land without homogeneous character or boundaries",
        "code":"AREA",
        "class":"Area",
        "name":"area"
    },
    "CVNT":{
        "description":"a building where a community of nuns lives in seclusion",
        "code":"CVNT",
        "class":"Spot",
        "name":"convent"
    },
    "CTHSE":{
        "description":"a building in which courts of law are held",
        "code":"CTHSE",
        "class":"Spot",
        "name":"courthouse"
    },
    "PYRS":{
        "description":"ancient massive structures of square ground plan with four triangular faces meeting at a point and used for enclosing tombs",
        "code":"PYRS",
        "class":"Spot",
        "name":"pyramids"
    },
    "SEA":{
        "description":"a large body of salt water more or less confined by continuous land or chains of islands forming a subdivision of an ocean",
        "code":"SEA",
        "class":"Hydrographic",
        "name":"sea"
    },
    "RHSE":{
        "description":"a structure maintained for the rest and shelter of travelers",
        "code":"RHSE",
        "class":"Spot",
        "name":"resthouse"
    },
    "HMSD":{
        "description":"a residence, owner's or manager's, on a sheep or cattle station, woolshed, outcamp, or Aboriginal outstation, specific to Australia and New Zealand ",
        "code":"HMSD",
        "class":"Spot",
        "name":"homestead"
    },
    "CSTL":{
        "description":"a large fortified building or set of buildings",
        "code":"CSTL",
        "class":"Spot",
        "name":"castle"
    },
    "CSTM":{
        "description":"a building in a port where customs and duties are paid, and where vessels are entered and cleared",
        "code":"CSTM",
        "class":"Spot",
        "name":"customs house"
    },
    "TRIG":{
        "description":"a point on the earth whose position has been determined by triangulation",
        "code":"TRIG",
        "class":"Spot",
        "name":"triangulation station"
    },
    "CLG":{
        "description":"an area in a forest with trees removed",
        "code":"CLG",
        "class":"Area",
        "name":"clearing"
    },
    "FRM":{
        "description":"a tract of land with associated buildings devoted to agriculture",
        "code":"FRM",
        "class":"Spot",
        "name":"farm"
    },
    "CARN":{
        "description":"a heap of stones erected as a landmark or for other purposes",
        "code":"CARN",
        "class":"Spot",
        "name":"cairn"
    },
    "SCRP":{
        "description":"a long line of cliffs or steep slopes separating level surfaces above and below",
        "code":"SCRP",
        "class":"Hypsographic",
        "name":"escarpment"
    },
    "FLTM":{
        "description":"a relatively level area of mud either between high and low tide lines, or subject to flooding",
        "code":"FLTM",
        "class":"Hydrographic",
        "name":"mud flat(s)"
    },
    "LTER":{
        "description":"a tract of land leased to another country, usually for military installations",
        "code":"LTER",
        "class":"Administrative Boundary",
        "name":"leased area"
    },
    "SCRB":{
        "description":"an area of low trees, bushes, and shrubs stunted by some environmental limitation",
        "code":"SCRB",
        "class":"Vegetation",
        "name":"scrubland"
    },
    "APNU":{
        "description":"a gentle slope, with a generally smooth surface, particularly found around groups of islands and seamounts",
        "code":"APNU",
        "class":"Undersea",
        "name":"apron"
    },
    "MFGPH":{
        "description":"a facility for producing fertilizer",
        "code":"MFGPH",
        "class":"Spot",
        "name":"phosphate works"
    },
    "FLTT":{
        "description":"a large flat area of mud or sand attached to the shore and alternately covered and uncovered by the tide",
        "code":"FLTT",
        "class":"Hydrographic",
        "name":"tidal flat(s)"
    },
    "FLTU":{
        "description":"a small level or nearly level area",
        "code":"FLTU",
        "class":"Undersea",
        "name":"flat"
    },
    "STMX":{
        "description":"",
        "code":"STMX",
        "class":"Hydrographic",
        "name":"section of stream"
    },
    "CSWY":{
        "description":"a raised roadway across wet ground or shallow water",
        "code":"CSWY",
        "class":"Road / Railroad",
        "name":"causeway"
    },
    "HSTS":{
        "description":"a place of historical importance",
        "code":"HSTS",
        "class":"Spot",
        "name":"historical site"
    },
    "STMS":{
        "description":"bodies of running water moving to a lower level in a channel on land",
        "code":"STMS",
        "class":"Hydrographic",
        "name":"streams"
    },
    "STMQ":{
        "description":"a former stream or distributary no longer carrying flowing water, but still evident due to lakes, wetland, topographic or vegetation patterns",
        "code":"STMQ",
        "class":"Hydrographic",
        "name":"abandoned watercourse"
    },
    "LTHSE":{
        "description":"a distinctive structure exhibiting a major navigation light",
        "code":"LTHSE",
        "class":"Spot",
        "name":"lighthouse"
    },
    "STMH":{
        "description":"the source and upper part of a stream, including the upper drainage basin",
        "code":"STMH",
        "class":"Hydrographic",
        "name":"headwaters"
    },
    "STMI":{
        "description":"",
        "code":"STMI",
        "class":"Hydrographic",
        "name":"intermittent stream"
    },
    "RDJCT":{
        "description":"a place where two or more roads join",
        "code":"RDJCT",
        "class":"Road / Railroad",
        "name":"road junction"
    },
    "SINK":{
        "description":"a small crater-shape depression in a karst area",
        "code":"SINK",
        "class":"Hypsographic",
        "name":"sinkhole"
    },
    "STMM":{
        "description":"a place where a stream discharges into a lagoon, lake, or the sea",
        "code":"STMM",
        "class":"Hydrographic",
        "name":"stream mouth(s)"
    },
    "AGRF":{
        "description":"a building and/or tract of land used for improving agriculture",
        "code":"AGRF",
        "class":"Spot",
        "name":"agricultural facility"
    },
    "STMC":{
        "description":"a stream that has been substantially ditched, diked, or straightened",
        "code":"STMC",
        "class":"Hydrographic",
        "name":"canalized stream"
    },
    "STMA":{
        "description":"a diverging branch flowing out of a main stream and rejoining it downstream",
        "code":"STMA",
        "class":"Hydrographic",
        "name":"anabranch"
    },
    "AGRC":{
        "description":"a tract of land set aside for agricultural settlement",
        "code":"AGRC",
        "class":"Area",
        "name":"agricultural colony"
    },
    "STMD":{
        "description":"a branch which flows away from the main stream, as in a delta or irrigation canal",
        "code":"STMD",
        "class":"Hydrographic",
        "name":"distributary(-ies)"
    },
    "HERM":{
        "description":"a secluded residence, usually for religious sects",
        "code":"HERM",
        "class":"Spot",
        "name":"hermitage"
    },
    "MSQE":{
        "description":"a building for public Islamic worship",
        "code":"MSQE",
        "class":"Spot",
        "name":"mosque"
    },
    "MFGLM":{
        "description":"a furnace in which limestone is reduced to lime",
        "code":"MFGLM",
        "class":"Spot",
        "name":"limekiln"
    },
    "TMSU":{
        "description":"seamounts having a comparatively smooth, flat top",
        "code":"TMSU",
        "class":"Undersea",
        "name":"tablemounts (or guyots)"
    },
    "SCNU":{
        "description":"a continuously sloping, elongated depression commonly found in fans or plains and customarily bordered by levees on one or two sides",
        "code":"SCNU",
        "class":"Undersea",
        "name":"seachannel"
    },
    "SAND":{
        "description":"a tract of land covered with sand",
        "code":"SAND",
        "class":"Hypsographic",
        "name":"sand area"
    },
    "MLSG":{
        "description":"a facility where sugar cane is processed into raw sugar",
        "code":"MLSG",
        "class":"Spot",
        "name":"sugar mill"
    },
    "CMPO":{
        "description":"a camp used by oilfield workers",
        "code":"CMPO",
        "class":"Spot",
        "name":"oil camp"
    },
    "CLF":{
        "description":"a high, steep to perpendicular slope overlooking a waterbody or lower area",
        "code":"CLF",
        "class":"Hypsographic",
        "name":"cliff(s)"
    },
    "SHPF":{
        "description":"a fence or wall enclosure for sheep and other small herd animals",
        "code":"SHPF",
        "class":"Spot",
        "name":"sheepfold"
    },
    "QCKS":{
        "description":"an area where loose sand with water moving through it may become unstable when heavy objects are placed at the surface, causing them to sink",
        "code":"QCKS",
        "class":"Area",
        "name":"quicksand"
    },
    "HOLU":{
        "description":"a small depression of the sea floor",
        "code":"HOLU",
        "class":"Undersea",
        "name":"hole"
    },
    "OBSR":{
        "description":"a facility equipped with an array of antennae for receiving radio waves from space",
        "code":"OBSR",
        "class":"Spot",
        "name":"radio observatory"
    },
    "CRNT":{
        "description":"a horizontal flow of water in a given direction with uniform velocity",
        "code":"CRNT",
        "class":"Hydrographic",
        "name":"current"
    },
    "MLM":{
        "description":"a facility for improving the metal content of ore by concentration",
        "code":"MLM",
        "class":"Spot",
        "name":"ore treatment plant"
    },
    "MILB":{
        "description":"a place used by an army or other armed service for storing arms and supplies, and for accommodating and training troops, a base from which operations can be initiated",
        "code":"MILB",
        "class":"Area",
        "name":"military base"
    },
    "CFT":{
        "description":"a deep narrow slot, notch, or groove in a coastal cliff",
        "code":"CFT",
        "class":"Hypsographic",
        "name":"cleft(s)"
    },
    "POOL":{
        "description":"a small and comparatively still, deep part of a larger body of water such as a stream or harbor; or a small body of standing water",
        "code":"POOL",
        "class":"Hydrographic",
        "name":"pool(s)"
    },
    "AIRB":{
        "description":"an area used to store supplies, provide barracks for air force personnel, hangars and runways for aircraft, and from which operations are initiated",
        "code":"AIRB",
        "class":"Spot",
        "name":"airbase"
    },
    "LGN":{
        "description":"a shallow coastal waterbody, completely or partly separated from a larger body of water by a barrier island, coral reef or other depositional feature",
        "code":"LGN",
        "class":"Hydrographic",
        "name":"lagoon"
    },
    "PT":{
        "description":"a tapering piece of land projecting into a body of water, less prominent than a cape",
        "code":"PT",
        "class":"Hypsographic",
        "name":"point"
    },
    "AIRF":{
        "description":"a place on land where aircraft land and take off; no facilities provided for the commercial handling of passengers and cargo",
        "code":"AIRF",
        "class":"Spot",
        "name":"airfield"
    },
    "GLYU":{
        "description":"a small valley-like feature",
        "code":"GLYU",
        "class":"Undersea",
        "name":"gully"
    },
    "AIRH":{
        "description":"a place where helicopters land and take off",
        "code":"AIRH",
        "class":"Spot",
        "name":"heliport"
    },
    "MFG":{
        "description":"one or more buildings where goods are manufactured, processed or fabricated",
        "code":"MFG",
        "class":"Spot",
        "name":"factory"
    },
    "AIRP":{
        "description":"a place where aircraft regularly land and take off, with runways, navigational aids, and major facilities for the commercial handling of passengers and cargo",
        "code":"AIRP",
        "class":"Spot",
        "name":"airport"
    },
    "AIRQ":{
        "description":"",
        "code":"AIRQ",
        "class":"Spot",
        "name":"abandoned airfield"
    },
    "AIRS":{
        "description":"a place on a waterbody where floatplanes land and take off",
        "code":"AIRS",
        "class":"Hydrographic",
        "name":"seaplane landing area"
    },
    "ADM4H":{
        "description":"a former fourth-order administrative division",
        "code":"ADM4H",
        "class":"Administrative Boundary",
        "name":"historical fourth-order administrative division"
    },
    "ISLET":{
        "description":"small island, bigger than rock, smaller than island.",
        "code":"ISLET",
        "class":"Hypsographic",
        "name":"islet"
    },
    "PCLIX":{
        "description":"",
        "code":"PCLIX",
        "class":"Administrative Boundary",
        "name":"section of independent political entity"
    },
    "GRVPN":{
        "description":"a planting of pine trees",
        "code":"GRVPN",
        "class":"Vegetation",
        "name":"pine grove"
    },
    "CRRL":{
        "description":"a pen or enclosure for confining or capturing animals",
        "code":"CRRL",
        "class":"Spot",
        "name":"corral(s)"
    },
    "PLDR":{
        "description":"an area reclaimed from the sea by diking and draining",
        "code":"PLDR",
        "class":"Hypsographic",
        "name":"polder"
    },
    "SWMP":{
        "description":"a wetland dominated by tree vegetation",
        "code":"SWMP",
        "class":"Hydrographic",
        "name":"swamp"
    },
    "BSTN":{
        "description":"a facility for baling agricultural products",
        "code":"BSTN",
        "class":"Spot",
        "name":"baling station"
    },
    "PAL":{
        "description":"a large stately house, often a royal or presidential residence",
        "code":"PAL",
        "class":"Spot",
        "name":"palace"
    },
    "PAN":{
        "description":"a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool",
        "code":"PAN",
        "class":"Hypsographic",
        "name":"pan"
    },
    "RSTPQ":{
        "description":"",
        "code":"RSTPQ",
        "class":"Spot",
        "name":"abandoned railroad stop"
    },
    "DCK":{
        "description":"a waterway between two piers, or cut into the land for the berthing of ships",
        "code":"DCK",
        "class":"Hydrographic",
        "name":"dock(s)"
    },
    "HSE":{
        "description":"a building used as a human habitation",
        "code":"HSE",
        "class":"Spot",
        "name":"house(s)"
    },
    "DEPU":{
        "description":"a localized deep area within the confines of a larger feature, such as a trough, basin or trench",
        "code":"DEPU",
        "class":"Undersea",
        "name":"deep"
    },
    "BUSH":{
        "description":"a small clump of conspicuous bushes in an otherwise bare area",
        "code":"BUSH",
        "class":"Vegetation",
        "name":"bush(es)"
    },
    "PKSU":{
        "description":"prominent elevations, part of a larger feature, either pointed or of very limited extent across the summit",
        "code":"PKSU",
        "class":"Undersea",
        "name":"peaks"
    },
    "ADM4":{
        "description":"a subdivision of a third-order administrative division",
        "code":"ADM4",
        "class":"Administrative Boundary",
        "name":"fourth-order administrative division"
    },
    "ADM5":{
        "description":"a subdivision of a fourth-order administrative division",
        "code":"ADM5",
        "class":"Administrative Boundary",
        "name":"fifth-order administrative division"
    },
    "CNYN":{
        "description":"a deep, narrow valley with steep sides cutting into a plateau or mountainous area",
        "code":"CNYN",
        "class":"Hypsographic",
        "name":"canyon"
    },
    "ADM1":{
        "description":"a primary administrative division of a country, such as a state in the United States",
        "code":"ADM1",
        "class":"Administrative Boundary",
        "name":"first-order administrative division"
    },
    "ADM2":{
        "description":"a subdivision of a first-order administrative division",
        "code":"ADM2",
        "class":"Administrative Boundary",
        "name":"second-order administrative division"
    },
    "ADM3":{
        "description":"a subdivision of a second-order administrative division",
        "code":"ADM3",
        "class":"Administrative Boundary",
        "name":"third-order administrative division"
    },
    "STDM":{
        "description":"a structure with an enclosure for athletic games with tiers of seats for spectators",
        "code":"STDM",
        "class":"Spot",
        "name":"stadium"
    },
    "PPLA":{
        "description":"seat of a first-order administrative division (PPLC takes precedence over PPLA)",
        "code":"PPLA",
        "class":"Populated Place",
        "name":"seat of a first-order administrative division"
    },
    "PPLC":{
        "description":"",
        "code":"PPLC",
        "class":"Populated Place",
        "name":"capital of a political entity"
    },
    "FRSTF":{
        "description":"a forest fossilized by geologic processes and now exposed at the earth's surface",
        "code":"FRSTF",
        "class":"Vegetation",
        "name":"fossilized forest"
    },
    "PPLF":{
        "description":"a populated place where the population is largely engaged in agricultural activities",
        "code":"PPLF",
        "class":"Populated Place",
        "name":"farm village"
    },
    "PPLG":{
        "description":"",
        "code":"PPLG",
        "class":"Populated Place",
        "name":"seat of government of a political entity"
    },
    "ADMD":{
        "description":"an administrative division of a country, undifferentiated as to administrative level",
        "code":"ADMD",
        "class":"Administrative Boundary",
        "name":"administrative division"
    },
    "ADMF":{
        "description":"a government building",
        "code":"ADMF",
        "class":"Spot",
        "name":"administrative facility"
    },
    "PPLL":{
        "description":"an area similar to a locality but with a small group of dwellings or other buildings",
        "code":"PPLL",
        "class":"Populated Place",
        "name":"populated locality"
    },
    "GRGE":{
        "description":"a short, narrow, steep-sided section of a stream valley",
        "code":"GRGE",
        "class":"Hypsographic",
        "name":"gorge(s)"
    },
    "DOMG":{
        "description":"a comparatively elevated area on an icecap",
        "code":"DOMG",
        "class":"Hydrographic",
        "name":"icecap dome"
    },
    "BNK":{
        "description":"an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for most surface navigation",
        "code":"BNK",
        "class":"Hydrographic",
        "name":"bank(s)"
    },
    "PPLQ":{
        "description":"",
        "code":"PPLQ",
        "class":"Populated Place",
        "name":"abandoned populated place"
    },
    "WLLS":{
        "description":"cylindrical holes, pits, or tunnels drilled or dug down to a depth from which water, oil, or gas can be pumped or brought to the surface",
        "code":"WLLS",
        "class":"Hydrographic",
        "name":"wells"
    },
    "PPLS":{
        "description":"cities, towns, villages, or other agglomerations of buildings where people live and work",
        "code":"PPLS",
        "class":"Populated Place",
        "name":"populated places"
    },
    "GAPU":{
        "description":"a narrow break in a ridge or rise",
        "code":"GAPU",
        "class":"Undersea",
        "name":"gap"
    },
    "PPLW":{
        "description":"a village, town or city destroyed by a natural disaster, or by war",
        "code":"PPLW",
        "class":"Populated Place",
        "name":"destroyed populated place"
    },
    "PPLX":{
        "description":"",
        "code":"PPLX",
        "class":"Populated Place",
        "name":"section of populated place"
    },
    "RISU":{
        "description":"a broad elevation that rises gently, and generally smoothly, from the sea floor",
        "code":"RISU",
        "class":"Undersea",
        "name":"rise"
    },
    "TRMO":{
        "description":"a tank farm or loading facility at the end of an oil pipeline",
        "code":"TRMO",
        "class":"Spot",
        "name":"oil pipeline terminal"
    },
    "RDGU":{
        "description":"a long narrow elevation with steep sides",
        "code":"RDGU",
        "class":"Undersea",
        "name":"ridge"
    },
    "CUET":{
        "description":"an asymmetric ridge formed on tilted strata",
        "code":"CUET",
        "class":"Hypsographic",
        "name":"cuesta(s)"
    },
    "ISTH":{
        "description":"a narrow strip of land connecting two larger land masses and bordered by water",
        "code":"ISTH",
        "class":"Hypsographic",
        "name":"isthmus"
    },
    "CAVE":{
        "description":"an underground passageway or chamber, or cavity on the side of a cliff",
        "code":"CAVE",
        "class":"Spot",
        "name":"cave(s)"
    },
    "LNDF":{
        "description":"a place for trash and garbage disposal in which the waste is buried between layers of earth to build up low-lying land",
        "code":"LNDF",
        "class":"Spot",
        "name":"landfill"
    },
    "CHNN":{
        "description":"a buoyed channel of sufficient depth for the safe navigation of vessels",
        "code":"CHNN",
        "class":"Hydrographic",
        "name":"navigation channel"
    },
    "CHNM":{
        "description":"that part of a body of water deep enough for navigation through an area otherwise not suitable",
        "code":"CHNM",
        "class":"Hydrographic",
        "name":"marine channel"
    },
    "CHNL":{
        "description":"that part of a lake having water deep enough for navigation between islands, shoals, etc.",
        "code":"CHNL",
        "class":"Hydrographic",
        "name":"lake channel(s)"
    },
    "RDGG":{
        "description":"a linear elevation on an icecap",
        "code":"RDGG",
        "class":"Hydrographic",
        "name":"icecap ridge"
    },
    "RDGE":{
        "description":"a long narrow elevation with steep sides, and a more or less continuous crest",
        "code":"RDGE",
        "class":"Hypsographic",
        "name":"ridge(s)"
    },
    "RDGB":{
        "description":"a ridge of sand just inland and parallel to the beach, usually in series",
        "code":"RDGB",
        "class":"Hypsographic",
        "name":"beach ridge"
    },
    "BP":{
        "description":"a fixture marking a point along a boundary",
        "code":"BP",
        "class":"Spot",
        "name":"boundary marker"
    },
    "TOWR":{
        "description":"a high conspicuous structure, typically much higher than its diameter",
        "code":"TOWR",
        "class":"Spot",
        "name":"tower"
    },
    "DSRT":{
        "description":"a large area with little or no vegetation due to extreme environmental conditions",
        "code":"DSRT",
        "class":"Hypsographic",
        "name":"desert"
    },
    "CONE":{
        "description":"a conical landform composed of mud or volcanic material",
        "code":"CONE",
        "class":"Hypsographic",
        "name":"cone(s)"
    },
    "DAMSB":{
        "description":"a dam put down to bedrock in a sand river",
        "code":"DAMSB",
        "class":"Spot",
        "name":"sub-surface dam"
    },
    "GOSP":{
        "description":"a facility for separating gas from oil",
        "code":"GOSP",
        "class":"Spot",
        "name":"gas-oil separator plant"
    },
    "WTLD":{
        "description":"an area subject to inundation, usually characterized by bog, marsh, or swamp vegetation",
        "code":"WTLD",
        "class":"Hydrographic",
        "name":"wetland"
    },
    "HUTS":{
        "description":"small primitive houses",
        "code":"HUTS",
        "class":"Spot",
        "name":"huts"
    },
    "CNLSB":{
        "description":"a gently inclined underground tunnel bringing water for irrigation from aquifers",
        "code":"CNLSB",
        "class":"Hydrographic",
        "name":"underground irrigation canal(s)"
    },
    "VALG":{
        "description":"a valley the floor of which is notably higher than the valley or shore to which it leads; most common in areas that have been glaciated",
        "code":"VALG",
        "class":"Hypsographic",
        "name":"hanging valley"
    },
    "MESU":{
        "description":"an isolated, extensive, flat-topped elevation on the shelf, with relatively steep sides",
        "code":"MESU",
        "class":"Undersea",
        "name":"mesa"
    },
    "RGN":{
        "description":"an area distinguished by one or more observable physical or cultural characteristics",
        "code":"RGN",
        "class":"Area",
        "name":"region"
    },
    "PS":{
        "description":"a facility for generating electric power",
        "code":"PS",
        "class":"Spot",
        "name":"power station"
    },
    "PP":{
        "description":"a building in which police are stationed",
        "code":"PP",
        "class":"Spot",
        "name":"police post"
    },
    "GRSLD":{
        "description":"an area dominated by grass vegetation",
        "code":"GRSLD",
        "class":"Vegetation",
        "name":"grassland"
    },
    "ADM1H":{
        "description":"a former first-order administrative division",
        "code":"ADM1H",
        "class":"Administrative Boundary",
        "name":"historical first-order administrative division"
    },
    "WTLDI":{
        "description":"",
        "code":"WTLDI",
        "class":"Hydrographic",
        "name":"intermittent wetland"
    },
    "BUR":{
        "description":"a cave used for human burials",
        "code":"BUR",
        "class":"Spot",
        "name":"burial cave(s)"
    },
    "CRDR":{
        "description":"a strip or area of land having significance as an access way",
        "code":"CRDR",
        "class":"Hypsographic",
        "name":"corridor"
    },
    "BGHT":{
        "description":"an open body of water forming a slight recession in a coastline",
        "code":"BGHT",
        "class":"Hydrographic",
        "name":"bight(s)"
    },
    "MALL":{
        "description":"A large, often enclosed shopping complex containing various stores, businesses, and restaurants usually accessible by common passageways.",
        "code":"MALL",
        "class":"Spot",
        "name":"mall"
    },
    "HMDA":{
        "description":"a relatively sand-free, high bedrock plateau in a hot desert, with or without a gravel veneer",
        "code":"HMDA",
        "class":"Hypsographic",
        "name":"rock desert"
    },
    "PK":{
        "description":"a pointed elevation atop a mountain, ridge, or other hypsographic feature",
        "code":"PK",
        "class":"Hypsographic",
        "name":"peak"
    },
    "HBR":{
        "description":"a haven or space of deep water so sheltered by the adjacent land as to afford a safe anchorage for ships",
        "code":"HBR",
        "class":"Hydrographic",
        "name":"harbor(s)"
    },
    "SMSU":{
        "description":"elevations rising generally more than 1,000 meters and of limited extent across the summit",
        "code":"SMSU",
        "class":"Undersea",
        "name":"seamounts"
    },
    "PO":{
        "description":"a public building in which mail is received, sorted and distributed",
        "code":"PO",
        "class":"Spot",
        "name":"post office"
    },
    "ZOO":{
        "description":"a zoological garden or park where wild animals are kept for exhibition",
        "code":"ZOO",
        "class":"Spot",
        "name":"zoo"
    },
    "BAR":{
        "description":"a shallow ridge or mound of coarse unconsolidated material in a stream channel, at the mouth of a stream, estuary, or lagoon and in the wave-break zone along coasts",
        "code":"BAR",
        "class":"Hypsographic",
        "name":"bar"
    },
    "PPLCH":{
        "description":"a former capital of a political entity",
        "code":"PPLCH",
        "class":"Populated Place",
        "name":"historical capital of a political entity"
    },
    "UNIP":{
        "description":"University Preparation Schools & Institutions",
        "code":"UNIP",
        "class":"Spot",
        "name":"university prep school"
    },
    "UNIV":{
        "description":"An institution for higher learning with teaching and research facilities constituting a graduate school and professional schools that award master's degrees and doctorates and an undergraduate division that awards bachelor's degrees.",
        "code":"UNIV",
        "class":"Spot",
        "name":"university"
    },
    "FRZU":{
        "description":"an extensive linear zone of irregular topography of the sea floor, characterized by steep-sided or asymmetrical ridges, troughs, or escarpments",
        "code":"FRZU",
        "class":"Undersea",
        "name":"fracture zone"
    },
    "PSH":{
        "description":"a building where electricity is generated from water power",
        "code":"PSH",
        "class":"Spot",
        "name":"hydroelectric power station"
    },
    "GULF":{
        "description":"a large recess in the coastline, larger than a bay",
        "code":"GULF",
        "class":"Hydrographic",
        "name":"gulf"
    },
    "FRST":{
        "description":"an area dominated by tree vegetation",
        "code":"FRST",
        "class":"Vegetation",
        "name":"forest(s)"
    },
    "SPRU":{
        "description":"a subordinate elevation, ridge, or rise projecting outward from a larger feature",
        "code":"SPRU",
        "class":"Undersea",
        "name":"spur"
    },
    "STRT":{
        "description":"a relatively narrow waterway, usually narrower and less extensive than a sound, connecting two larger bodies of water",
        "code":"STRT",
        "class":"Hydrographic",
        "name":"strait"
    },
    "NVB":{
        "description":"an area used to store supplies, provide barracks for troops and naval personnel, a port for naval vessels, and from which operations are initiated",
        "code":"NVB",
        "class":"Area",
        "name":"naval base"
    },
    "ANS":{
        "description":"a place where archeological remains, old structures, or cultural artifacts are located",
        "code":"ANS",
        "class":"Spot",
        "name":"ancient site"
    },
    "BCN":{
        "description":"a fixed artificial navigation mark",
        "code":"BCN",
        "class":"Spot",
        "name":"beacon"
    },
    "BCH":{
        "description":"a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves",
        "code":"BCH",
        "class":"Hypsographic",
        "name":"beach"
    },
    "USGE":{
        "description":"a facility operated by the United States Government in Panama",
        "code":"USGE",
        "class":"Spot",
        "name":"united states government establishment"
    },
    "DVD":{
        "description":"a line separating adjacent drainage basins",
        "code":"DVD",
        "class":"Hypsographic",
        "name":"divide"
    },
    "FISH":{
        "description":"a fishing ground, bank or area where fishermen go to catch fish",
        "code":"FISH",
        "class":"Hydrographic",
        "name":"fishing area"
    },
    "TMB":{
        "description":"a structure for interring bodies",
        "code":"TMB",
        "class":"Spot",
        "name":"tomb(s)"
    },
    "FLLS":{
        "description":"a perpendicular or very steep descent of the water of a stream",
        "code":"FLLS",
        "class":"Hydrographic",
        "name":"waterfall(s)"
    },
    "RKFL":{
        "description":"an irregular mass of fallen rock at the base of a cliff or steep slope",
        "code":"RKFL",
        "class":"Hypsographic",
        "name":"rockfall"
    },
    "TRNU":{
        "description":"a long, narrow, characteristically very deep and asymmetrical depression of the sea floor, with relatively steep sides",
        "code":"TRNU",
        "class":"Undersea",
        "name":"trench"
    },
    "SCSU":{
        "description":"continuously sloping, elongated depressions commonly found in fans or plains and customarily bordered by levees on one or two sides",
        "code":"SCSU",
        "class":"Undersea",
        "name":"seachannels"
    },
    "HLSU":{
        "description":"elevations rising generally less than 500 meters",
        "code":"HLSU",
        "class":"Undersea",
        "name":"hills"
    },
    "DAMQ":{
        "description":"a destroyed or decayed dam which is no longer functional",
        "code":"DAMQ",
        "class":"Spot",
        "name":"ruined dam"
    },
    "FLLSX":{
        "description":"",
        "code":"FLLSX",
        "class":"Hydrographic",
        "name":"section of waterfall(s)"
    },
    "MOLE":{
        "description":"a massive structure of masonry or large stones serving as a pier or breakwater",
        "code":"MOLE",
        "class":"Spot",
        "name":"mole"
    },
    "SECP":{
        "description":"state exam preparation centres",
        "code":"SECP",
        "class":"Spot",
        "name":"State Exam Prep Centre"
    },
    "MNFE":{
        "description":"a mine where iron ore is extracted",
        "code":"MNFE",
        "class":"Spot",
        "name":"iron mine(s)"
    },
    "DLTA":{
        "description":"a flat plain formed by alluvial deposits at the mouth of a stream",
        "code":"DLTA",
        "class":"Hypsographic",
        "name":"delta"
    },
    "SLID":{
        "description":"a mound of earth material, at the base of a slope and the associated scoured area",
        "code":"SLID",
        "class":"Hypsographic",
        "name":"slide"
    },
    "CH":{
        "description":"a building for public Christian worship",
        "code":"CH",
        "class":"Spot",
        "name":"church"
    },
    "BLDO":{
        "description":"commercial building where business and/or services are conducted",
        "code":"BLDO",
        "class":"Spot",
        "name":"office building"
    },
    "LOCK":{
        "description":"a basin in a waterway with gates at each end by means of which vessels are passed from one water level to another",
        "code":"LOCK",
        "class":"Spot",
        "name":"lock(s)"
    },
    "WAD":{
        "description":"a valley or ravine, bounded by relatively steep banks, which in the rainy season becomes a watercourse; found primarily in North Africa and the Middle East",
        "code":"WAD",
        "class":"Hydrographic",
        "name":"wadi"
    },
    "BLDG":{
        "description":"a structure built for permanent use, as a house, factory, etc.",
        "code":"BLDG",
        "class":"Spot",
        "name":"building(s)"
    },
    "GLCR":{
        "description":"a mass of ice, usually at high latitudes or high elevations, with sufficient thickness to flow away from the source area in lobes, tongues, or masses",
        "code":"GLCR",
        "class":"Hydrographic",
        "name":"glacier(s)"
    },
    "TWO":{
        "description":"Temporary Work Offices",
        "code":"TWO",
        "class":"Spot",
        "name":"temp work office"
    },
    "BLDR":{
        "description":"a high altitude or high latitude bare, flat area covered with large angular rocks",
        "code":"BLDR",
        "class":"Hypsographic",
        "name":"boulder field"
    },
    "COMC":{
        "description":"a facility, including buildings, antennae, towers and electronic equipment for receiving and transmitting information",
        "code":"COMC",
        "class":"Spot",
        "name":"communication center"
    },
    "OBS":{
        "description":"a facility equipped for observation of atmospheric or space phenomena",
        "code":"OBS",
        "class":"Spot",
        "name":"observatory"
    },
    "OILF":{
        "description":"an area containing a subterranean store of petroleum of economic value",
        "code":"OILF",
        "class":"Area",
        "name":"oilfield"
    },
    "PMPW":{
        "description":"a facility for pumping water from a major well or through a pipeline",
        "code":"PMPW",
        "class":"Spot",
        "name":"water pumping station"
    },
    "RDCR":{
        "description":"a road junction formed around a central circle about which traffic moves in one direction only",
        "code":"RDCR",
        "class":"Spot",
        "name":"traffic circle"
    },
    "CTRCM":{
        "description":"a facility for community recreation and other activities",
        "code":"CTRCM",
        "class":"Spot",
        "name":"community center"
    },
    "OILJ":{
        "description":"a section of an oil pipeline where two or more pipes join together",
        "code":"OILJ",
        "class":"Spot",
        "name":"oil pipeline junction"
    },
    "OILT":{
        "description":"a tract of land occupied by large, cylindrical, metal tanks in which oil or liquid petrochemicals are stored",
        "code":"OILT",
        "class":"Spot",
        "name":"tank farm"
    },
    "OILW":{
        "description":"a well from which oil may be pumped",
        "code":"OILW",
        "class":"Spot",
        "name":"oil well"
    },
    "OILP":{
        "description":"a pipeline used for transporting oil",
        "code":"OILP",
        "class":"Road / Railroad",
        "name":"oil pipeline"
    },
    "OILQ":{
        "description":"",
        "code":"OILQ",
        "class":"Spot",
        "name":"abandoned oil well"
    },
    "OILR":{
        "description":"a facility for converting crude oil into refined petroleum products",
        "code":"OILR",
        "class":"Spot",
        "name":"oil refinery"
    },
    "PLN":{
        "description":"an extensive area of comparatively level to gently undulating land, lacking surface irregularities, and usually adjacent to a higher area",
        "code":"PLN",
        "class":"Hypsographic",
        "name":"plain(s)"
    },
    "SLPU":{
        "description":"the slope seaward from the shelf edge to the beginning of a continental rise or the point where there is a general reduction in slope",
        "code":"SLPU",
        "class":"Undersea",
        "name":"slope"
    },
    "PMPO":{
        "description":"a facility for pumping oil through a pipeline",
        "code":"PMPO",
        "class":"Spot",
        "name":"oil pumping station"
    },
    "TMPL":{
        "description":"an edifice dedicated to religious worship",
        "code":"TMPL",
        "class":"Spot",
        "name":"temple(s)"
    },
    "CUTF":{
        "description":"a channel formed as a result of a stream cutting through a meander neck",
        "code":"CUTF",
        "class":"Hydrographic",
        "name":"cutoff"
    },
    "MN":{
        "description":"a site where mineral ores are extracted from the ground by excavating surface pits and subterranean passages",
        "code":"MN",
        "class":"Spot",
        "name":"mine(s)"
    },
    "HDLD":{
        "description":"a high projection of land extending into a large body of water beyond the line of the coast",
        "code":"HDLD",
        "class":"Hypsographic",
        "name":"headland"
    },
    "INSM":{
        "description":"a facility for use of and control by armed forces",
        "code":"INSM",
        "class":"Spot",
        "name":"military installation"
    },
    "STMB":{
        "description":"a conspicuously curved or bent segment of a stream",
        "code":"STMB",
        "class":"Hydrographic",
        "name":"stream bend"
    },
    "PRSH":{
        "description":"an ecclesiastical district",
        "code":"PRSH",
        "class":"Administrative Boundary",
        "name":"parish"
    },
    "RCH":{
        "description":"a straight section of a navigable stream or channel between two bends",
        "code":"RCH",
        "class":"Hydrographic",
        "name":"reach"
    },
    "RECR":{
        "description":"a track where races are held",
        "code":"RECR",
        "class":"Spot",
        "name":"racetrack"
    },
    "ARCH":{
        "description":"a natural or man-made structure in the form of an arch",
        "code":"ARCH",
        "class":"Spot",
        "name":"arch"
    },
    "MFGCU":{
        "description":"a facility for processing copper ore",
        "code":"MFGCU",
        "class":"Spot",
        "name":"copper works"
    },
    "PPL":{
        "description":"a city, town, village",
        "code":"PPL",
        "class":"Populated Place",
        "name":"populated place"
    },
    "NSY":{
        "description":"a place where plants are propagated for transplanting or grafting",
        "code":"NSY",
        "class":"Spot",
        "name":"nursery(-ies)"
    },
    "PPQ":{
        "description":"",
        "code":"PPQ",
        "class":"Spot",
        "name":"abandoned police post"
    },
    "FAN":{
        "description":"a fan-shaped wedge of coarse alluvium with apex merging with a mountain stream bed and the fan spreading out at a low angle slope onto an adjacent plain",
        "code":"FAN",
        "class":"Hypsographic",
        "name":"fan(s)"
    },
    "TERU":{
        "description":"a relatively flat horizontal or gently inclined surface, sometimes long and narrow, which is bounded by a steeper ascending slope on one side and by a steep descending slope on the opposite side",
        "code":"TERU",
        "class":"Undersea",
        "name":"terrace"
    },
    "TERR":{
        "description":"",
        "code":"TERR",
        "class":"Administrative Boundary",
        "name":"territory"
    },
    "RPDS":{
        "description":"a turbulent section of a stream associated with a steep, irregular stream bed",
        "code":"RPDS",
        "class":"Hydrographic",
        "name":"rapids"
    },
    "PANS":{
        "description":"a near-level shallow, natural depression or basin, usually containing an intermittent lake, pond, or pool",
        "code":"PANS",
        "class":"Hypsographic",
        "name":"pans"
    },
    "CNSU":{
        "description":"relatively narrow, deep depressions with steep sides, the bottom of which generally has a continuous slope",
        "code":"CNSU",
        "class":"Undersea",
        "name":"canyons"
    },
    "LKSB":{
        "description":"a standing body of water in a cave",
        "code":"LKSB",
        "class":"Hydrographic",
        "name":"underground lake"
    },
    "PLTU":{
        "description":"a comparatively flat-topped feature of considerable extent, dropping off abruptly on one or more sides",
        "code":"PLTU",
        "class":"Undersea",
        "name":"plateau"
    },
    "INLT":{
        "description":"a narrow waterway extending into the land, or connecting a bay or lagoon with a larger body of water",
        "code":"INLT",
        "class":"Hydrographic",
        "name":"inlet"
    },
    "LEVU":{
        "description":"an embankment bordering a canyon, valley, or seachannel",
        "code":"LEVU",
        "class":"Undersea",
        "name":"levee"
    },
    "MTU":{
        "description":"a well-delineated subdivision of a large and complex positive feature",
        "code":"MTU",
        "class":"Undersea",
        "name":"mountain"
    },
    "CRQS":{
        "description":"bowl-like hollows partially surrounded by cliffs or steep slopes at the head of a glaciated valley",
        "code":"CRQS",
        "class":"Hypsographic",
        "name":"cirques"
    },
    "MESA":{
        "description":"a flat-topped, isolated elevation with steep slopes on all sides, less extensive than a plateau",
        "code":"MESA",
        "class":"Hypsographic",
        "name":"mesa(s)"
    },
    "MLSW":{
        "description":"a mill where logs or lumber are sawn to specified shapes and sizes",
        "code":"MLSW",
        "class":"Spot",
        "name":"sawmill"
    },
    "TNGU":{
        "description":"an elongate (tongue-like) extension of a flat sea floor into an adjacent higher feature",
        "code":"TNGU",
        "class":"Undersea",
        "name":"tongue"
    },
    "CDAU":{
        "description":"an entire mountain system including the subordinate ranges, interior plateaus, and basins",
        "code":"CDAU",
        "class":"Undersea",
        "name":"cordillera"
    },
    "LDGU":{
        "description":"a rocky projection or outcrop, commonly linear and near shore",
        "code":"LDGU",
        "class":"Undersea",
        "name":"ledge"
    },
    "LGNX":{
        "description":"",
        "code":"LGNX",
        "class":"Hydrographic",
        "name":"section of lagoon"
    },
    "MNMT":{
        "description":"a commemorative structure or statue",
        "code":"MNMT",
        "class":"Spot",
        "name":"monument"
    },
    "ASYL":{
        "description":"a facility where the insane are cared for and protected",
        "code":"ASYL",
        "class":"Spot",
        "name":"asylum"
    },
    "RJCT":{
        "description":"a place where two or more railroad tracks join",
        "code":"RJCT",
        "class":"Road / Railroad",
        "name":"railroad junction"
    },
    "ADMDH":{
        "description":"a former administrative division of a political entity, undifferentiated as to administrative level",
        "code":"ADMDH",
        "class":"Administrative Boundary",
        "name":"historical administrative division "
    },
    "SDL":{
        "description":"a broad, open pass crossing a ridge or between hills or mountains",
        "code":"SDL",
        "class":"Hypsographic",
        "name":"saddle"
    },
    "DARY":{
        "description":"a facility for the processing, sale and distribution of milk or milk products",
        "code":"DARY",
        "class":"Spot",
        "name":"dairy"
    },
    "CONT":{
        "description":"continent: Europe, Africa, Asia, North America, South America, Oceania, Antarctica",
        "code":"CONT",
        "class":"Area",
        "name":"continent"
    },
    "CTRM":{
        "description":"a complex of health care buildings including two or more of the following: hospital, medical school, clinic, pharmacy, doctor's offices, etc.",
        "code":"CTRM",
        "class":"Spot",
        "name":"medical center"
    },
    "CTRB":{
        "description":"a place where a number of businesses are located",
        "code":"CTRB",
        "class":"Area",
        "name":"business center"
    },
    "CTRA":{
        "description":"a facility where atomic research is carried out",
        "code":"CTRA",
        "class":"Spot",
        "name":"atomic center"
    },
    "SHLU":{
        "description":"a surface-navigation hazard composed of unconsolidated material",
        "code":"SHLU",
        "class":"Undersea",
        "name":"shoal"
    },
    "CTRF":{
        "description":"a place where more than one facility is situated",
        "code":"CTRF",
        "class":"Spot",
        "name":"facility center"
    },
    "KRST":{
        "description":"a distinctive landscape developed on soluble rock such as limestone characterized by sinkholes, caves, disappearing streams, and underground drainage",
        "code":"KRST",
        "class":"Hypsographic",
        "name":"karst area"
    },
    "OAS":{
        "description":"an area in a desert made productive by the availability of water",
        "code":"OAS",
        "class":"Area",
        "name":"oasis(-es)"
    },
    "STLMT":{
        "description":"",
        "code":"STLMT",
        "class":"Populated Place",
        "name":"israeli settlement"
    },
    "CTRS":{
        "description":"a facility for launching, tracking, or controlling satellites and space vehicles",
        "code":"CTRS",
        "class":"Spot",
        "name":"space center"
    },
    "CTRR":{
        "description":"a facility where more than one religious activity is carried out, e.g., retreat, school, monastery, worship",
        "code":"CTRR",
        "class":"Spot",
        "name":"religious center"
    },
    "WRCK":{
        "description":"the site of the remains of a wrecked vessel",
        "code":"WRCK",
        "class":"Spot",
        "name":"wreck"
    },
    "BOG":{
        "description":"a wetland characterized by peat forming sphagnum moss, sedge, and other acid-water plants",
        "code":"BOG",
        "class":"Hydrographic",
        "name":"bog(s)"
    },
    "ATHF":{
        "description":"a tract of land used for playing team sports, and athletic track and field events",
        "code":"ATHF",
        "class":"Spot",
        "name":"athletic field"
    },
    "TRANT":{
        "description":"facilities for the handling of vehicular freight and passengers",
        "code":"TRANT",
        "class":"Spot",
        "name":"transit terminal"
    },
    "OBPT":{
        "description":"a wildlife or scenic observation point",
        "code":"OBPT",
        "class":"Spot",
        "name":"observation point"
    },
    "RVN":{
        "description":"a small, narrow, deep, steep-sided stream channel, smaller than a gorge",
        "code":"RVN",
        "class":"Hydrographic",
        "name":"ravine(s)"
    },
    "RES":{
        "description":"a tract of public land reserved for future use or restricted as to use",
        "code":"RES",
        "class":"Area",
        "name":"reserve"
    },
    "VETF":{
        "description":"a building or camp at which veterinary services are available",
        "code":"VETF",
        "class":"Spot",
        "name":"veterinary facility"
    },
    "POOLI":{
        "description":"",
        "code":"POOLI",
        "class":"Hydrographic",
        "name":"intermittent pool"
    },
    "TNLRR":{
        "description":"a tunnel through which a railroad passes",
        "code":"TNLRR",
        "class":"Road / Railroad",
        "name":"railroad tunnel"
    },
    "NTKS":{
        "description":"rocks or mountain peaks protruding through glacial ice",
        "code":"NTKS",
        "class":"Hypsographic",
        "name":"nunataks"
    },
    "TNLRD":{
        "description":"a tunnel through which a road passes",
        "code":"TNLRD",
        "class":"Road / Railroad",
        "name":"road tunnel"
    },
    "ISLX":{
        "description":"",
        "code":"ISLX",
        "class":"Hypsographic",
        "name":"section of island"
    },
    "RSVI":{
        "description":"",
        "code":"RSVI",
        "class":"Hydrographic",
        "name":"intermittent reservoir"
    },
    "SQR":{
        "description":"a broad, open, public area near the center of a town or city",
        "code":"SQR",
        "class":"Spot",
        "name":"square"
    },
    "ISLS":{
        "description":"tracts of land, smaller than a continent, surrounded by water at high water",
        "code":"ISLS",
        "class":"Hypsographic",
        "name":"islands"
    },
    "ISLT":{
        "description":"a coastal island connected to the mainland by barrier beaches, levees or dikes",
        "code":"ISLT",
        "class":"Hypsographic",
        "name":"land-tied island"
    },
    "FSR":{
        "description":"a crack associated with volcanism",
        "code":"FSR",
        "class":"Hypsographic",
        "name":"fissure"
    },
    "FJDS":{
        "description":"long, narrow, steep-walled, deep-water arms of the sea at high latitudes, usually along mountainous coasts",
        "code":"FJDS",
        "class":"Hydrographic",
        "name":"fjords"
    },
    "ISLM":{
        "description":"a mangrove swamp surrounded by a waterbody",
        "code":"ISLM",
        "class":"Hypsographic",
        "name":"mangrove island"
    },
    "RSVT":{
        "description":"a contained pool or tank of water at, below, or above ground level",
        "code":"RSVT",
        "class":"Hydrographic",
        "name":"water tank"
    },
    "PYR":{
        "description":"an ancient massive structure of square ground plan with four triangular faces meeting at a point and used for enclosing tombs",
        "code":"PYR",
        "class":"Spot",
        "name":"pyramid"
    },
    "ISLF":{
        "description":"an island created by landfill or diking and filling in a wetland, bay, or lagoon",
        "code":"ISLF",
        "class":"Hypsographic",
        "name":"artificial island"
    },
    "LKN":{
        "description":"an inland body of salt water with no outlet",
        "code":"LKN",
        "class":"Hydrographic",
        "name":"salt lake"
    },
    "LKO":{
        "description":"a crescent-shaped lake commonly found adjacent to meandering streams",
        "code":"LKO",
        "class":"Hydrographic",
        "name":"oxbow lake"
    },
    "BCHS":{
        "description":"a shore zone of coarse unconsolidated sediment that extends from the low-water line to the highest reach of storm waves",
        "code":"BCHS",
        "class":"Hypsographic",
        "name":"beaches"
    },
    "TMTU":{
        "description":"a seamount having a comparatively smooth, flat top",
        "code":"TMTU",
        "class":"Undersea",
        "name":"tablemount (or guyot)"
    },
    "LKI":{
        "description":"",
        "code":"LKI",
        "class":"Hydrographic",
        "name":"intermittent lake"
    },
    "TREE":{
        "description":"a conspicuous tree used as a landmark",
        "code":"TREE",
        "class":"Vegetation",
        "name":"tree(s)"
    },
    "LKC":{
        "description":"a lake in a crater or caldera",
        "code":"LKC",
        "class":"Hydrographic",
        "name":"crater lake"
    },
    "THTR":{
        "description":"A building, room, or outdoor structure for the presentation of plays, films, or other dramatic performances",
        "code":"THTR",
        "class":"Spot",
        "name":"theater"
    },
    "INTF":{
        "description":"a relatively undissected upland between adjacent stream valleys",
        "code":"INTF",
        "class":"Hypsographic",
        "name":"interfluve"
    },
    "LKX":{
        "description":"",
        "code":"LKX",
        "class":"Hydrographic",
        "name":"section of lake"
    },
    "LKS":{
        "description":"large inland bodies of standing water",
        "code":"LKS",
        "class":"Hydrographic",
        "name":"lakes"
    },
    "SNTR":{
        "description":"a facility where victims of physical or mental disorders are treated",
        "code":"SNTR",
        "class":"Spot",
        "name":"sanatorium"
    },
    "SBKH":{
        "description":"a salt flat or salt encrusted plain subject to periodic inundation from flooding or high tides",
        "code":"SBKH",
        "class":"Hydrographic",
        "name":"sabkha(s)"
    },
    "MFGM":{
        "description":"a factory where ammunition is made",
        "code":"MFGM",
        "class":"Spot",
        "name":"munitions plant"
    },
    "MFGN":{
        "description":"diked salt ponds used in the production of solar evaporated salt",
        "code":"MFGN",
        "class":"Hydrographic",
        "name":"salt evaporation ponds"
    },
    "MNQ":{
        "description":"",
        "code":"MNQ",
        "class":"Spot",
        "name":"abandoned mine"
    },
    "MFGB":{
        "description":"one or more buildings where beer is brewed",
        "code":"MFGB",
        "class":"Spot",
        "name":"brewery"
    },
    "MFGC":{
        "description":"a building where food items are canned",
        "code":"MFGC",
        "class":"Spot",
        "name":"cannery"
    },
    "VALU":{
        "description":"a relatively shallow, wide depression, the bottom of which usually has a continuous gradient",
        "code":"VALU",
        "class":"Undersea",
        "name":"valley"
    },
    "RKRY":{
        "description":"a breeding place of a colony of birds or seals",
        "code":"RKRY",
        "class":"Spot",
        "name":"rookery"
    },
    "WALL":{
        "description":"a thick masonry structure, usually enclosing a field or building, or forming the side of a structure",
        "code":"WALL",
        "class":"Spot",
        "name":"wall"
    },
    "GYSR":{
        "description":"a type of hot spring with intermittent eruptions of jets of hot water and steam",
        "code":"GYSR",
        "class":"Hydrographic",
        "name":"geyser"
    },
    "SPA":{
        "description":"a resort area usually developed around a medicinal spring",
        "code":"SPA",
        "class":"Spot",
        "name":"spa"
    },
    "MNN":{
        "description":"a mine from which salt is extracted",
        "code":"MNN",
        "class":"Spot",
        "name":"salt mine(s)"
    },
    "MNA":{
        "description":"an area of mine sites where minerals and ores are extracted",
        "code":"MNA",
        "class":"Area",
        "name":"mining area"
    },
    "MNC":{
        "description":"a mine where coal is extracted",
        "code":"MNC",
        "class":"Spot",
        "name":"coal mine(s)"
    },
    "MND":{
        "description":"a low, isolated, rounded hill",
        "code":"MND",
        "class":"Hypsographic",
        "name":"mound(s)"
    },
    "OPRA":{
        "description":"A theater designed chiefly for the performance of operas.",
        "code":"OPRA",
        "class":"Spot",
        "name":"opera house"
    },
    "BDG":{
        "description":"a structure erected across an obstacle such as a stream, road, etc., in order to carry roads, railroads, and pedestrians across",
        "code":"BDG",
        "class":"Spot",
        "name":"bridge"
    },
    "UPLD":{
        "description":"an extensive interior region of high land with low to moderate surface relief",
        "code":"UPLD",
        "class":"Hypsographic",
        "name":"upland"
    },
    "TRL":{
        "description":"a path, track, or route used by pedestrians, animals, or off-road vehicles",
        "code":"TRL",
        "class":"Road / Railroad",
        "name":"trail"
    },
    "SWT":{
        "description":"facility for the processing of sewage and/or wastewater",
        "code":"SWT",
        "class":"Spot",
        "name":"sewage treatment plant"
    },
    "SLP":{
        "description":"a surface with a relatively uniform slope angle",
        "code":"SLP",
        "class":"Hypsographic",
        "name":"slope(s)"
    },
    "TRB":{
        "description":"a tract of land used by nomadic or other tribes",
        "code":"TRB",
        "class":"Area",
        "name":"tribal area"
    },
    "MLO":{
        "description":"a mill where oil is extracted from olives",
        "code":"MLO",
        "class":"Spot",
        "name":"olive oil mill"
    },
    "BDGQ":{
        "description":"a destroyed or decayed bridge which is no longer functional",
        "code":"BDGQ",
        "class":"Spot",
        "name":"ruined bridge"
    },
    "STMIX":{
        "description":"",
        "code":"STMIX",
        "class":"Hydrographic",
        "name":"section of intermittent stream"
    },
    "CAPE":{
        "description":"a land area, more prominent than a point, projecting into the sea and marking a notable change in coastal direction",
        "code":"CAPE",
        "class":"Hypsographic",
        "name":"cape"
    },
    "CAPG":{
        "description":"a dome-shaped mass of glacial ice covering an area of mountain summits or other high lands; smaller than an ice sheet",
        "code":"CAPG",
        "class":"Hydrographic",
        "name":"icecap"
    },
    "SDLU":{
        "description":"a low part, resembling in shape a saddle, in a ridge or between contiguous seamounts",
        "code":"SDLU",
        "class":"Undersea",
        "name":"saddle"
    },
    "RSTNQ":{
        "description":"",
        "code":"RSTNQ",
        "class":"Spot",
        "name":"abandoned railroad station"
    },
    "HTL":{
        "description":"a building providing lodging and/or meals for the public",
        "code":"HTL",
        "class":"Spot",
        "name":"hotel"
    },
    "RDCUT":{
        "description":"an excavation cut through a hill or ridge for a road",
        "code":"RDCUT",
        "class":"Road / Railroad",
        "name":"road cut"
    },
    "INLTQ":{
        "description":"an inlet which has been filled in, or blocked by deposits",
        "code":"INLTQ",
        "class":"Hydrographic",
        "name":"former inlet"
    },
    "MNAU":{
        "description":"a mine where gold ore, or alluvial gold is extracted",
        "code":"MNAU",
        "class":"Spot",
        "name":"gold mine(s)"
    },
    "HSEC":{
        "description":"a large house, mansion, or chateau, on a large estate",
        "code":"HSEC",
        "class":"Spot",
        "name":"country house"
    },
    "FURU":{
        "description":"a closed, linear, narrow, shallow depression",
        "code":"FURU",
        "class":"Undersea",
        "name":"furrow"
    },
    "SILU":{
        "description":"the low part of a gap or saddle separating basins",
        "code":"SILU",
        "class":"Undersea",
        "name":"sill"
    },
    "HLLU":{
        "description":"an elevation rising generally less than 500 meters",
        "code":"HLLU",
        "class":"Undersea",
        "name":"hill"
    },
    "ESTO":{
        "description":"an estate specializing in the cultivation of oil palm trees",
        "code":"ESTO",
        "class":"Spot",
        "name":"oil palm plantation"
    },
    "ESTT":{
        "description":"an estate which specializes in growing tea bushes",
        "code":"ESTT",
        "class":"Spot",
        "name":"tea plantation"
    },
    "ESTR":{
        "description":"an estate which specializes in growing and tapping rubber trees",
        "code":"ESTR",
        "class":"Spot",
        "name":"rubber plantation"
    },
    "FLDI":{
        "description":"a tract of level or terraced land which is irrigated",
        "code":"FLDI",
        "class":"Area",
        "name":"irrigated field(s)"
    },
    "PENX":{
        "description":"",
        "code":"PENX",
        "class":"Hypsographic",
        "name":"section of peninsula"
    },
    "ESTX":{
        "description":"",
        "code":"ESTX",
        "class":"Spot",
        "name":"section of estate"
    },
    "LKSC":{
        "description":"lakes in a crater or caldera",
        "code":"LKSC",
        "class":"Hydrographic",
        "name":"crater lakes"
    },
    "GRAZ":{
        "description":"an area of grasses and shrubs used for grazing",
        "code":"GRAZ",
        "class":"Area",
        "name":"grazing area"
    },
    "HLLS":{
        "description":"rounded elevations of limited extent rising above the surrounding land with local relief of less than 300m",
        "code":"HLLS",
        "class":"Hypsographic",
        "name":"hills"
    },
    "PNLU":{
        "description":"a high tower or spire-shaped pillar of rock or coral, alone or cresting a summit",
        "code":"PNLU",
        "class":"Undersea",
        "name":"pinnacle"
    },
    "SHVU":{
        "description":"a valley on the shelf, generally the shoreward extension of a canyon",
        "code":"SHVU",
        "class":"Undersea",
        "name":"shelf valley"
    },
    "SALT":{
        "description":"a shallow basin or flat where salt accumulates after periodic inundation",
        "code":"SALT",
        "class":"Area",
        "name":"salt area"
    },
    "RRQ":{
        "description":"",
        "code":"RRQ",
        "class":"Road / Railroad",
        "name":"abandoned railroad"
    },
    "HSP":{
        "description":"a building in which sick or injured, especially those confined to bed, are medically treated",
        "code":"HSP",
        "class":"Spot",
        "name":"hospital"
    },
    "QUAY":{
        "description":"a structure of solid construction along a shore or bank which provides berthing for ships and which generally provides cargo handling facilities",
        "code":"QUAY",
        "class":"Spot",
        "name":"quay"
    },
    "SCHA":{
        "description":"a school with a curriculum focused on agriculture",
        "code":"SCHA",
        "class":"Spot",
        "name":"agricultural school"
    },
    "GHSE":{
        "description":"a house used to provide lodging for paying guests",
        "code":"GHSE",
        "class":"Spot",
        "name":"guest house"
    },
    "CMPRF":{
        "description":"a camp used by refugees",
        "code":"CMPRF",
        "class":"Spot",
        "name":"refugee camp"
    },
    "KNLU":{
        "description":"an elevation rising generally more than 500 meters and less than 1,000 meters and of limited extent across the summit",
        "code":"KNLU",
        "class":"Undersea",
        "name":"knoll"
    },
    "RDA":{
        "description":"the remains of a road used by ancient cultures",
        "code":"RDA",
        "class":"Road / Railroad",
        "name":"ancient road"
    },
    "RGNE":{
        "description":"a region of a country established for economic development or for statistical purposes",
        "code":"RGNE",
        "class":"Area",
        "name":"economic region"
    },
    "RDB":{
        "description":"a conspicuously curved or bent section of a road",
        "code":"RDB",
        "class":"Road / Railroad",
        "name":"road bend"
    },
    "RFSU":{
        "description":"surface-navigation hazards composed of consolidated material",
        "code":"RFSU",
        "class":"Undersea",
        "name":"reefs"
    },
    "RGNH":{
        "description":"a former historic area distinguished by one or more observable physical or cultural characteristics",
        "code":"RGNH",
        "class":"Area",
        "name":"historical region"
    },
    "RGNL":{
        "description":"a tract of land distinguished by numerous lakes",
        "code":"RGNL",
        "class":"Area",
        "name":"lake region"
    },
    "ADM2H":{
        "description":"a former second-order administrative division",
        "code":"ADM2H",
        "class":"Administrative Boundary",
        "name":"historical second-order administrative division"
    },
    "PGDA":{
        "description":"a tower-like storied structure, usually a Buddhist shrine",
        "code":"PGDA",
        "class":"Spot",
        "name":"pagoda"
    },
    "RSRT":{
        "description":"a specialized facility for vacation, health, or participation sports activities",
        "code":"RSRT",
        "class":"Spot",
        "name":"resort"
    },
    "ADM3H":{
        "description":"a former third-order administrative division",
        "code":"ADM3H",
        "class":"Administrative Boundary",
        "name":"historical third-order administrative division"
    },
    "FRMS":{
        "description":"tracts of land with associated buildings devoted to agriculture",
        "code":"FRMS",
        "class":"Spot",
        "name":"farms"
    },
    "FRMQ":{
        "description":"",
        "code":"FRMQ",
        "class":"Spot",
        "name":"abandoned farm"
    },
    "LEV":{
        "description":"a natural low embankment bordering a distributary or meandering stream; often built up artificially to control floods",
        "code":"LEV",
        "class":"Hypsographic",
        "name":"levee"
    },
    "FRMT":{
        "description":"the buildings and adjacent service areas of a farm",
        "code":"FRMT",
        "class":"Spot",
        "name":"farmstead"
    },
    "CULT":{
        "description":"an area under cultivation",
        "code":"CULT",
        "class":"Vegetation",
        "name":"cultivated area"
    },
    "HMCK":{
        "description":"a patch of ground, distinct from and slightly above the surrounding plain or wetland. Often occurs in groups",
        "code":"HMCK",
        "class":"Hypsographic",
        "name":"hammock(s)"
    },
    "MSSNQ":{
        "description":"",
        "code":"MSSNQ",
        "class":"Spot",
        "name":"abandoned mission"
    },
    "GDN":{
        "description":"an enclosure for displaying selected plant or animal life",
        "code":"GDN",
        "class":"Spot",
        "name":"garden(s)"
    },
    "CNLN":{
        "description":"a watercourse constructed for navigation of vessels",
        "code":"CNLN",
        "class":"Hydrographic",
        "name":"navigation canal(s)"
    },
    "CNLI":{
        "description":"a canal which serves as a main conduit for irrigation water",
        "code":"CNLI",
        "class":"Hydrographic",
        "name":"irrigation canal"
    },
    "SPNS":{
        "description":"a place where sulphur ground water flows naturally out of the ground",
        "code":"SPNS",
        "class":"Hydrographic",
        "name":"sulphur spring(s)"
    },
    "CNLD":{
        "description":"an artificial waterway carrying water away from a wetland or from drainage ditches",
        "code":"CNLD",
        "class":"Hydrographic",
        "name":"drainage canal"
    },
    "CMPLA":{
        "description":"a camp used by migrant or temporary laborers",
        "code":"CMPLA",
        "class":"Spot",
        "name":"labor camp"
    },
    "CNLB":{
        "description":"a conspicuously curved or bent section of a canal",
        "code":"CNLB",
        "class":"Hydrographic",
        "name":"canal bend"
    },
    "CNLA":{
        "description":"a conduit used to carry water",
        "code":"CNLA",
        "class":"Hydrographic",
        "name":"aqueduct"
    },
    "SPNT":{
        "description":"a place where hot ground water flows naturally out of the ground",
        "code":"SPNT",
        "class":"Hydrographic",
        "name":"hot spring(s)"
    },
    "GHAT":{
        "description":"a set of steps leading to a river, which are of religious significance, and at their base is usually a platform for bathing",
        "code":"GHAT",
        "class":"Spot",
        "name":"ghat"
    },
    "CMTY":{
        "description":"a burial place or ground",
        "code":"CMTY",
        "class":"Spot",
        "name":"cemetery"
    },
    "CNLX":{
        "description":"",
        "code":"CNLX",
        "class":"Hydrographic",
        "name":"section of canal"
    },
    "SPNG":{
        "description":"a place where ground water flows naturally out of the ground",
        "code":"SPNG",
        "class":"Hydrographic",
        "name":"spring(s)"
    },
    "CNLQ":{
        "description":"",
        "code":"CNLQ",
        "class":"Hydrographic",
        "name":"abandoned canal"
    },
    "STMSB":{
        "description":"a surface stream that disappears into an underground channel, or dries up in an arid area",
        "code":"STMSB",
        "class":"Hydrographic",
        "name":"lost river"
    },
    "RKS":{
        "description":"conspicuous, isolated rocky masses",
        "code":"RKS",
        "class":"Hypsographic",
        "name":"rocks"
    },
    "DAM":{
        "description":"a barrier constructed across a stream to impound water",
        "code":"DAM",
        "class":"Spot",
        "name":"dam"
    },
    "FLD":{
        "description":"an open as opposed to wooded area",
        "code":"FLD",
        "class":"Area",
        "name":"field(s)"
    },
    "AQC":{
        "description":"facility or area for the cultivation of aquatic animals and plants, especially fish, shellfish, and seaweed, in natural or controlled marine or freshwater environments; underwater agriculture",
        "code":"AQC",
        "class":"Spot",
        "name":"aquaculture facility"
    },
    "ESTSG":{
        "description":"an estate that specializes in growing sugar cane",
        "code":"ESTSG",
        "class":"Spot",
        "name":"sugar plantation"
    },
    "SHOR":{
        "description":"a narrow zone bordering a waterbody which covers and uncovers at high and low water, respectively",
        "code":"SHOR",
        "class":"Hypsographic",
        "name":"shore"
    },
    "EST":{
        "description":"a large commercialized agricultural landholding with associated buildings and other facilities",
        "code":"EST",
        "class":"Spot",
        "name":"estate(s)"
    },
    "CNS":{
        "description":"a lease of land by a government for economic development, e.g., mining, forestry",
        "code":"CNS",
        "class":"Area",
        "name":"concession area"
    },
    "GVL":{
        "description":"an area covered with gravel",
        "code":"GVL",
        "class":"Area",
        "name":"gravel area"
    },
    "RNCH":{
        "description":"a large farm specializing in extensive grazing of livestock",
        "code":"RNCH",
        "class":"Spot",
        "name":"ranch(es)"
    },
    "PLAT":{
        "description":"an elevated plain with steep slopes on one or more sides, and often with incised streams",
        "code":"PLAT",
        "class":"Hypsographic",
        "name":"plateau"
    },
    "ARCU":{
        "description":"a low bulge around the southeastern end of the island of Hawaii",
        "code":"ARCU",
        "class":"Undersea",
        "name":"arch"
    },
    "DUNE":{
        "description":"a wave form, ridge or star shape feature composed of sand",
        "code":"DUNE",
        "class":"Hypsographic",
        "name":"dune(s)"
    },
    "ATOL":{
        "description":"a ring-shaped coral reef which has closely spaced islands on it encircling a lagoon",
        "code":"ATOL",
        "class":"Hypsographic",
        "name":"atoll(s)"
    },
    "TNL":{
        "description":"a subterranean passageway for transportation",
        "code":"TNL",
        "class":"Road / Railroad",
        "name":"tunnel"
    },
    "CNL":{
        "description":"an artificial watercourse",
        "code":"CNL",
        "class":"Hydrographic",
        "name":"canal"
    },
    "SHOL":{
        "description":"a surface-navigation hazard composed of unconsolidated material",
        "code":"SHOL",
        "class":"Hydrographic",
        "name":"shoal(s)"
    },
    "SCH":{
        "description":"building(s) where instruction in one or more branches of knowledge takes place",
        "code":"SCH",
        "class":"Spot",
        "name":"school"
    },
    "ANCH":{
        "description":"an area where vessels may anchor",
        "code":"ANCH",
        "class":"Hydrographic",
        "name":"anchorage"
    },
    "BNKX":{
        "description":"",
        "code":"BNKX",
        "class":"Hydrographic",
        "name":"section of bank"
    },
    "INDS":{
        "description":"an area characterized by industrial activity",
        "code":"INDS",
        "class":"Area",
        "name":"industrial area"
    },
    "BNKU":{
        "description":"an elevation, typically located on a shelf, over which the depth of water is relatively shallow but sufficient for safe surface navigation",
        "code":"BNKU",
        "class":"Undersea",
        "name":"bank"
    },
    "SNOW":{
        "description":"an area of permanent snow and ice forming the accumulation area of a glacier",
        "code":"SNOW",
        "class":"Area",
        "name":"snowfield"
    },
    "SHFU":{
        "description":"a zone adjacent to a continent (or around an island) that extends from the low water line to a depth at which there is usually a marked increase of slope towards oceanic depths",
        "code":"SHFU",
        "class":"Undersea",
        "name":"shelf"
    },
    "BNKR":{
        "description":"a sloping margin of a stream channel which normally confines the stream to its channel on land",
        "code":"BNKR",
        "class":"Hydrographic",
        "name":"stream bank"
    },
    "PNDSN":{
        "description":"small standing bodies of salt water often in a marsh or swamp, usually along a seacoast",
        "code":"PNDSN",
        "class":"Hydrographic",
        "name":"salt ponds"
    },
    "BAYS":{
        "description":"coastal indentations between two capes or headlands, larger than a cove but smaller than a gulf",
        "code":"BAYS",
        "class":"Hydrographic",
        "name":"bays"
    },
    "AMTH":{
        "description":"an oval or circular structure with rising tiers of seats about a stage or open space",
        "code":"AMTH",
        "class":"Spot",
        "name":"amphitheater"
    },
    "PNDSI":{
        "description":"",
        "code":"PNDSI",
        "class":"Hydrographic",
        "name":"intermittent ponds"
    },
    "PNDSF":{
        "description":"ponds or enclosures in which fish are kept or raised",
        "code":"PNDSF",
        "class":"Hydrographic",
        "name":"fishponds"
    },
    "MTS":{
        "description":"a mountain range or a group of mountains or high ridges",
        "code":"MTS",
        "class":"Hypsographic",
        "name":"mountains"
    }
}