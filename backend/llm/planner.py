def generate_edit_plan(user_prompt: str):
    """
    Converts user intent into a structured edit plan.
    This is the brain. Not ffmpeg.
    """
    plan = {
        "intent": user_prompt,
        "platform": "instagram",
        "duration": 30,
        "steps": [
            {"tool": "segmenter", "action": "find_best_clips"},
            {"tool": "ffmpeg", "action": "trim_video", "max_duration": 30},
            {"tool": "audio", "action": "add_music", "mood": "emotional"},
            {"tool": "subtitles", "action": "generate"}
        ]
    }
    return plan
