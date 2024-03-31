# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionDefault(Action):
    def name(self) -> Text:
        return "utter_default"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Désolé, je ne comprends pas. Pouvez-vous reformuler votre question ?")
        return []

class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bonjour ! Comment puis-je vous aider aujourd'hui ?")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "utter_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Au revoir ! À bientôt.")
        return []

class ActionThanks(Action):
    def name(self) -> Text:
        return "utter_thanks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="De rien ! N'hésitez pas à me demander si vous avez besoin d'aide supplémentaire.")
        return []

class ActionInform(Action):
    def name(self) -> Text:
        return "utter_inform"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Voici les informations que vous avez demandées.")
        return []

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("location")
        date = tracker.get_slot("date")
        # Logique pour obtenir la météo en fonction de la localisation et de la date
        # Répondre à l'utilisateur avec la météo
        dispatcher.utter_message(text="Voici la météo pour {} le {}.".format(location, date))
        return []

class ActionBookFlight(Action):
    def name(self) -> Text:
        return "action_book_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        destination = tracker.get_slot("location")
        date = tracker.get_slot("date")
        flight_class = tracker.get_slot("flight_class")
        # Logique pour réserver un vol en fonction de la destination, de la date et de la classe de vol
        # Répondre à l'utilisateur avec la confirmation de réservation
        dispatcher.utter_message(text="Votre vol pour {} le {} en classe {} a été réservé.".format(destination, date, flight_class))
        return []

class ActionCancelBooking(Action):
    def name(self) -> Text:
        return "action_cancel_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        destination = tracker.get_slot("location")
        date = tracker.get_slot("date")
        # Logique pour annuler une réservation de vol en fonction de la destination et de la date
        # Répondre à l'utilisateur avec la confirmation d'annulation
        dispatcher.utter_message(text="Votre réservation pour {} le {} a été annulée.".format(destination, date))
        return []

