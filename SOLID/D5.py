from abc import ABC, abstractmethod

class Cache(ABC):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value):
        pass

class RedisCache(Cache):
    def __init__(self):
        self._store = {}

    def get(self, key: str):
        return self._store.get(key)

    def set(self, key: str, value):
        self._store[key] = value
        print(f"[Redis] Сохранено: {key}")

class InMemoryCache(Cache):
    def __init__(self):
        self._store = {}

    def get(self, key: str):
        return self._store.get(key)

    def set(self, key: str, value):
        self._store[key] = value
        print(f"[InMemory] Сохранено: {key}")

class ArticleService:
    def __init__(self, cache: Cache):
        self.cache = cache

    def get_article(self, article_id: int) -> dict:
        key = f"article:{article_id}"
        cached = self.cache.get(key)
        if cached:
            return cached
        article = {'id': article_id, 'title': f'Статья #{article_id}'}
        self.cache.set(key, article)
        return article

redis_cache = RedisCache()
service = ArticleService(redis_cache)
print(service.get_article(1))
print(service.get_article(1))  # из кэша

in_memory_cache = InMemoryCache()
test_service = ArticleService(in_memory_cache)
print(test_service.get_article(2))
print(test_service.get_article(2))