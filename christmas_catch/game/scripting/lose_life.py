from game.scripting.action import Action

class LoseLife(Action):
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    