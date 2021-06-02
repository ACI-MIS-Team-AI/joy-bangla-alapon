from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from fuzzywuzzy import fuzz

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
            "1": "কুষ্টিয়া যশোর খুলনা বরিশাল ফরিদপুর পটুয়াখালী",
            "2": "চট্টগ্রাম চিটাগাং",
            "3": "ঢাকা ঢাকার",
            "4": "নৌ কমান্ডো",
            "5": "দুর্গাপুর",
            "6": "ময়মনসিংহ টাঙ্গাইল",
            "7": "রংপুর",
            "8": "রাজশাহী পাবনা বগুড়া",
            "9": "সিলেটের সিলেট",
            "10": "হবিগঞ্জ"
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