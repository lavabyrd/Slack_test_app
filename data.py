# loading info for buttons
button_text = {
    "text": "Would you like a game?",
    "attachments": [
        {
            "text": "What would you like to do?",
            "fallback": "You are unable to choose a game",
            "callback_id": "wopr_game",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "game",
                    "text": "Chess",
                    "type": "button",
                    "value": "chess"
                },
                {
                    "name": "game",
                    "text": "Falken's Maze",
                    "type": "button",
                    "value": "maze"
                },
                {
                    "name": "game",
                    "text": "thumbsup",
                    "type": "button",
                    "value": "blah"
                },
                {
                    "name": "game",
                    "text": "Thermonuclear War",
                    "style": "danger",
                    "type": "button",
                    "value": "war",
                    "confirm": {
                        "title": "Are you sure?",
                        "text": "Wouldn't you prefer a good game of chess?",
                        "ok_text": "Yes",
                        "dismiss_text": "No"
                    }
                }
            ]
        }
    ]
}

attachment_text = {
        "attachments": [{
            "text": ":thumbsup: F0 9F 8C 8A",
            "color": "#36a64f",
            "mrkdwn": True
        }]
    }