from mycroft import MycroftSkill, intent_file_handler


class PlayMusic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('music.play.intent')
    def handle_music_play(self, message):
        self.speak_dialog('music.play')


def create_skill():
    return PlayMusic()

