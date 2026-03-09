#!/usr/bin/env python3
"""
Download R.C. Sproul sermons from learn.ligonier.org and save as Markdown.
Only saves sermons where the teacher is R.C. Sproul.
Saves metadata JSON alongside for map building.
"""

import requests
import re
import json
import time
import sys
from pathlib import Path
from bs4 import BeautifulSoup

SERMONS_DIR = Path(__file__).parent / "sermons"
SERMONS_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; research/1.0)",
    "Accept-Language": "en-US,en;q=0.9",
}

# All 547 sermon URLs from sitemap-sermons.xml
SERMON_URLS = [
    "https://learn.ligonier.org/sermons/conclusion",
    "https://learn.ligonier.org/sermons/jerusalem-illyricum",
    "https://learn.ligonier.org/sermons/bearing-others-burdens",
    "https://learn.ligonier.org/sermons/do-not-cause-another-stumble",
    "https://learn.ligonier.org/sermons/who-are-you",
    "https://learn.ligonier.org/sermons/prologue-johns-gospel",
    "https://learn.ligonier.org/sermons/law-liberty",
    "https://learn.ligonier.org/sermons/put-christ",
    "https://learn.ligonier.org/sermons/christ-and-david",
    "https://learn.ligonier.org/sermons/love-your-neighbor",
    "https://learn.ligonier.org/sermons/submit-government-part-2",
    "https://learn.ligonier.org/sermons/submit-government-part-1",
    "https://learn.ligonier.org/sermons/behave-christian-part-2",
    "https://learn.ligonier.org/sermons/behave-christian-part-1",
    "https://learn.ligonier.org/sermons/serve-god-spiritual-gifts",
    "https://learn.ligonier.org/sermons/living-sacrifices-god",
    "https://learn.ligonier.org/sermons/israels-rejection-not-final-part-4",
    "https://learn.ligonier.org/sermons/israels-rejection-not-final-part-3",
    "https://learn.ligonier.org/sermons/israels-rejection-not-final-part-2",
    "https://learn.ligonier.org/sermons/israels-rejection-not-final-part-1",
    "https://learn.ligonier.org/sermons/israels-rejection-not-total",
    "https://learn.ligonier.org/sermons/israel-rejects-gospel",
    "https://learn.ligonier.org/sermons/israel-needs-gospel",
    "https://learn.ligonier.org/sermons/present-condition-israel",
    "https://learn.ligonier.org/sermons/israels-rejection-gods-justice-part-3",
    "https://learn.ligonier.org/sermons/israels-rejection-gods-justice-part-2",
    "https://learn.ligonier.org/sermons/israels-rejection-gods-justice-part-1",
    "https://learn.ligonier.org/sermons/crucififixion",
    "https://learn.ligonier.org/sermons/israels-rejection-gods-purpose",
    "https://learn.ligonier.org/sermons/israels-rejection-christ",
    "https://learn.ligonier.org/sermons/gods-everlasting-love",
    "https://learn.ligonier.org/sermons/golden-chain",
    "https://learn.ligonier.org/sermons/suffering-glory-part-2",
    "https://learn.ligonier.org/sermons/suffering-glory-part-1",
    "https://learn.ligonier.org/sermons/sanctification",
    "https://learn.ligonier.org/sermons/free-indwelling-sin",
    "https://learn.ligonier.org/sermons/saul-tarsus",
    "https://learn.ligonier.org/sermons/mark-healing-man-unclean",
    "https://learn.ligonier.org/sermons/law-cannot-save-sin-part-3",
    "https://learn.ligonier.org/sermons/law-cannot-save-sin-part-2",
    "https://learn.ligonier.org/sermons/law-cannot-save-sin-part-1",
    "https://learn.ligonier.org/sermons/sins-advantage-law",
    "https://learn.ligonier.org/sermons/freed-law",
    "https://learn.ligonier.org/sermons/slaves-sin-slaves-god",
    "https://learn.ligonier.org/sermons/dead-sin-alive-god-part-2",
    "https://learn.ligonier.org/sermons/dead-sin-alive-god-part",
    "https://learn.ligonier.org/sermons/doctrine-imputation",
    "https://learn.ligonier.org/sermons/great-commission",
    "https://learn.ligonier.org/sermons/matthew-resurrection-2",
    "https://learn.ligonier.org/sermons/matthew-burial-jesus",
    "https://learn.ligonier.org/sermons/give-us-barabbas",
    "https://learn.ligonier.org/sermons/matthew-jesus-pilate",
    "https://learn.ligonier.org/sermons/matthew-peters-denial",
    "https://learn.ligonier.org/sermons/jesus-caiaphas",
    "https://learn.ligonier.org/sermons/jesus-arrest",
    "https://learn.ligonier.org/sermons/garden-gethsemane",
    "https://learn.ligonier.org/sermons/jesus-prediction-peters-denial",
    "https://learn.ligonier.org/sermons/judass-betrayal",
    "https://learn.ligonier.org/sermons/anointing-bethany",
    "https://learn.ligonier.org/sermons/judgment-christ",
    "https://learn.ligonier.org/sermons/parable-talents",
    "https://learn.ligonier.org/sermons/parable-wise-and-foolish-virgins",
    "https://learn.ligonier.org/sermons/faithful-and-evil-servants",
    "https://learn.ligonier.org/sermons/day-and-hour",
    "https://learn.ligonier.org/sermons/coming-son-man",
    "https://learn.ligonier.org/sermons/great-tribulation",
    "https://learn.ligonier.org/sermons/signs-times",
    "https://learn.ligonier.org/sermons/destruction-temple",
    "https://learn.ligonier.org/sermons/jesus-laments-over-jerusalem",
    "https://learn.ligonier.org/sermons/woes-pharisees-part-3",
    "https://learn.ligonier.org/sermons/woes-pharisees-part-2",
    "https://learn.ligonier.org/sermons/woes-pharisees-part-1",
    "https://learn.ligonier.org/sermons/davids-son-and-lord",
    "https://learn.ligonier.org/sermons/first-commandment",
    "https://learn.ligonier.org/sermons/matthew-resurrection",
    "https://learn.ligonier.org/sermons/render-caesar",
    "https://learn.ligonier.org/sermons/parable-marriage-feast",
    "https://learn.ligonier.org/sermons/parable-vineyard",
    "https://learn.ligonier.org/sermons/authority-jesus",
    "https://learn.ligonier.org/sermons/curse-fig-tree",
    "https://learn.ligonier.org/sermons/matthew-cleansing-temple",
    "https://learn.ligonier.org/sermons/matthew-triumphal-entry",
    "https://learn.ligonier.org/sermons/service",
    "https://learn.ligonier.org/sermons/parable-workers",
    "https://learn.ligonier.org/sermons/all-things-are-possible",
    "https://learn.ligonier.org/sermons/rich-young-ruler",
    "https://learn.ligonier.org/sermons/jesus-and-children",
    "https://learn.ligonier.org/sermons/marriage-and-divorce",
    "https://learn.ligonier.org/sermons/unforgiving-servant",
    "https://learn.ligonier.org/sermons/discipline",
    "https://learn.ligonier.org/sermons/parable-lost-sheep",
    "https://learn.ligonier.org/sermons/dealing-temptation",
    "https://learn.ligonier.org/sermons/greatest-kingdom-heaven",
    "https://learn.ligonier.org/sermons/paying-tax",
    "https://learn.ligonier.org/sermons/faithless-generation",
    "https://learn.ligonier.org/sermons/coming-elijah",
    "https://learn.ligonier.org/sermons/transfiguration",
    "https://learn.ligonier.org/sermons/shadow-cross",
    "https://learn.ligonier.org/sermons/great-confession",
    "https://learn.ligonier.org/sermons/leaven-pharisees",
    "https://learn.ligonier.org/sermons/gentile-woman",
    "https://learn.ligonier.org/sermons/inner-defilement",
    "https://learn.ligonier.org/sermons/jesus-walks-water",
    "https://learn.ligonier.org/sermons/feeding-five-thousand",
    "https://learn.ligonier.org/sermons/death-john-baptist",
    "https://learn.ligonier.org/sermons/three-parables",
    "https://learn.ligonier.org/sermons/parable-mustard-seed",
    "https://learn.ligonier.org/sermons/parable-tares",
    "https://learn.ligonier.org/sermons/parable-sower-part-3",
    "https://learn.ligonier.org/sermons/parable-sower-part-2",
    "https://learn.ligonier.org/sermons/parable-sower-part-1",
    "https://learn.ligonier.org/sermons/who-are-my-brothers",
    "https://learn.ligonier.org/sermons/asking-sign",
    "https://learn.ligonier.org/sermons/tree-and-its-fruit",
    "https://learn.ligonier.org/sermons/matthew-unpardonable-sin",
    "https://learn.ligonier.org/sermons/war-between-kingdoms",
    "https://learn.ligonier.org/sermons/servant-lord",
    "https://learn.ligonier.org/sermons/matthew-jesus-lord-sabbath",
    "https://learn.ligonier.org/sermons/yoke-christ",
    "https://learn.ligonier.org/sermons/woes-jesus",
    "https://learn.ligonier.org/sermons/greatness-john-baptist",
    "https://learn.ligonier.org/sermons/john-baptists-inquiry",
    "https://learn.ligonier.org/sermons/jesus-and-division",
    "https://learn.ligonier.org/sermons/fear-god",
    "https://learn.ligonier.org/sermons/persecutions",
    "https://learn.ligonier.org/sermons/matthew-sending-twelve",
    "https://learn.ligonier.org/sermons/call-disciples",
    "https://learn.ligonier.org/sermons/fields-ready-harvest",
    "https://learn.ligonier.org/sermons/compassion-jesus",
    "https://learn.ligonier.org/sermons/healing-daughter",
    "https://learn.ligonier.org/sermons/presence-bridegroom",
    "https://learn.ligonier.org/sermons/call-matthew",
    "https://learn.ligonier.org/sermons/jesus-forgives-sin",
    "https://learn.ligonier.org/sermons/death-adam-life-christ",
    "https://learn.ligonier.org/sermons/time",
    "https://learn.ligonier.org/sermons/matthew-calming-sea",
    "https://learn.ligonier.org/sermons/cost-discipleship-part-2",
    "https://learn.ligonier.org/sermons/cost-discipleship-part-1",
    "https://learn.ligonier.org/sermons/centurions-servant-peters-mother-law",
    "https://learn.ligonier.org/sermons/cleansing-leper",
    "https://learn.ligonier.org/sermons/firm-foundation",
    "https://learn.ligonier.org/sermons/lord-lord",
    "https://learn.ligonier.org/sermons/narrow-way",
    "https://learn.ligonier.org/sermons/ask-and-receive",
    "https://learn.ligonier.org/sermons/matthew-judge-not",
    "https://learn.ligonier.org/sermons/do-not-be-anxious",
    "https://learn.ligonier.org/sermons/treasure-heaven",
    "https://learn.ligonier.org/sermons/lead-us-not-temptation",
    "https://learn.ligonier.org/sermons/thine-kingdom",
    "https://learn.ligonier.org/sermons/forgive-us-our-debts",
    "https://learn.ligonier.org/sermons/daily-bread",
    "https://learn.ligonier.org/sermons/thy-kingdom-come",
    "https://learn.ligonier.org/sermons/hallowed-be-your-name",
    "https://learn.ligonier.org/sermons/our-fathers-house",
    "https://learn.ligonier.org/sermons/sincere-prayer",
    "https://learn.ligonier.org/sermons/private-piety",
    "https://learn.ligonier.org/sermons/loving-our-enemies",
    "https://learn.ligonier.org/sermons/oaths-and-vows",
    "https://learn.ligonier.org/sermons/jesus-view-adultery",
    "https://learn.ligonier.org/sermons/jesus-view-murder",
    "https://learn.ligonier.org/sermons/christ-and-law",
    "https://learn.ligonier.org/sermons/sermon-mount",
    "https://learn.ligonier.org/sermons/beatitudes-part-4",
    "https://learn.ligonier.org/sermons/beatitudes-part-3",
    "https://learn.ligonier.org/sermons/beatitudes-part-2",
    "https://learn.ligonier.org/sermons/beatitudes-part-1",
    "https://learn.ligonier.org/sermons/jesus-disciples-and-ministries",
    "https://learn.ligonier.org/sermons/jesus-goes-galilee",
    "https://learn.ligonier.org/sermons/matthew-temptation-jesus-part-1",
    "https://learn.ligonier.org/sermons/matthew-temptation-jesus-part-2",
    "https://learn.ligonier.org/sermons/matthew-baptism-jesus",
    "https://learn.ligonier.org/sermons/matthew-john-baptist",
    "https://learn.ligonier.org/sermons/slaughter-innocents",
    "https://learn.ligonier.org/sermons/visit-magi",
    "https://learn.ligonier.org/sermons/birth-jesus-matthew",
    "https://learn.ligonier.org/sermons/jewish-look-jesus",
    "https://learn.ligonier.org/sermons/feed-my-sheep",
    "https://learn.ligonier.org/sermons/breakfast-seashore",
    "https://learn.ligonier.org/sermons/doubting-thomas",
    "https://learn.ligonier.org/sermons/resurrection-john",
    "https://learn.ligonier.org/sermons/burial-jesus",
    "https://learn.ligonier.org/sermons/crucifixion-2",
    "https://learn.ligonier.org/sermons/judgment-pilate",
    "https://learn.ligonier.org/sermons/jesus-pilate",
    "https://learn.ligonier.org/sermons/peters-denial",
    "https://learn.ligonier.org/sermons/arrest-jesus",
    "https://learn.ligonier.org/sermons/prayer-church",
    "https://learn.ligonier.org/sermons/intercession",
    "https://learn.ligonier.org/sermons/glory-christ",
    "https://learn.ligonier.org/sermons/overcoming-world",
    "https://learn.ligonier.org/sermons/redemption-applied",
    "https://learn.ligonier.org/sermons/cost-discipleship",
    "https://learn.ligonier.org/sermons/i-am-vine",
    "https://learn.ligonier.org/sermons/legacy",
    "https://learn.ligonier.org/sermons/another-helper",
    "https://learn.ligonier.org/sermons/betrayal",
    "https://learn.ligonier.org/sermons/foot-washing",
    "https://learn.ligonier.org/sermons/one-sent-me",
    "https://learn.ligonier.org/sermons/hour-come",
    "https://learn.ligonier.org/sermons/blessed-king",
    "https://learn.ligonier.org/sermons/expediency-extravagance",
    "https://learn.ligonier.org/sermons/raising-lazarus",
    "https://learn.ligonier.org/sermons/death-lazarus",
    "https://learn.ligonier.org/sermons/son-god",
    "https://learn.ligonier.org/sermons/good-shepherd-discourse",
    "https://learn.ligonier.org/sermons/man-born-blind-part-2",
    "https://learn.ligonier.org/sermons/man-born-blind-part-1",
    "https://learn.ligonier.org/sermons/abraham-freedom",
    "https://learn.ligonier.org/sermons/jesus-self-witness",
    "https://learn.ligonier.org/sermons/woman-caught-adultery",
    "https://learn.ligonier.org/sermons/who-man",
    "https://learn.ligonier.org/sermons/christ-scholar",
    "https://learn.ligonier.org/sermons/unbelief",
    "https://learn.ligonier.org/sermons/hard-sayings",
    "https://learn.ligonier.org/sermons/bread-life",
    "https://learn.ligonier.org/sermons/bread-heaven",
    "https://learn.ligonier.org/sermons/feeding",
    "https://learn.ligonier.org/sermons/witnesses-christ",
    "https://learn.ligonier.org/sermons/son-father",
    "https://learn.ligonier.org/sermons/pool-bethesda",
    "https://learn.ligonier.org/sermons/noblemans-son",
    "https://learn.ligonier.org/sermons/woman-well-part-2",
    "https://learn.ligonier.org/sermons/woman-well-part-1",
    "https://learn.ligonier.org/sermons/jesus-john-baptist",
    "https://learn.ligonier.org/sermons/son-man-lifted-up",
    "https://learn.ligonier.org/sermons/rebirth",
    "https://learn.ligonier.org/sermons/cleansing-temple",
    "https://learn.ligonier.org/sermons/wedding-feast",
    "https://learn.ligonier.org/sermons/lamb-god",
    "https://learn.ligonier.org/sermons/jesus-and-the-angels-part-1",
    "https://learn.ligonier.org/sermons/jesus-and-the-angels-part-2",
    "https://learn.ligonier.org/sermons/brightness-of-glory",
    "https://learn.ligonier.org/sermons/big-letters",
    "https://learn.ligonier.org/sermons/mocking-god",
    "https://learn.ligonier.org/sermons/household-faith",
    "https://learn.ligonier.org/sermons/fruit-spirit",
    "https://learn.ligonier.org/sermons/works-flesh",
    "https://learn.ligonier.org/sermons/circumcision-law",
    "https://learn.ligonier.org/sermons/hagar-sarah",
    "https://learn.ligonier.org/sermons/days-seasons",
    "https://learn.ligonier.org/sermons/adopted-heirs",
    "https://learn.ligonier.org/sermons/christ",
    "https://learn.ligonier.org/sermons/law-gospel",
    "https://learn.ligonier.org/sermons/covenant",
    "https://learn.ligonier.org/sermons/curse-law",
    "https://learn.ligonier.org/sermons/nutty-galatians-part-2",
    "https://learn.ligonier.org/sermons/nutty-galatians-part-1",
    "https://learn.ligonier.org/sermons/crucified-christ",
    "https://learn.ligonier.org/sermons/paul-versus-peter",
    "https://learn.ligonier.org/sermons/paul-circumcision",
    "https://learn.ligonier.org/sermons/paul-jerusalem",
    "https://learn.ligonier.org/sermons/gospel-god",
    "https://learn.ligonier.org/sermons/love-lines-man-pleasing",
    "https://learn.ligonier.org/sermons/another-gospel-gal",
    "https://learn.ligonier.org/sermons/apostolic-greeting-gal",
    "https://learn.ligonier.org/sermons/paul-rome",
    "https://learn.ligonier.org/sermons/paul-malta",
    "https://learn.ligonier.org/sermons/paul-tempest",
    "https://learn.ligonier.org/sermons/almost-persuaded",
    "https://learn.ligonier.org/sermons/pauls-defense",
    "https://learn.ligonier.org/sermons/paul-tried-festus-paul-appeals-caesar",
    "https://learn.ligonier.org/sermons/pauls-defense-felix",
    "https://learn.ligonier.org/sermons/paul-sent-felix",
    "https://learn.ligonier.org/sermons/house-divided-acts",
    "https://learn.ligonier.org/sermons/pauls-defense-jerusalem",
    "https://learn.ligonier.org/sermons/pauls-arrest-jerusalem",
    "https://learn.ligonier.org/sermons/thy-will-be-done",
    "https://learn.ligonier.org/sermons/message-elders",
    "https://learn.ligonier.org/sermons/ministry-troas",
    "https://learn.ligonier.org/sermons/riot-ephesus",
    "https://learn.ligonier.org/sermons/paul-ephesus",
    "https://learn.ligonier.org/sermons/paul-corinth",
    "https://learn.ligonier.org/sermons/paul-mars-hill-part-2",
    "https://learn.ligonier.org/sermons/paul-mars-hill-part-1",
    "https://learn.ligonier.org/sermons/reasoning-scriptures",
    "https://learn.ligonier.org/sermons/philippian-jailer",
    "https://learn.ligonier.org/sermons/doctrine-baptism",
    "https://learn.ligonier.org/sermons/among-brethren",
    "https://learn.ligonier.org/sermons/jerusalem-decree",
    "https://learn.ligonier.org/sermons/judaizer-threat",
    "https://learn.ligonier.org/sermons/entering-kingdom",
    "https://learn.ligonier.org/sermons/zeus-and-hermes",
    "https://learn.ligonier.org/sermons/eternal-appointment",
    "https://learn.ligonier.org/sermons/new-apostle",
    "https://learn.ligonier.org/sermons/epilogue",
    "https://learn.ligonier.org/sermons/be-diligent-and-vigilant",
    "https://learn.ligonier.org/sermons/gods-long-suffering",
    "https://learn.ligonier.org/sermons/empty-words-and-false-liberty",
    "https://learn.ligonier.org/sermons/gods-wrath-for-apostates",
    "https://learn.ligonier.org/sermons/false-prophets-and-teachers",
    "https://learn.ligonier.org/sermons/heed-the-prophetic-word",
    "https://learn.ligonier.org/sermons/remember-these-things",
    "https://learn.ligonier.org/sermons/due-diligence",
    "https://learn.ligonier.org/sermons/more-precious-than-gold",
    "https://learn.ligonier.org/sermons/introduction-and-background",
    "https://learn.ligonier.org/sermons/make-your-calling-sure",
    "https://learn.ligonier.org/sermons/humility-and-alertness",
    "https://learn.ligonier.org/sermons/shepherding-flock",
    "https://learn.ligonier.org/sermons/suffering-as-a-vocation",
    "https://learn.ligonier.org/sermons/doxology",
    "https://learn.ligonier.org/sermons/above-all-fervently-love",
    "https://learn.ligonier.org/sermons/the-end-of-all-things",
    "https://learn.ligonier.org/sermons/armed-with-christs-mind",
    "https://learn.ligonier.org/sermons/saved-through-water",
    "https://learn.ligonier.org/sermons/imprisoned-spirits",
    "https://learn.ligonier.org/sermons/apologetics",
    "https://learn.ligonier.org/sermons/love-life-and-see-good-days",
    "https://learn.ligonier.org/sermons/five-virtues-of-a-healthy-church",
    "https://learn.ligonier.org/sermons/roles-in-marriage",
    "https://learn.ligonier.org/sermons/submission-to-the-shepherd-in-suffering",
    "https://learn.ligonier.org/sermons/be-honorable-sojourners-amidst-gentiles",
    "https://learn.ligonier.org/sermons/stumbling-stones-and-living-stones",
    "https://learn.ligonier.org/sermons/implications-of-the-new-birth",
    "https://learn.ligonier.org/sermons/the-word-of-god-abides-forever",
    "https://learn.ligonier.org/sermons/girded-sober-minds-yield-non-conformity",
    "https://learn.ligonier.org/sermons/christian-joy-amidst-suffering",
    "https://learn.ligonier.org/sermons/election-and-inheritance-evoke-praise",
    "https://learn.ligonier.org/sermons/introduction-and-greetings",
    "https://learn.ligonier.org/sermons/christ-place",
    "https://learn.ligonier.org/sermons/faith-triumphs-trouble-part-3",
    "https://learn.ligonier.org/sermons/faith-triumphs-trouble-part-2",
    "https://learn.ligonier.org/sermons/faith-triumphs-trouble-part-1",
    "https://learn.ligonier.org/sermons/righteousness-revealed",
    "https://learn.ligonier.org/sermons/abraham-justified-faith",
    "https://learn.ligonier.org/sermons/abraham-justified-circumcision",
    "https://learn.ligonier.org/sermons/promise-granted-faith",
    "https://learn.ligonier.org/sermons/boasting-excluded",
    "https://learn.ligonier.org/sermons/indictment-jews-and-gentiles",
    "https://learn.ligonier.org/sermons/gods-judgment-defended",
    "https://learn.ligonier.org/sermons/jews-are-guilty-gentiles",
    "https://learn.ligonier.org/sermons/man-without-excuse",
    "https://learn.ligonier.org/sermons/gods-wrath-unrighteousness",
    "https://learn.ligonier.org/sermons/gods-wrath",
    "https://learn.ligonier.org/sermons/good-bad-fruit",
    "https://learn.ligonier.org/sermons/just-shall-live-faith",
    "https://learn.ligonier.org/sermons/introduction",
    "https://learn.ligonier.org/sermons/witness-king",
    "https://learn.ligonier.org/sermons/peters-second-speech",
    "https://learn.ligonier.org/sermons/pauls-sermon-antioch",
    "https://learn.ligonier.org/sermons/paul-cyprus",
    "https://learn.ligonier.org/sermons/death-herod",
    "https://learn.ligonier.org/sermons/peter-prison",
    "https://learn.ligonier.org/sermons/peters-vision",
    "https://learn.ligonier.org/sermons/team-barnabas-and-saul",
    "https://learn.ligonier.org/sermons/holy-spirit-gentiles",
    "https://learn.ligonier.org/sermons/cornelius-household",
    "https://learn.ligonier.org/sermons/raising-dorcas",
    "https://learn.ligonier.org/sermons/basket-case",
    "https://learn.ligonier.org/sermons/street-called-straight",
    "https://learn.ligonier.org/sermons/pauls-conversion",
    "https://learn.ligonier.org/sermons/ethiopian-eunuch",
    "https://learn.ligonier.org/sermons/gospel-samaria",
    "https://learn.ligonier.org/sermons/stephen-trial",
    "https://learn.ligonier.org/sermons/apostles-and-deacons",
    "https://learn.ligonier.org/sermons/if-it-god",
    "https://learn.ligonier.org/sermons/lying-donors",
    "https://learn.ligonier.org/sermons/holy-boldness",
    "https://learn.ligonier.org/sermons/obeying-god-or-man",
    "https://learn.ligonier.org/sermons/no-other-name",
    "https://learn.ligonier.org/sermons/life-early-church",
    "https://learn.ligonier.org/sermons/the-triumphal-entry",
    "https://learn.ligonier.org/sermons/sons-covenant",
    "https://learn.ligonier.org/sermons/healing-gate-beautiful",
    "https://learn.ligonier.org/sermons/mark-taking-cross",
    "https://learn.ligonier.org/sermons/peters-sermon-part-3",
    "https://learn.ligonier.org/sermons/peters-sermon-part-2",
    "https://learn.ligonier.org/sermons/peters-sermon-part-1",
    "https://learn.ligonier.org/sermons/pentecost",
    "https://learn.ligonier.org/sermons/ascension",
    "https://learn.ligonier.org/sermons/second-account",
    "https://learn.ligonier.org/sermons/mark-great-commission",
    "https://learn.ligonier.org/sermons/mark-resurrection-2",
    "https://learn.ligonier.org/sermons/mark-burial-jesus",
    "https://learn.ligonier.org/sermons/jesus-appears-luke",
    "https://learn.ligonier.org/sermons/mark-atonement",
    "https://learn.ligonier.org/sermons/mark-crucifixion",
    "https://learn.ligonier.org/sermons/mark-jesus-pilate",
    "https://learn.ligonier.org/sermons/mark-garden-gethsemane",
    "https://learn.ligonier.org/sermons/mark-jesus-sanhedrin",
    "https://learn.ligonier.org/sermons/mark-jesus-arrest",
    "https://learn.ligonier.org/sermons/mark-last-supper",
    "https://learn.ligonier.org/sermons/mark-anointing-bethany",
    "https://learn.ligonier.org/sermons/mark-christ-coming-glory",
    "https://learn.ligonier.org/sermons/jesus-temple",
    "https://learn.ligonier.org/sermons/mark-olivet-discourse-part-2",
    "https://learn.ligonier.org/sermons/mark-olivet-discourse-part-1",
    "https://learn.ligonier.org/sermons/mark-scribes-and-widow",
    "https://learn.ligonier.org/sermons/mark-davids-son-and-lord",
    "https://learn.ligonier.org/sermons/mark-great-commandment",
    "https://learn.ligonier.org/sermons/mark-resurrection",
    "https://learn.ligonier.org/sermons/mark-god-and-caesar",
    "https://learn.ligonier.org/sermons/mark-jesus-authority",
    "https://learn.ligonier.org/sermons/mark-parable-vinedressers",
    "https://learn.ligonier.org/sermons/mark-jesus-walking-water",
    "https://learn.ligonier.org/sermons/mark-feeding-five-thousand",
    "https://learn.ligonier.org/sermons/mark-beheading-john-baptist-part-2",
    "https://learn.ligonier.org/sermons/mark-beheading-john-baptist-part-1",
    "https://learn.ligonier.org/sermons/mark-sending-disciples",
    "https://learn.ligonier.org/sermons/mark-jairus-daughter",
    "https://learn.ligonier.org/sermons/jesus-gethsemane-luke",
    "https://learn.ligonier.org/sermons/mark-a-fearful-deliverance",
    "https://learn.ligonier.org/sermons/mark-gadarene-demoniac",
    "https://learn.ligonier.org/sermons/mark-calming-sea",
    "https://learn.ligonier.org/sermons/mark-parables-kingdom",
    "https://learn.ligonier.org/sermons/road-emmaus-luke",
    "https://learn.ligonier.org/sermons/mark-parable-sower",
    "https://learn.ligonier.org/sermons/mark-unpardonable-sin",
    "https://learn.ligonier.org/sermons/resurrection-luke23",
    "https://learn.ligonier.org/sermons/jesus-dies",
    "https://learn.ligonier.org/sermons/mark-calling-disciples",
    "https://learn.ligonier.org/sermons/mark-lord-sabbath",
    "https://learn.ligonier.org/sermons/crucifixion-part-1-luke",
    "https://learn.ligonier.org/sermons/jesus-trial",
    "https://learn.ligonier.org/sermons/peters-denial-luke",
    "https://learn.ligonier.org/sermons/lords-supper-luke",
    "https://learn.ligonier.org/sermons/betrayed",
    "https://learn.ligonier.org/sermons/generation-will-not-pass-away",
    "https://learn.ligonier.org/sermons/render-unto-caesar",
    "https://learn.ligonier.org/sermons/jesus-authority-parable-tenants",
    "https://learn.ligonier.org/sermons/jesus-weeps-over-jerusalem",
    "https://learn.ligonier.org/sermons/triumphal-entry-luke",
    "https://learn.ligonier.org/sermons/parable-minas",
    "https://learn.ligonier.org/sermons/guess-whos-coming-dinner",
    "https://learn.ligonier.org/sermons/blind-man",
    "https://learn.ligonier.org/sermons/rich-young-ruler-luke18",
    "https://learn.ligonier.org/sermons/suffer-little-children-come-unto-me",
    "https://learn.ligonier.org/sermons/pharisee-and-tax-collector",
    "https://learn.ligonier.org/sermons/unjust-judge",
    "https://learn.ligonier.org/sermons/kingdom-come",
    "https://learn.ligonier.org/sermons/cleansing-leper-luke",
    "https://learn.ligonier.org/sermons/unprofitable-servants",
    "https://learn.ligonier.org/sermons/rich-man-lazarus",
    "https://learn.ligonier.org/sermons/pressing-kingdom",
    "https://learn.ligonier.org/sermons/parable-unjust-stweard",
    "https://learn.ligonier.org/sermons/lost-son-part-2",
    "https://learn.ligonier.org/sermons/lost-son-part-1",
    "https://learn.ligonier.org/sermons/cost-discipleship-luke-weekends",
    "https://learn.ligonier.org/sermons/parable-great-supper",
    "https://learn.ligonier.org/sermons/way-humility",
    "https://learn.ligonier.org/sermons/parable-barren-fig",
    "https://learn.ligonier.org/sermons/locus-astonishment",
    "https://learn.ligonier.org/sermons/faithful-steward",
    "https://learn.ligonier.org/sermons/unforgivable-sin",
    "https://learn.ligonier.org/sermons/fearing-god",
    "https://learn.ligonier.org/sermons/simple-way-pray",
    "https://learn.ligonier.org/sermons/martha-mary",
    "https://learn.ligonier.org/sermons/parable-good-samaritan",
    "https://learn.ligonier.org/sermons/return-seventy-two",
    "https://learn.ligonier.org/sermons/crucifixion-part-2-luke",
    "https://learn.ligonier.org/sermons/great-salvation-hebrews",
    "https://learn.ligonier.org/sermons/mark-new-wine-skins",
    "https://learn.ligonier.org/sermons/mark-healing-paralytic",
    "https://learn.ligonier.org/sermons/mark-jesus-heals-many",
    "https://learn.ligonier.org/sermons/mark-beginning-jesus-public-ministry",
    "https://learn.ligonier.org/sermons/mark-baptism-and-temptation-jesus",
    "https://learn.ligonier.org/sermons/mark-john-baptist",
    "https://learn.ligonier.org/sermons/destruction-jerusalem",
    "https://learn.ligonier.org/sermons/resurrection-davids-son",
    "https://learn.ligonier.org/sermons/narrow-way-luke-sep16",
    "https://learn.ligonier.org/sermons/little-leaven",
    "https://learn.ligonier.org/sermons/dividing-christ",
    "https://learn.ligonier.org/sermons/mark-fig-tree-and-temple",
    "https://learn.ligonier.org/sermons/mark-son-man-servant",
    "https://learn.ligonier.org/sermons/mark-kingdom-climbers",
    "https://learn.ligonier.org/sermons/mark-eye-needle",
    "https://learn.ligonier.org/sermons/mark-rich-young-ruler",
    "https://learn.ligonier.org/sermons/mark-marriage-and-divorce",
    "https://learn.ligonier.org/sermons/where-the-worm-does-not-die",
    "https://learn.ligonier.org/sermons/mark-who-greatest",
    "https://learn.ligonier.org/sermons/mark-healing-possessed-boy",
    "https://learn.ligonier.org/sermons/mark-transfiguration-part-2",
    "https://learn.ligonier.org/sermons/mark-transfiguration-part-1",
    "https://learn.ligonier.org/sermons/mark-blind-man-peters-confession",
    "https://learn.ligonier.org/sermons/mark-feeding-four-thousand",
    "https://learn.ligonier.org/sermons/mark-healing-deaf-mute",
    "https://learn.ligonier.org/sermons/mark-syro-phoenician-woman",
    "https://learn.ligonier.org/sermons/mark-defilement-within-part-2",
    "https://learn.ligonier.org/sermons/mark-defilement-within-part-1",
    "https://learn.ligonier.org/sermons/mark-jesus-nazareth",
    "https://learn.ligonier.org/sermons/gospel-luke",
    "https://learn.ligonier.org/sermons/angel-zacharias-part-1",
    "https://learn.ligonier.org/sermons/angel-zacharias-part-2",
    "https://learn.ligonier.org/sermons/angel-zacharias-part-3",
    "https://learn.ligonier.org/sermons/annunciation-sacluke",
    "https://learn.ligonier.org/sermons/marys-fiat",
    "https://learn.ligonier.org/sermons/marys-visit-elizabeth",
    "https://learn.ligonier.org/sermons/magnificat-part-1",
    "https://learn.ligonier.org/sermons/magnificat-part-2",
    "https://learn.ligonier.org/sermons/birth-john-baptist",
    "https://learn.ligonier.org/sermons/benedictus-part-3",
    "https://learn.ligonier.org/sermons/benedictus-part-2",
    "https://learn.ligonier.org/sermons/benedictus-part-1",
    "https://learn.ligonier.org/sermons/birth-jesus",
    "https://learn.ligonier.org/sermons/song-simeon",
    "https://learn.ligonier.org/sermons/ministry-john-baptist",
    "https://learn.ligonier.org/sermons/john-preaches",
    "https://learn.ligonier.org/sermons/baptism-jesus",
    "https://learn.ligonier.org/sermons/genealogy-jesus",
    "https://learn.ligonier.org/sermons/temptation-jesus",
    "https://learn.ligonier.org/sermons/jesus-synagogue",
    "https://learn.ligonier.org/sermons/jesus-rejected",
    "https://learn.ligonier.org/sermons/jesus-meets-demon",
    "https://learn.ligonier.org/sermons/healing-preaching",
    "https://learn.ligonier.org/sermons/gospel-kingdom",
    "https://learn.ligonier.org/sermons/catch-fish",
    "https://learn.ligonier.org/sermons/healing-leper",
    "https://learn.ligonier.org/sermons/authority-forgive",
    "https://learn.ligonier.org/sermons/call-levi",
    "https://learn.ligonier.org/sermons/new-wineskins",
    "https://learn.ligonier.org/sermons/jesus-lord-sabbath",
    "https://learn.ligonier.org/sermons/twelve-apostles-part-1",
    "https://learn.ligonier.org/sermons/twelve-apostles-part-2",
    "https://learn.ligonier.org/sermons/twelve-apostles-part-3",
    "https://learn.ligonier.org/sermons/beatitudes",
    "https://learn.ligonier.org/sermons/blessings-curses",
    "https://learn.ligonier.org/sermons/love-your-enemies",
    "https://learn.ligonier.org/sermons/judge-not",
    "https://learn.ligonier.org/sermons/build-rock",
    "https://learn.ligonier.org/sermons/widows-son",
    "https://learn.ligonier.org/sermons/centurions-servant",
    "https://learn.ligonier.org/sermons/message-john-baptist-part-1",
    "https://learn.ligonier.org/sermons/message-john-baptist-part-2",
    "https://learn.ligonier.org/sermons/forgiven-woman",
    "https://learn.ligonier.org/sermons/parable-sower-luk8",
    "https://learn.ligonier.org/sermons/parable-revealed-light",
    "https://learn.ligonier.org/sermons/calming-storm",
    "https://learn.ligonier.org/sermons/legion",
    "https://learn.ligonier.org/sermons/jairus-daughter-luk51",
    "https://learn.ligonier.org/sermons/sending-twelve",
    "https://learn.ligonier.org/sermons/haunted-guilt",
    "https://learn.ligonier.org/sermons/feeding-5000-luke16",
    "https://learn.ligonier.org/sermons/peters-confession-and-our-cross",
    "https://learn.ligonier.org/sermons/transfiguration-luke",
    "https://learn.ligonier.org/sermons/discipleship-luke",
    "https://learn.ligonier.org/sermons/mission-seventy-two",
    "https://learn.ligonier.org/sermons/asking-knocking",
    "https://learn.ligonier.org/sermons/house-divided",
    "https://learn.ligonier.org/sermons/seeking-sign",
    "https://learn.ligonier.org/sermons/woes-hypocrites",
    "https://learn.ligonier.org/sermons/parable-rich-fool",
    "https://learn.ligonier.org/sermons/end-anxiety",
    "https://learn.ligonier.org/sermons/gods-finite-grace",
    "https://learn.ligonier.org/sermons/place-you",
    "https://learn.ligonier.org/sermons/only-way",
    "https://learn.ligonier.org/sermons/greatest-luke",
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def slug_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def infer_series(slug: str, transcript: str) -> str:
    """Infer the sermon series from slug patterns and transcript content."""
    slug_lower = slug.lower()
    transcript_lower = (transcript or "")[:500].lower()

    if "matthew" in slug_lower or "birth-jesus-matthew" in slug_lower or "jewish-look" in slug_lower:
        return "Matthew"
    if slug_lower.startswith("mark-") or "mark-" in slug_lower:
        return "Mark"
    if any(x in slug_lower for x in ["gospel-luke", "angel-zacharias", "annunciation", "marys-", "magnificat",
            "benedictus", "birth-john", "birth-jesus", "song-simeon", "genealogy", "baptism-jesus",
            "temptation-jesus", "jesus-synagogue", "jesus-rejected", "jesus-meets-demon",
            "healing-preaching", "gospel-kingdom", "catch-fish", "healing-leper", "authority-forgive",
            "call-levi", "new-wineskins", "jesus-lord-sabbath", "twelve-apostles",
            "blessings-curses", "love-your-enemies", "judge-not", "build-rock",
            "widows-son", "centurions-servant", "message-john-baptist", "forgiven-woman",
            "parable-sower-luk", "parable-revealed", "calming-storm", "legion",
            "jairus-daughter", "sending-twelve", "haunted-guilt", "feeding-5000-luke",
            "peters-confession-and", "transfiguration-luke", "discipleship-luke",
            "mission-seventy-two", "asking-knocking", "house-divided", "seeking-sign",
            "woes-hypocrites", "parable-rich-fool", "end-anxiety", "gods-finite-grace",
            "place-you", "only-way", "greatest-luke", "narrow-way-luke", "little-leaven",
            "dividing-christ", "destruction-jerusalem", "resurrection-davids-son",
            "road-emmaus", "jesus-appears-luke", "jesus-gethsemane-luke",
            "crucifixion-part-1-luke", "crucifixion-part-2-luke",
            "peters-denial-luke", "lords-supper-luke", "betrayed",
            "generation-will-not", "render-unto-caesar", "jesus-authority-parable",
            "jesus-weeps-over", "triumphal-entry-luke", "parable-minas",
            "guess-whos-coming", "blind-man", "rich-young-ruler-luke",
            "suffer-little-children", "pharisee-and-tax", "unjust-judge",
            "kingdom-come", "cleansing-leper-luke", "unprofitable-servants",
            "rich-man-lazarus", "pressing-kingdom", "parable-unjust",
            "lost-son", "cost-discipleship-luke", "parable-great-supper",
            "way-humility", "parable-barren-fig", "locus-astonishment",
            "faithful-steward", "unforgivable-sin", "fearing-god",
            "simple-way-pray", "martha-mary", "parable-good-samaritan",
            "return-seventy-two", "resurrection-luke", "jesus-dies",
            "jesus-trial", "jesus-resurrection-luke"]):
        return "Luke"
    if any(x in slug_lower for x in ["prologue-johns", "lamb-god", "wedding-feast",
            "cleansing-temple", "rebirth", "son-man-lifted", "jesus-john-baptist",
            "woman-well", "noblemans-son", "pool-bethesda", "son-father",
            "witnesses-christ", "feeding", "bread-heaven", "bread-life",
            "hard-sayings", "unbelief", "christ-scholar", "who-man",
            "woman-caught-adultery", "jesus-self-witness", "abraham-freedom",
            "man-born-blind", "good-shepherd", "son-god",
            "death-lazarus", "raising-lazarus", "expediency-extravagance",
            "blessed-king", "hour-come", "one-sent-me", "foot-washing",
            "betrayal", "another-helper", "legacy", "i-am-vine",
            "cost-discipleship", "redemption-applied", "overcoming-world",
            "glory-christ", "intercession", "prayer-church", "arrest-jesus",
            "peters-denial", "jesus-pilate", "judgment-pilate",
            "crucifixion-2", "burial-jesus", "resurrection-john",
            "doubting-thomas", "breakfast-seashore", "feed-my-sheep",
            "jewish-look-jesus"]):
        return "John"
    if any(x in slug_lower for x in ["second-account", "ascension", "pentecost",
            "peters-sermon", "healing-gate", "sons-covenant", "the-triumphal-entry",
            "life-early-church", "no-other-name", "obeying-god", "holy-boldness",
            "lying-donors", "if-it-god", "apostles-and-deacons", "stephen-trial",
            "gospel-samaria", "ethiopian-eunuch", "pauls-conversion",
            "street-called-straight", "basket-case", "raising-dorcas",
            "cornelius-household", "holy-spirit-gentiles", "team-barnabas",
            "peters-vision", "peter-prison", "death-herod", "paul-cyprus",
            "pauls-sermon-antioch", "peters-second-speech", "witness-king",
            "new-apostle", "eternal-appointment", "zeus-and-hermes",
            "entering-kingdom", "judaizer-threat", "jerusalem-decree",
            "among-brethren", "doctrine-baptism", "philippian-jailer",
            "reasoning-scriptures", "paul-mars-hill", "paul-corinth",
            "paul-ephesus", "riot-ephesus", "ministry-troas", "message-elders",
            "thy-will-be-done", "pauls-arrest-jerusalem", "pauls-defense-jerusalem",
            "house-divided-acts", "paul-sent-felix", "pauls-defense-felix",
            "paul-tried-festus", "pauls-defense", "almost-persuaded",
            "paul-tempest", "paul-malta", "paul-rome", "epilogue",
            "saul-tarsus", "mark-taking-cross", "the-triumphal-entry"]):
        return "Acts"
    if any(x in slug_lower for x in ["introduction", "just-shall-live", "good-bad-fruit",
            "gods-wrath", "man-without-excuse", "jews-are-guilty",
            "gods-judgment-defended", "indictment-jews", "boasting-excluded",
            "promise-granted", "abraham-justified", "righteousness-revealed",
            "faith-triumphs-trouble", "christ-place",
            "dead-sin-alive-god", "doctrine-imputation",
            "death-adam-life-christ", "time", "slaves-sin",
            "freed-law", "sins-advantage", "law-cannot-save",
            "free-indwelling-sin", "sanctification", "suffering-glory",
            "golden-chain", "gods-everlasting-love",
            "israels-rejection", "israel-rejects", "israel-needs",
            "present-condition-israel", "crucififixion",
            "living-sacrifices", "serve-god-spiritual",
            "behave-christian", "submit-government",
            "love-your-neighbor", "christ-and-david",
            "law-liberty", "put-christ", "bearing-others",
            "do-not-cause-another", "jerusalem-illyricum", "conclusion"]):
        return "Romans"
    if any(x in slug_lower for x in ["apostolic-greeting-gal", "another-gospel-gal",
            "love-lines-man-pleasing", "gospel-god", "paul-jerusalem",
            "paul-circumcision", "paul-versus-peter", "crucified-christ",
            "nutty-galatians", "curse-law", "covenant", "law-gospel",
            "christ", "adopted-heirs", "days-seasons", "hagar-sarah",
            "circumcision-law", "works-flesh", "fruit-spirit",
            "household-faith", "mocking-god", "big-letters",
            "brightness-of-glory", "jesus-and-the-angels"]):
        return "Galatians"
    if any(x in slug_lower for x in ["introduction-and-greetings", "election-and-inheritance",
            "christian-joy-amidst", "girded-sober-minds", "the-word-of-god-abides",
            "implications-of-the-new-birth", "stumbling-stones",
            "be-honorable-sojourners", "submission-to-the-shepherd",
            "roles-in-marriage", "five-virtues", "love-life-and-see",
            "apologetics", "imprisoned-spirits", "saved-through-water",
            "armed-with-christs-mind", "the-end-of-all-things",
            "above-all-fervently", "doxology", "suffering-as-a-vocation",
            "shepherding-flock", "humility-and-alertness",
            "make-your-calling-sure", "introduction-and-background",
            "more-precious-than-gold", "due-diligence",
            "remember-these-things", "heed-the-prophetic",
            "false-prophets-and-teachers", "gods-wrath-for-apostates",
            "empty-words-and-false", "gods-long-suffering",
            "be-diligent-and-vigilant"]):
        if any(x in slug_lower for x in ["introduction-and-greetings", "election-and-inheritance",
                "christian-joy-amidst", "girded-sober-minds", "the-word-of-god-abides",
                "implications-of-the-new-birth", "stumbling-stones",
                "be-honorable-sojourners", "submission-to-the-shepherd",
                "roles-in-marriage", "five-virtues", "love-life-and-see",
                "apologetics", "imprisoned-spirits", "saved-through-water",
                "armed-with-christs-mind", "the-end-of-all-things",
                "above-all-fervently", "doxology", "suffering-as-a-vocation",
                "shepherding-flock", "humility-and-alertness",
                "make-your-calling-sure", "introduction-and-background"]):
            # Check transcript for 1 Peter vs 2 Peter
            if "2 peter" in transcript_lower or "second peter" in transcript_lower:
                return "2 Peter"
            return "1 Peter"
    if "great-salvation-hebrews" in slug_lower:
        return "Hebrews"
    return "Other"


def extract_scripture_from_transcript(transcript: str) -> str:
    """Extract the primary scripture reference from the transcript text."""
    if not transcript:
        return ""
    # Match "Book ch:v" or "Book ch:v-v" patterns, including numbered books
    # Sproul announces the text in the first ~2000 chars
    search_zone = transcript[:2000]
    pattern = re.compile(
        r'\b((?:1|2|3)\s+)?'
        r'(Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|'
        r'(?:1|2)\s+Samuel|(?:1|2)\s+Kings|(?:1|2)\s+Chronicles|Ezra|Nehemiah|Esther|'
        r'Job|Psalms?|Proverbs|Ecclesiastes|Song of Solomon|Isaiah|Jeremiah|'
        r'Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|'
        r'Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|'
        r'Matthew|Mark|Luke|John|Acts|Romans|'
        r'(?:1|2)\s+Corinthians|Galatians|Ephesians|Philippians|Colossians|'
        r'(?:1|2)\s+Thessalonians|(?:1|2)\s+Timothy|Titus|Philemon|Hebrews|'
        r'James|(?:1|2|3)\s+(?:Peter|John)|Jude|Revelation)'
        r'\s+(\d+):(\d+)(?:[:\-–](\d+))?',
        re.IGNORECASE
    )
    m = pattern.search(search_zone)
    if m:
        return m.group(0).strip()
    return ""


def parse_sermon_page(url: str) -> dict | None:
    """Fetch a sermon page and extract structured data. Returns None if not Sproul."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
    except Exception as e:
        return {"error": str(e), "url": url}

    soup = BeautifulSoup(r.text, "html.parser")
    script = soup.find("script", string=re.compile(r"__remixContext"))
    if not script:
        return {"error": "no remixContext", "url": url}

    raw = script.string

    # Locate the currentSermon block specifically (not previousSermon)
    idx = raw.find('"currentSermon"')
    if idx == -1:
        return {"error": "no currentSermon", "url": url}

    block = raw[idx:idx + 20000]

    # Teacher check — must be R.C. Sproul
    if '"rc-sproul"' not in block and "R.C. Sproul" not in block:
        return None

    # Title — first sermonTitle within currentSermon block
    m = re.search(r'"sermonTitle"\s*:\s*"([^"]+)"', block)
    title = m.group(1) if m else slug_from_url(url).replace("-", " ").title()

    # Transcript — decode JSON string escapes properly
    m = re.search(r'"sermonTranscript"\s*:\s*"((?:[^"\\]|\\.)*)"', block)
    if m:
        transcript_raw = m.group(1)
        # Decode JSON string escapes
        transcript = (transcript_raw
                      .replace("\\n", "\n")
                      .replace("\\t", "\t")
                      .replace('\\"', '"')
                      .replace("\\\\", "\\")
                      .replace("\\u003e", ">")
                      .replace("\\u003c", "<")
                      .replace("\\u0026", "&"))
    else:
        transcript = ""

    # Topic hierarchy (names appear in order: topic, parent, grandparent, ...)
    topic_name = topic_parent = topic_grandparent = ""
    topic_start = block.find('"primaryTopic"')
    if topic_start != -1:
        topic_block = block[topic_start:topic_start + 600]
        names = re.findall(r'"name"\s*:\s*"([^"]+)"', topic_block)
        if names:
            topic_name = names[0]
            topic_parent = names[1] if len(names) > 1 else ""
            topic_grandparent = names[2] if len(names) > 2 else ""

    slug = slug_from_url(url)
    series = infer_series(slug, transcript)
    scripture = extract_scripture_from_transcript(transcript)

    return {
        "url": url,
        "slug": slug,
        "title": title,
        "series": series,
        "scripture": scripture,
        "topic": topic_name,
        "topic_parent": topic_parent,
        "topic_grandparent": topic_grandparent,
        "transcript": transcript,
    }


def sermon_to_markdown(data: dict) -> str:
    lines = [
        f"# {data['title']}",
        f"\n**Series:** {data['series']}",
        f"**Scripture:** {data['scripture'] or '(see transcript)'}",
        f"**Topic:** {data['topic']}",
        f"**Source:** [{data['url']}]({data['url']})",
        "\n---\n",
        data["transcript"],
    ]
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    total = len(SERMON_URLS)
    saved = 0
    skipped = 0
    errors = []
    metadata_list = []

    print(f"Downloading {total} sermon pages...\n")

    for i, url in enumerate(SERMON_URLS, 1):
        slug = slug_from_url(url)
        md_path = SERMONS_DIR / f"{slug}.md"
        meta_path = SERMONS_DIR / f"{slug}.json"

        if md_path.exists():
            # Already downloaded — load metadata for map building
            if meta_path.exists():
                with open(meta_path) as f:
                    metadata_list.append(json.load(f))
            skipped += 1
            if i % 50 == 0:
                print(f"  {i}/{total} (skipping already downloaded)")
            continue

        data = parse_sermon_page(url)

        if data is None:
            # Not a Sproul sermon
            skipped += 1
        elif "error" in data:
            print(f"  ERROR {slug}: {data['error']}")
            errors.append(slug)
        else:
            md_path.write_text(sermon_to_markdown(data), encoding="utf-8")
            # Save metadata (without full transcript to keep it small)
            meta = {k: v for k, v in data.items() if k != "transcript"}
            meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
            metadata_list.append(meta)
            saved += 1

        if i % 25 == 0 or i == total:
            print(f"  {i}/{total} — saved: {saved}, skipped: {skipped}, errors: {len(errors)}", flush=True)

        time.sleep(0.5)  # polite rate limit

    # Save combined metadata for map builder
    combined = SERMONS_DIR.parent / "sermon-metadata.json"
    combined.write_text(json.dumps(metadata_list, indent=2), encoding="utf-8")

    print(f"\nDone. {saved} Sproul sermons saved, {skipped} skipped, {len(errors)} errors.")
    if errors:
        print("Errors:", errors)
    print(f"Metadata saved to sermon-metadata.json")
