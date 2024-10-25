from share_strategy import ShareStrategy


class Mail(ShareStrategy):
    def share(self):
        print("I'm emailing the photo")
