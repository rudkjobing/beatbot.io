from django.db import IntegrityError

from core.models import Event


class CrawlingPipeline(object):

    def process_item(self, item, spider):
        try:
            item.save()

        except IntegrityError:
            existing_item: Event = Event.objects.filter(
                venue=item["venue"],
                artist=item["artist"],
                datetime_of_performance=item["datetime_of_performance"]
            ).first()
            if existing_item is not None:
                for genre in item["genres"]:
                    if str(genre) not in existing_item.genres:
                        existing_item.genres.append(genre)
                        existing_item.save(update_fields=["genres"])
        return item
