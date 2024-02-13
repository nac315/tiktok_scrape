from page_objects.PageTiktok import PageTiktok
import time

class TiktokAudit(PageTiktok):
    def test_like_hashtag(self):
        self.fetch_tiktok(4)
        self.iterate_through_batches_by_hashtag()
        time.sleep(10)

    def test_like_random(self):
        self.fetch_tiktok(1)
        self.iterate_through_batches_random()
        time.sleep(10)


