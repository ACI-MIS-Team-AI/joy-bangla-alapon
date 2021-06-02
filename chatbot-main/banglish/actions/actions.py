from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from fuzzywuzzy import fuzz


class LiberationWarSector19(Action):

    def name(self) -> Text:
        return "action_liberation_war_sector_19"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("sector_no")
        value = value.lower()
        sector_map = {
            'one': 1,
            'two': 2,
            'three':3,
            'four': 4,
            'five' :5,
            'six':6,
            'seven':7,
            'eight' : 8,
            'nine': 9,
            'ten': 10,
            'eleven':11
        }
        sectors = sector_map.keys()
        if value in ["1","one","2","two",'3','4','5','6','7','8','9','10','11','three','four','five','six','seven','eight','nine','ten','eleven']:
            #dispatcher.utter_message(text="In if")
            if value in sectors:
                #dispatcher.utter_message(text=f'ValueUnmap {value}')
                value = sector_map[value]
                #dispatcher.utter_message(text=f'ValueMap {value}')
            else:
                #dispatcher.utter_message(text=f'ValueUnMap {value}')
                value = int(value)
                # dispatcher.utter_message(text="In if if")
                #dispatcher.utter_message(text=f'ValueMap {value}')
            #dispatcher.utter_message(text=f'Value {value}')
            if (value == 1):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ১ এর অধিনে চট্টগ্রাম জেলা, পার্বত্য চট্টগ্রাম এবং নোয়াখালী জেলার পুরো পূর্ব অঞ্চল মুহুরী নদীর তীরে।")
            elif(value == 2):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ২ এর অধিনে ঢাকা, কুমিল্লা, ফরিদপুর এবং নোয়াখালী জেলার কিছু অংশ।")
            elif (value == 3):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৩ এর অধিনে উত্তরে চুরমন কাঠি (শ্রীমঙ্গলের নিকটবর্তী), সিলেট এবং দক্ষিণে ব্রাহ্মণবাড়িয়ার সিঙ্গারবিলের মধ্যবর্তী অঞ্চল।")
            elif (value == 4):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৪ এর অধিনে হবিগঞ্জ জেলা ।")
            elif (value == 5):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৫ এর অধিনে দুর্গাপুর থেকে সিলেট জেলার দাওকি (তামাবিল) পর্যন্ত অঞ্চল এবং জেলার পূর্ব সীমানা পর্যন্ত পুরো অঞ্চল ।")
            elif (value == 6):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৬ এর অধিনে রংপুর জেলা ও দিনাজপুর জেলার অংশ ।")
            elif (value == 7):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৭ এর অধিনে রাজশাহী, পাবনা, বগুড়া এবং দিনাজপুর জেলার অংশ।")
            elif (value == 8):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৮ এর অধিনে কুষ্টিয়া, যশোর, খুলনা, বরিশাল, ফরিদপুর এবং পটুয়াখালী ।")
            elif (value == 9):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ৯ এর অধিনে বরিশাল, পটুয়াখালী এবং খুলনা এবং ফরিদপুর জেলার কিছু অংশ ।")
            elif (value == 10):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ১০ সেক্টরটি নৌ কমান্ডো নিয়ে গঠিত হয়েছিল।")
            elif (value == 11):
                dispatcher.utter_message(text="মুুক্তিযুদ্ধে সেক্টর ১১ এর অধিনে ময়মনসিংহ, টাঙ্গাইলের সাথে রংপুরের কিছু অংশ - গাইবান্ধা, উলিপুর, কমলপুর এবং চিলমারী।")
        else:
            dispatcher.utter_message(text="No such sector")
        #return [SlotSet("counter", counter1)]
        return []

class LiberationWarHonoraryTitle13(Action):

    def name(self) -> Text:
        return "action_liberation_war_honorary_title_13"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("bs_death")
        value = value.lower()
        # dispatcher.utter_message(text=f'{value}')
        bs_map = {
            "1": "Engineroom Room Artificer Mohammad Ruhul Amin",
            "2": "Captain Mohiuddin Jahangir",
            "3": "Flight Lieutenant Motiur Rahman",
            "4": "Lance Naik Munshi Abdur Rouf",
            "5": "Lance Naik Nur Mohammad Sheikh",
            "6": "Sipahi Mustafa Kamal",
            "7": "Sipahi Hamidur Rahman"
        }
        bs_keys = bs_map.keys()
        ratio = []
        for key in bs_keys:
            bs = bs_map[key].lower()
            ratio.append(fuzz.partial_ratio(bs,value))

        # dispatcher.utter_message(text=f'{ratio}')
        max_value = max(ratio)
        max_index = ratio.index(max_value) +1
        if max_index == 1:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ইঞ্জিনরুম আর্টিফিসার মোহাম্মদ রুহুল আমিন মৃত্যু বরণ করেন ১০ ডিসেম্বর ১৯৭১ সালে')
        elif max_index == 2:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর মৃত্যু বরণ করেন ডিসেম্বর ১৪, ১৯৭১ সালে')
        elif max_index == 3:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ফ্লাইট লেফটেন্যান্ট মতিউর রহমান মৃত্যু বরণ করেন ২০ আগস্ট ১৯৭১ সালে')
        elif max_index == 4:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ল্যান্স নায়েক মুন্সি আব্দুর রউফ মৃত্যু বরণ করেন ৮ এপ্রিল ১৯৭১ সালে')
        elif max_index == 5:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ল্যান্স নায়েক নূর মোহাম্মদ শেখ মৃত্যু বরণ করেন সেপ্টেম্বর ৫, ১৯৭১ সালে')
        elif max_index == 6:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ সিপাহী মোস্তফা কামাল মৃত্যু বরণ করেন ১৮ এপ্রিল ১৯৭১ সালে')
        elif max_index == 7:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ সিপাহী হামিদুর রহমান মৃত্যু বরণ করেন ২৮ অক্টোবর ১৯৭১ সালে')
        else:
            dispatcher.utter_message(text=f'Person not found')
        
        
        return []

class LiberationWarHonoraryTitle14(Action):

    def name(self) -> Text:
        return "action_liberation_war_honorary_title_14"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("bs_birth")
        value = value.lower()
        # dispatcher.utter_message(text=f'{value}')
        bs_map = {
            "1": "Engineroom Room Artificer Mohammad Ruhul Amin",
            "2": "Captain Mohiuddin Jahangir",
            "3": "Flight Lieutenant Motiur Rahman",
            "4": "Lance Naik Munshi Abdur Rouf",
            "5": "Lance Naik Nur Mohammad Sheikh",
            "6": "Sipahi Mustafa Kamal",
            "7": "Sipahi Hamidur Rahman"
        }
        bs_keys = bs_map.keys()
        ratio = []
        for key in bs_keys:
            bs = bs_map[key].lower()
            ratio.append(fuzz.partial_ratio(bs,value))

        max_value = max(ratio)
        max_index = int(ratio.index(max_value) + 1)
        if max_index == 1:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ইঞ্জিনরুম আর্টিফিসার মোহাম্মদ রুহুল আমিন জন্ম ১৯৩৫ সালে')
        elif max_index == 2:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ক্যাপ্টেন মহিউদ্দিন জাহাঙ্গীর এর জন্ম ৭ মার্চ ১৯৪৯ সালে')
        elif max_index == 3:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ফ্লাইট লেফটেন্যান্ট মতিউর রহমান এর জন্ম ২৯ অক্টোবর ১৯৪১ সালে')
        elif max_index == 4:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ল্যান্স নায়েক মুন্সি আব্দুর রউফ এর জন্ম ১ মে ১৯৪৩ সালে')
        elif max_index == 5:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ ল্যান্স নায়েক নূর মোহাম্মদ শেখ এর জন্ম ফেব্রুয়ারি ২৬, ১৯৩৬ সালে')
        elif max_index == 6:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ সিপাহী মোস্তফা কামাল এর জন্ম ১৬ ডিসেম্বর ১৯৪৭ সালে')
        elif max_index == 7:
            dispatcher.utter_message(text=f'বীরশ্রেষ্ঠ সিপাহী হামিদুর রহমান এর জন্ম ২ ফেব্রুয়ারি ১৯৫৩ সালে')
        else:
            dispatcher.utter_message(text=f'Person not found')
        
        
        return []

class LiberationWarSecretariate08(Action):

    def name(self) -> Text:
        return "action_liberation_war_secretariate_08"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("post")
        # dispatcher.utter_message(text=f'{value}')
        # value = value.lower()
        post_map = {
            "1": "president",
            "2": "prime minister",
            "3": "prodhan montri",
            "4": "rastro poti"
        }
        post_keys = post_map.keys()
        ratio = []
        for key in post_keys:
            post =  post_map[key].lower()
            ratio.append(fuzz.partial_ratio(post,value))

        max_value = max(ratio)
        max_index = int(ratio.index(max_value) + 1)
        if max_index == 1 or max_index == 4:
            dispatcher.utter_message(text=f'বাংলাদেশের অস্থায়ী সরকারের অন্তর্বর্তীকালীন রাষ্ট্রপতি ছিলেন সৈয়দ নজরুল ইসলাম ।')
        elif max_index == 2 or max_index == 3:
            dispatcher.utter_message(text=f'বাংলাদেশের অস্থায়ী সরকারের প্রধানমন্ত্রী ছিলেন তাজউদ্দীন আহমদ')
        
        else:
            dispatcher.utter_message(text=f'Post not found')
        
        
        return []

class LiberationWarSecretariate13(Action):

    def name(self) -> Text:
        return "action_liberation_war_secretariate_13"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("post_1")
        # value = value.lower()
        # dispatcher.utter_message(text=f'{value}')
        post_map = {
            "1": "chief of staff",
            "2": "deputy chief of staff",
        }
        post_keys = post_map.keys()
        ratio = []
        for key in post_keys:
            post =  post_map[key].lower()
            ratio.append(fuzz.partial_ratio(post,value))

        max_value = max(ratio)
        max_index = int(ratio.index(max_value) + 1)
        if max_index == 1:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে বাংলাদেশের চিফ অফ স্টাফ ছিলেন কর্নেল মোহাম্মদ আব্দুর রব ।।')
        elif max_index == 2:
            dispatcher.utter_message(text=f'কমান্ডার আবদুল করিম খন্দকারকে নতুন রাষ্ট্রের মুক্তিবাহিনীর ডেপুটি চিফ অব স্টাফ উইং পদে নিযুক্ত করা হয়')
        else:
            dispatcher.utter_message(text=f'Post not found')
        
        
        return []

class LiberationWarSector05(Action):

    def name(self) -> Text:
        return "action_liberation_war_sector_05"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.get_slot("sector_area")
        # value = value.lower()
        # dispatcher.utter_message(text=f'{value}')
        area_map = {
            "1": "Kushtia Jessore Khulna Barisal Faridpur Potuakhali]",
            "2": "Chattogram Chittagong",
            "3": "Dhaka Dhakar",
            "4": "Nou Commando",
            "5": "Durgapur",
            "6": "Mymensingh Tangail",
            "7": "Rangpur",
            "8": "Rajshahi Pabna Bogura Bogra",
            "9": "Sylheter Sylhet",
            "10": "Habiganj"
        }
        area_keys = area_map.keys()
        ratio = []
        for key in area_keys:
            area = area_map[key].lower()
            ratio.append(fuzz.partial_ratio(area,value))

        max_value = max(ratio)
        max_index = int(ratio.index(max_value) + 1)
        if max_index == 1:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে কুষ্টিয়া, যশোর, খুলনা, বরিশাল, ফরিদপুর এবং পটুয়াখালী জেলার  সেক্টর কমান্ডার ছিলেন দুইজন। প্রথমে মেজর আবু ওসমান চৌধুরী এবং পরবর্তীতে মেজর আবুল মঞ্জুর।')
        elif max_index == 2:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে চট্টগ্রাম জেলার সেক্টর কমান্ডার ছিলেন দুইজন। প্রথমে মেজর জিয়াউর রহমান এবং পরবর্তীতে ক্যাপ্টেন রফিকুল ইসলাম।')
        elif max_index == 3:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে ঢাকার সেক্টর কমান্ডার ছিলেন মেজর খালেদ মোশাররফ,পরবর্তীতে মেজর এ টি এম হায়দার।')
        elif max_index == 4:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে নৌ কমান্ডো ১০ নম্বর সেক্টর এর অধীনে ছিল। এই সেক্টরটি বাংলাদেশ সশস্ত্র বাহিনীর সদর দপ্তর এর অধীনের পরিচালিত হত।')
        elif max_index == 5:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে দুর্গাপুর সেক্টর কমান্ডার ছিলেন মেজর মীর শওকত আলী')
        elif max_index == 6:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে ময়মনসিংহ ও টাঙ্গাইল জেলার সেক্টর কমান্ডার ছিলেন তিনজন। প্রথমে মেজর জিয়াউর রহমান এবং পরবর্তীতে মেজর আবু তাহের এবং এম হামিদুল্লাহ খান।')
        elif max_index == 7:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে রংপুর জেলার সেক্টর কমান্ডার ছিলেন উইং কমান্ডার এম খাদেমুল বাশার ।')
        elif max_index == 8:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে রাজশাহী, পাবনা, বগুড়া জেলার সেক্টর কমান্ডার ছিলেন দুইজন। প্রথমে সেক্টর কমান্ডার ছিলেন মেজর নাজমুল হক এবং পরবর্তীতে মেজর কাজী নুরুজ্জামান।')
        elif max_index == 9:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধের সময় সিলেট তিনটি সেকটর এর অধীনে ছিলো(৩,৪ ও ৫)। এদের সেক্টর কমানফদার ছিলেন যথাক্রমে মেজর কে এম শফিউল্লাহ,মেজর এ এন এম নুরুজ্জামান[৩], মেজর চিত্তরঞ্জন দত্ত ও ক্যাপ্টেন আবদুর রব[৪] এবং মেজর মীর শওকত আলী।')
        elif max_index == 10:
            dispatcher.utter_message(text=f'মুুক্তিযুদ্ধে হবিগঞ্জ জেলার সেক্টর কমান্ডার ছিলেন মেজর চিত্ত রঞ্জন দত্ত')
        else:
            dispatcher.utter_message(text=f'Sorry, i was not taught about this area.')
        return []

