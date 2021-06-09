import abc
import os
import hashlib
import json


class CacheBase(abc.ABC):
    @abc.abstractmethod
    def set(self, key, content):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass


class CachePathNotExistsError(FileNotFoundError):
    pass


class FileCache(CacheBase):
    def __init__(self, cache_path='/tmp/cmdfanyi_cache'):
        if not cache_path or not os.path.isdir(cache_path):
            raise CachePathNotExistsError("No such cache_path: %s" % cache_path)
        self._cache_path = cache_path

    @staticmethod
    def to_cache_key(key):
        md5 = hashlib.md5()
        md5.update(key.encode('utf8'))

        return md5.hexdigest()

    def get_cache_file(self, key):
        return os.path.join(self._cache_path, self.to_cache_key(key))

    def set(self, key, content):
        with open(self.get_cache_file(key), 'wb') as cache:
            cache.write(content.encode('utf8'))

    def get(self, key):
        if not self._has(key):
            return b""
        with open(self.get_cache_file(key), 'rb') as cache:
            return cache.read()

    def _has(self, key):
        return os.path.isfile(self.get_cache_file(key))

    def delete(self, key):
        if not self._has(key):
            return False

        os.unlink(cache_file)
        return True


class JSONCache(CacheBase):
    def __init__(self, cache=None):
        if not cache:
            cache = FileCache()
        self._cache = cache

    def get(self, key, decode_json=True):
        content = self._cache.get(key)
        if not content:
            return ""

        content = content.decode('utf8')
        if not decode_json:
            return content

        return json.loads(content)

    def set(self, key, content):
        if type(content) is not str:
            content = json.dumps(content)
        return self._cache.set(key, content)

    def delete(self, key):
        return self._cache.delete(key)


if __name__ == '__main__':
    cache = JSONCache()
    cache.set('hello', {'hello': True})
    print(cache.get('hello'))

