from typing import Any, List

from project.category import Category
from project.topic import Topic


class Document:
    id: int
    category_id: int
    topic_id: int
    file_name: str
    tags: List[str]

    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str) -> 'Document':
        return cls(
            id,
            category_id=category.id,
            topic_id=topic.id,
            file_name=file_name
        )
